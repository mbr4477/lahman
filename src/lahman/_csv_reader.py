from abc import ABC, abstractmethod
import pandas as pd


class CSVReader(ABC):
    """A generic CSV reader."""

    @abstractmethod
    def read_csv(self, path: str) -> pd.DataFrame:
        """Read a CSV file and return a Pandas DataFrame."""
        pass


class PandasCSVReader(CSVReader):
    """A CSV reader implemented with Pandas."""

    def read_csv(self, path: str) -> pd.DataFrame:
        return pd.read_csv(path)
