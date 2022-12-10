from abc import ABC, abstractmethod
import requests
import zipfile
import os
import io


class LahmanDownloader(ABC):
    """A generic interface for downloading and unzipping the Lahman data."""

    @abstractmethod
    def download(self, zip_url: str, root_dir: str):
        """Download the Lahman data and unzip into the root_dir.

        Args:
            zip_url: The URL of the Lahman zip file.
            root_dir: The directory in which to put the database.
        """
        pass


class RequestsDownloader(LahmanDownloader):
    def download(self, zip_url: str, root_dir: str):
        print(f"Downloading from {zip_url} ... ", end="", flush=True)
        req = requests.get(zip_url)
        z = zipfile.ZipFile(io.BytesIO(req.content))
        os.makedirs(root_dir, exist_ok=True)
        z.extractall(root_dir)
        print(f"Done")
