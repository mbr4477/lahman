import os.path as path
import pandas as pd
from ._csv_reader import CSVReader
from ._injector import Injector
from ._locator import LahmanLocator
from ._downloader import LahmanDownloader
from typing import Optional
from os import path


class LahmanNotFound(RuntimeError):
    def __init__(self, root_dir: str):
        super().__init__(f"Couldn't find Lahman database in {root_dir}")


class LahmanData:
    """The Lahman Baseball Database.
    https://www.seanlahman.com/baseball-archive/statistics
    """

    def __init__(
        self,
        download: bool = True,
        root_dir: str = ".",
        zip_url: str = "https://github.com/chadwickbureau/baseballdatabank/archive/refs/tags/v2022.2.zip",
        csv_reader: Optional[CSVReader] = None,
        locator: Optional[LahmanLocator] = None,
        downloader: Optional[LahmanDownloader] = None,
    ):
        """
        Args:
            download: If True, download the data if it doesn't exist
                at the expected location.
            root_dir: The directory in which to store the database.
            zip_url: The URL to the latest zip file of the data set.
            csv_reader: Optional, override the CSVReader.
            locator: Optional, override the LahmanLocator.
            downloader: Optional, override the LahmanDownloader.
        """
        self._root_dir = root_dir
        self._locator = locator if locator is not None else Injector.locator()
        self._downloader = (
            downloader if downloader is not None else Injector.downloader()
        )

        # Look for existing folder
        self._folder_path = self._locator.locate(root_dir)
        if self._folder_path is None and download:
            self._downloader.download(zip_url, root_dir)
            self._folder_path = self._locator.locate(root_dir)

        if self._folder_path is None:
            raise LahmanNotFound(path.abspath(root_dir))

        self._version = self._folder_path.rsplit("-", 1)[-1]
        print(f"Using Lahman Database v{self._version}")

        # Inject the csv reader
        self._csv_reader = (
            csv_reader if csv_reader is not None else Injector.csv_reader()
        )

    def _get_csv(self, relative_path: str) -> pd.DataFrame:
        """Get a CSV file inside the databank as a data frame.

        Args:
            relative_path: The path to the CSV inside the databank.
        """
        full_path = path.join(self._folder_path, relative_path)
        return self._csv_reader.read_csv(full_path)

    def all_star_full(self) -> pd.DataFrame:
        """Get core/AllstarFull data."""
        return self._get_csv(path.join("core", "AllstarFull.csv"))

    def appearances(self) -> pd.DataFrame:
        """Get core/Appearances data."""
        return self._get_csv(path.join("core", "Appearances.csv"))

    def batting(self) -> pd.DataFrame:
        """Get core/Batting data."""
        return self._get_csv(path.join("core", "Batting.csv"))

    def batting_post(self) -> pd.DataFrame:
        """Get core/BattingPost data."""
        return self._get_csv(path.join("core", "BattingPost.csv"))

    def fielding(self) -> pd.DataFrame:
        """Get core/Fielding data."""
        return self._get_csv(path.join("core", "Fielding.csv"))

    def fielding_of(self) -> pd.DataFrame:
        """Get core/FieldingOF data."""
        return self._get_csv(path.join("core", "FieldingOF.csv"))

    def fielding_of_split(self) -> pd.DataFrame:
        """Get core/FieldingOFsplit data."""
        return self._get_csv(path.join("core", "FieldingOFsplit.csv"))

    def fielding_post(self) -> pd.DataFrame:
        """Get core/FieldingPost data."""
        return self._get_csv(path.join("core", "FieldingPost.csv"))

    def home_games(self) -> pd.DataFrame:
        """Get core/HomeGames data."""
        return self._get_csv(path.join("core", "HomeGames.csv"))

    def managers(self) -> pd.DataFrame:
        """Get core/Managers data."""
        return self._get_csv(path.join("core", "Managers.csv"))

    def managers_half(self) -> pd.DataFrame:
        """Get core/ManagersHalf data."""
        return self._get_csv(path.join("core", "ManagersHalf.csv"))

    def parks(self) -> pd.DataFrame:
        """Get core/Parks data."""
        return self._get_csv(path.join("core", "Parks.csv"))

    def people(self) -> pd.DataFrame:
        """Get core/People data."""
        return self._get_csv(path.join("core", "People.csv"))

    def pitching(self) -> pd.DataFrame:
        """Get core/Pitching data."""
        return self._get_csv(path.join("core", "Pitching.csv"))

    def pitching_post(self) -> pd.DataFrame:
        """Get core/PitchingPost data."""
        return self._get_csv(path.join("core", "PitchingPost.csv"))

    def series_post(self) -> pd.DataFrame:
        """Get core/SeriesPost data."""
        return self._get_csv(path.join("core", "SeriesPost.csv"))

    def teams(self) -> pd.DataFrame:
        """Get core/Teams data."""
        return self._get_csv(path.join("core", "Teams.csv"))

    def teams_franchises(self) -> pd.DataFrame:
        """Get core/TeamsFranchises data."""
        return self._get_csv(path.join("core", "TeamsFranchises.csv"))

    def teams_half(self) -> pd.DataFrame:
        """Get core/TeamsHalf data."""
        return self._get_csv(path.join("core", "TeamsHalf.csv"))
