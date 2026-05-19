from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime
import os
import time

# Set up free proxy to bypass Google Scholar blocking
pg = ProxyGenerator()
success = pg.FreeProxies()
if success:
    scholarly.use_proxy(pg)
    print("Proxy configured")
else:
    print("Warning: no proxy available")

MAX_RETRIES = 3
for attempt in range(MAX_RETRIES):
    try:
        print(f"Attempt {attempt + 1}/{MAX_RETRIES}")
        author = scholarly.search_author_id("zqfkhZcAAAAJ")
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
        break
    except Exception as e:
        print(f"Failed: {e}")
        if attempt < MAX_RETRIES - 1:
            time.sleep(10)
        else:
            raise

name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2, default=str))
os.makedirs('../assets/results', exist_ok=True)
with open('../assets/results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False, default=str)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author['citedby']}",
}
with open('../assets/results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
