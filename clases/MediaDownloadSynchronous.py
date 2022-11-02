from abc import ABC

import requests

from clases.MediaDownload import MediaDownload


class MediaDownloadSynchronous(MediaDownload, ABC):

    def download_site(self, url, session):
        with session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")

    def download_all_sites(self, sites):
        with requests.Session() as session:
            for url in sites:
                self.download_site(url, session)
