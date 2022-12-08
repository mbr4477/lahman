import os.path as path
import requests
import zipfile
import io
import os
import glob
import pandas as pd


class LahmanData:
    """The Lahman Baseball Database.
    https://www.seanlahman.com/baseball-archive/statistics
    """

    def __init__(
        self,
        download: bool = True,
        root_dir: str = ".",
        zip_url: str = "https://github.com/chadwickbureau/baseballdatabank/archive/refs/tags/v2022.2.zip",
    ):
        """
        Args:
            download: If True, download the data if it doesn't exist
                at the expected location.
            root_dir: The directory in which to store the database.
            zip_url: The URL to the latest zip file of the data set.
        """
        self._root_dir = root_dir

        # Look for existing folder
        candidates = glob.glob(path.join(root_dir, "baseballdatabank-*"))
        if len(candidates) > 0:
            self._folder_path = candidates[0]
        elif download:
            print(f"Downloading from {zip_url} ... ", end="", flush=True)
            req = requests.get(zip_url)
            z = zipfile.ZipFile(io.BytesIO(req.content))
            os.makedirs(root_dir, exist_ok=True)
            z.extractall(root_dir)
            print(f"Done")
            self._folder_path = glob.glob(path.join(root_dir, "baseballdatabank-*"))[0]

        self._version = self._folder_path.rsplit("-", 1)[-1]
        print(f"Using Lahman Database v{self._version}")

    def _get_csv(self, relative_path: str) -> pd.DataFrame:
        """Get a CSV file inside the databank as a data frame.

        Args:
            relative_path: The path to the CSV inside the databank.
        """
        full_path = path.join(self._folder_path, relative_path)
        return pd.read_csv(full_path)

    def all_star_full(self) -> pd.DataFrame:
        """Get core/AllstarFull data."""
        return self._get_csv("core/AllstarFull.csv")

    def appearances(self) -> pd.DataFrame:
        """Get core/Appearances data."""
        return self._get_csv("core/Appearances.csv")

    def batting(self) -> pd.DataFrame:
        """Get core/Batting data."""
        return self._get_csv("core/Batting.csv")

    def batting_post(self) -> pd.DataFrame:
        """Get core/BattingPost data."""
        return self._get_csv("core/BattingPost.csv")

    def fielding(self) -> pd.DataFrame:
        """Get core/Fielding data."""
        return self._get_csv("core/Fielding.csv")

    def fielding_of(self) -> pd.DataFrame:
        """Get core/FieldingOF data."""
        return self._get_csv("core/FieldingOF.csv")

    def fielding_of_split(self) -> pd.DataFrame:
        """Get core/FieldingOFsplit data."""
        return self._get_csv("core/FieldingOFsplit.csv")

    def fielding_post(self) -> pd.DataFrame:
        """Get core/FieldingPost data."""
        return self._get_csv("core/FieldingPost.csv")

    def home_games(self) -> pd.DataFrame:
        """Get core/HomeGames data."""
        return self._get_csv("core/HomeGames.csv")

    def managers(self) -> pd.DataFrame:
        """Get core/Managers data."""
        return self._get_csv("core/Managers.csv")

    def managers_half(self) -> pd.DataFrame:
        """Get core/ManagersHalf data."""
        return self._get_csv("core/ManagersHalf.csv")

    def parks(self) -> pd.DataFrame:
        """Get core/Parks data."""
        return self._get_csv("core/Parks.csv")

    def people(self) -> pd.DataFrame:
        """Get core/People data."""
        return self._get_csv("core/People.csv")

    def pitching(self) -> pd.DataFrame:
        """Get core/Pitching data."""
        return self._get_csv("core/Pitching.csv")

    def pitching_post(self) -> pd.DataFrame:
        """Get core/PitchingPost data."""
        return self._get_csv("core/PitchingPost.csv")

    def series_post(self) -> pd.DataFrame:
        """Get core/SeriesPost data."""
        return self._get_csv("core/SeriesPost.csv")

    def teams(self) -> pd.DataFrame:
        """Get core/Teams data."""
        return self._get_csv("core/Teams.csv")

    def teams_franchises(self) -> pd.DataFrame:
        """Get core/TeamsFranchises data."""
        return self._get_csv("core/TeamsFranchises.csv")

    def teams_half(self) -> pd.DataFrame:
        """Get core/TeamsHalf data."""
        return self._get_csv("core/TeamsHalf.csv")
