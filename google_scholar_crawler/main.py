import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime


AUTHOR_ID = "zqfkhZcAAAAJ"
SERPAPI_URL = "https://serpapi.com/search.json"
REQUEST_TIMEOUT_SECONDS = 60
RESULTS_DIR = "../assets/results"


def warn(message):
    # Shown as an annotation on the workflow run summary.
    print(f"::warning::{message}", flush=True)


def fetch_author(api_key):
    query = urllib.parse.urlencode({
        "engine": "google_scholar_author",
        "author_id": AUTHOR_ID,
        "hl": "en",
        "api_key": api_key,
    })
    with urllib.request.urlopen(f"{SERPAPI_URL}?{query}", timeout=REQUEST_TIMEOUT_SECONDS) as resp:
        data = json.load(resp)
    if "error" in data:
        raise RuntimeError(data["error"])
    return data


def cited_by_metric(data, name):
    for row in data.get("cited_by", {}).get("table", []):
        if name in row:
            return row[name].get("all")
    return None


api_key = os.environ.get("SERPAPI_KEY")
if not api_key:
    warn("SERPAPI_KEY secret is not set; keeping existing citation data.")
    sys.exit(0)

try:
    data = fetch_author(api_key)
except (urllib.error.URLError, TimeoutError, RuntimeError, ValueError) as e:
    warn(f"SerpApi request failed ({e}); keeping existing citation data.")
    sys.exit(0)

citations = cited_by_metric(data, "citations")
if citations is None:
    warn("SerpApi response has no citation count; keeping existing citation data.")
    sys.exit(0)

author_info = data.get("author", {})
author = {
    "scholar_id": AUTHOR_ID,
    "name": author_info.get("name"),
    "affiliation": author_info.get("affiliations"),
    "interests": [i.get("title") for i in author_info.get("interests", [])],
    "citedby": citations,
    "hindex": cited_by_metric(data, "h_index"),
    "i10index": cited_by_metric(data, "i10_index"),
    "cites_per_year": {str(g["year"]): g["citations"] for g in data.get("cited_by", {}).get("graph", [])},
    "updated": str(datetime.now()),
}
print(json.dumps(author, indent=2, ensure_ascii=False))

os.makedirs(RESULTS_DIR, exist_ok=True)
with open(f"{RESULTS_DIR}/gs_data.json", "w") as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{citations}",
}
with open(f"{RESULTS_DIR}/gs_data_shieldsio.json", "w") as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
