import requests
import os
from tqdm import tqdm
from neoskola_dl.config import CHUNK_SIZE


class Downloader:
    def __init__(self, url, path):
        self.url = url
        self.path = path
        self._make_dir()

    def _make_dir(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

    def download(self):
        with requests.get(self.url, stream=True) as r:
            total_size = int(r.headers.get('content-length', 0))
            if total_size == 0:
                print("Download Failed")
            progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=self.path)
            with open(self.path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                    progress_bar.update(len(chunk))
                    f.write(chunk)
                    f.flush()
