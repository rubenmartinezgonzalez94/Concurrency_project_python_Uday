import requests
import multiprocessing
from abc import ABC
from clases.MediaDownload import MediaDownload


class MediaDownloadMultiprocessing(MediaDownload, ABC):
    session = None

    def set_global_session(self):

        if not self.session:
            self.session = requests.Session()

    def download_site(self, url):
        with self.session.get(url) as response:
            name = multiprocessing.current_process().name
            print(f"{name}:Read {len(response.content)} from {url}")

    def download_all_sites(self, sites):
        with multiprocessing.Pool() as pool:
            pool.map(self.download_site, sites)
