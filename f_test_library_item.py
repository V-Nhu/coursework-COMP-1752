import pytest
from library_item import LibraryItem

def test_library_item_creation():
    item = LibraryItem("Test Song", "Test Artist", 3)
    assert item.name == "Test Song"
    assert item.artist == "Test Artist"
    assert item.rating == 3
    assert item.play_count == 0

def test_info_and_stars():
    item = LibraryItem("Test Song", "Test Artist", 4)
    assert item.stars() == "****"
    assert item.info() == "Test Song - Test Artist ****"

def test_increment_play_count():
    item = LibraryItem("Song", "Artist")
    assert item.play_count == 0
    item.play_count += 1
    assert item.play_count == 1
    item.play_count += 1
    assert item.play_count == 2

def test_rating_update():
    item = LibraryItem("X", "Y", 1)
    item.rating = 5
    assert item.rating == 5

def test_default_rating():
    item = LibraryItem("Z", "W")
    assert item.rating == 0
