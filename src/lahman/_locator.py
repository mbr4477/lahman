from abc import ABC, abstractmethod
import glob
from typing import Optional
from os import path


class LahmanLocator(ABC):
    """A class to locate the Lahman database."""

    @abstractmethod
    def locate(self, root_dir: str) -> str:
        """Locate the Lahman database in root_dir.

        Args:
            root_dir: The root directory.

        Returns:
            The full path to the root Lahman folder.
        """
        pass


class GlobLocator(LahmanLocator):
    def locate(self, root_dir: str) -> Optional[str]:
        candidates = glob.glob(path.join(root_dir, "baseballdatabank-*"))
        return path.abspath(candidates[0]) if len(candidates) > 0 else None
