from ._csv_reader import CSVReader, PandasCSVReader
from ._locator import LahmanLocator, GlobLocator
from ._downloader import LahmanDownloader, RequestsDownloader


class Injector:
    """A dependency injector."""

    @staticmethod
    def csv_reader() -> CSVReader:
        return PandasCSVReader()

    @staticmethod
    def locator() -> LahmanLocator:
        return GlobLocator()

    @staticmethod
    def downloader() -> LahmanDownloader:
        return RequestsDownloader()
