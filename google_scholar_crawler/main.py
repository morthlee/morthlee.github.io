from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime
import os

# Set up free proxy to avoid Google Scholar blocking
try:
    pg = ProxyGenerator()
    success = pg.FreeProxies()
    if success:
        scholarly.use_proxy(pg)
        print("Using free proxy")
    else:
        print("No proxy available, proceeding without proxy")
except Exception as e:
    print(f"Proxy setup failed: {e}, proceeding without proxy")

author: dict = scholarly.search_author_id("zqfkhZcAAAAJ")
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
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
