# Python program showing
# abstract base class work

from abc import ABC, abstractmethod


class MediaDownload(ABC):

    @abstractmethod
    def download_site(self, url):
        pass

    @abstractmethod
    def download_all_sites(self, sites):
        pass
