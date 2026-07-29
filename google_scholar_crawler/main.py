from scholarly import scholarly
import json
from datetime import datetime
import os
import signal
import time
from contextlib import contextmanager


MAX_RETRIES = 3
ATTEMPT_TIMEOUT_SECONDS = 60
RETRY_DELAY_SECONDS = 10


class ScholarTimeoutError(TimeoutError):
    pass


def timeout_handler(signum, frame):
    raise ScholarTimeoutError(
        f"Google Scholar request exceeded {ATTEMPT_TIMEOUT_SECONDS} seconds"
    )


@contextmanager
def request_timeout(seconds):
    if not hasattr(signal, "SIGALRM"):
        yield
        return

    previous_handler = signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous_handler)


for attempt in range(MAX_RETRIES):
    try:
        print(f"Attempt {attempt + 1}/{MAX_RETRIES}", flush=True)
        with request_timeout(ATTEMPT_TIMEOUT_SECONDS):
            author = scholarly.search_author_id("zqfkhZcAAAAJ")
            scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
        break
    except Exception as e:
        print(f"Failed: {e}", flush=True)
        if attempt < MAX_RETRIES - 1:
            time.sleep(RETRY_DELAY_SECONDS)
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
