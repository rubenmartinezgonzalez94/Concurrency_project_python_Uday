import requests
import multiprocessing
from abc import ABC
from clases.MediaDownload import MediaDownload


def set_global_session():
    global session
    if not session:
        session = requests.Session()


class MediaDownloadMultiprocessing(MediaDownload, ABC):
    session = None

    def download_site(self, url):
        with session.get(url) as response:
            name = multiprocessing.current_process().name
            print(f"{name}:Read {len(response.content)} from {url}")

    def download_all_sites(self, sites):
        with multiprocessing.Pool() as pool:
            pool.map(MediaDownloadMultiprocessing.download_site, sites)
