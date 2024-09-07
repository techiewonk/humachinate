import pytest
from humachinate.src.standalone import Humachinate, ClickType


@pytest.fixture
def humachinate():
    """Fixture to create a Humachinate instance for each test."""
    return Humachinate()


def test_find_elements(humachinate):
    """Test the find_elements method with a known image on the screen."""
    # This test needs an actual image path and correct screen setup
    results = humachinate.find_elements(image_path="path_to_test_image.png")
    assert len(results) > 0  # Adjust based on what you expect


def test_move_to(humachinate):
    """Test moving to a specific screen location."""
    # Test this function possibly with a predefined element center
    humachinate.move_to({'x': 100, 'y': 100})
    # Actual movement needs manual verification or screen capture analysis


def test_click_at(humachinate):
    """Test clicking functionality."""
    # This may need manual verification unless automated screen interaction verification is set up
    humachinate.click_at({'x': 100, 'y': 100}, ClickType.LEFT)


def test_type_at(humachinate):
    """Test typing at a specific location."""
    humachinate.type_at({'x': 100, 'y': 100}, "Hello, world!", 280, 20, ClickType.LEFT)
    # Manual verification or using an application to receive input


def test_not_implemented(humachinate):
    """Ensure that not implemented methods raise the correct error."""
    with pytest.raises(NotImplementedError):
        humachinate.scroll_to({'x': 100, 'y': 100})
