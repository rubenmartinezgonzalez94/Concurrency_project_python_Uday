import concurrent.futures
import threading
from abc import ABC

import requests

from clases.MediaDownload import MediaDownload


class MediaDownloadThreading(MediaDownload, ABC):
    thread_local = threading.local()

    def get_session(self):
        if not hasattr(MediaDownloadThreading.thread_local, "session"):
            MediaDownloadThreading.thread_local.session = requests.Session()
        return self.thread_local.session

    def download_site(self, url):
        session = self.get_session()
        with session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")

    def download_all_sites(self, sites):
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(self.download_site, sites)
