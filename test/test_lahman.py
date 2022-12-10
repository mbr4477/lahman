from lahman import LahmanData
from lahman._locator import LahmanLocator
from unittest import mock
from os import path
import pytest


class MockLocator(LahmanLocator):
    def locate(self, root_dir: str) -> str:
        return path.abspath(path.join(root_dir, "baseballdatabank-2022.2"))


def test_all_star_full():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.all_star_full()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "AllstarFull.csv"))
    )


def test_appearances():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.appearances()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "Appearances.csv"))
    )


def test_batting():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.batting()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "Batting.csv"))
    )


def test_batting_post():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.batting_post()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "BattingPost.csv"))
    )


def test_fielding():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.fielding()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "Fielding.csv"))
    )


def test_fielding_of():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.fielding_of()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "FieldingOF.csv"))
    )


def test_fielding_of_split():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.fielding_of_split()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "FieldingOFsplit.csv"))
    )


def test_fielding_post():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.fielding_post()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "FieldingPost.csv"))
    )


def test_home_games():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.home_games()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "HomeGames.csv"))
    )


def test_managers():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.managers()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "Managers.csv"))
    )


def test_managers_half():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.managers_half()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "ManagersHalf.csv"))
    )


def test_parks():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.parks()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "Parks.csv"))
    )


def test_people():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.people()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "People.csv"))
    )


def test_pitching():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.pitching()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "Pitching.csv"))
    )


def test_pitching_post():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.pitching_post()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "PitchingPost.csv"))
    )


def test_series_post():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.series_post()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "SeriesPost.csv"))
    )


def test_teams():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.teams()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "Teams.csv"))
    )


def test_teams_franchises():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.teams_franchises()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "TeamsFranchises.csv"))
    )


def test_teams_half():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader, locator=MockLocator())
    db.teams_half()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "TeamsHalf.csv"))
    )
