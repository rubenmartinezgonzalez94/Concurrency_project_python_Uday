import time

from clases import MediaDownloadSynchronous
from clases.MediaDownloadMultiprocessing import MediaDownloadMultiprocessing
from clases.MediaDownloadThreading import MediaDownloadThreading

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 2
    start_time = time.time()

    sy = MediaDownloadSynchronous.MediaDownloadSynchronous()
    th = MediaDownloadThreading()
    mu = MediaDownloadMultiprocessing()

    #sy.download_all_sites(sites)
    #th.download_all_sites(sites)
    mu.download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
