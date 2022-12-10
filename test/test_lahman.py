from lahman import LahmanData
from unittest import mock
from os import path


def test_all_star_full():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.all_star_full()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "AllstarFull.csv"))
    )


def test_appearances():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.appearances()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "Appearances.csv"))
    )


def test_batting():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.batting()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "Batting.csv"))
    )


def test_batting_post():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.batting_post()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "BattingPost.csv"))
    )

def test_fielding():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.fielding()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "Fielding.csv"))
    )

def test_fielding_of():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.fielding_of()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "FieldingOF.csv"))
    )

def test_fielding_of_split():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.fielding_of_split()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "FieldingOFsplit.csv"))
    )

def test_fielding_post():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.fielding_post()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "FieldingPost.csv"))
    )

def test_home_games():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.home_games()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "HomeGames.csv"))
    )

def test_managers():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.managers()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "Managers.csv"))
    )

def test_managers_half():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.managers_half()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "ManagersHalf.csv"))
    )

def test_parks():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.parks()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "Parks.csv"))
    )

def test_people():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.people()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "People.csv"))
    )

def test_pitching():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.pitching()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "Pitching.csv"))
    )

def test_pitching_post():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.pitching_post()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "PitchingPost.csv"))
    )

def test_series_post():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.series_post()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "SeriesPost.csv"))
    )

def test_teams():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.teams()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "Teams.csv"))
    )

def test_teams_franchises():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.teams_franchises()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "TeamsFranchises.csv"))
    )

def test_teams_half():
    mock_reader = mock.Mock()
    mock_reader.read_csv = mock.Mock()
    db = LahmanData(download=False, csv_reader=mock_reader)
    db.teams_half()
    mock_reader.read_csv.assert_called_once_with(
        path.abspath(path.join(db._folder_path, "core", "TeamsHalf.csv"))
    )
