import concurrent.futures
import threading
from abc import ABC

import requests

from clases.MediaDownload import MediaDownload


class MediaDownloadThreading(MediaDownload, ABC):
    thread_local = threading.local()

    @staticmethod
    def get_session():
        if not hasattr(MediaDownloadThreading.thread_local, "session"):
            MediaDownloadThreading.thread_local.session = requests.Session()
        return MediaDownloadThreading.thread_local.session

    def download_site(self, url):
        session = MediaDownloadThreading.get_session()
        with session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")

    def download_all_sites(self, sites):
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(MediaDownloadThreading.download_site, sites)
