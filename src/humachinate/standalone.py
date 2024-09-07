import random
import logging
import pyautogui
from .base import HumachinateBase, ClickType

# Set up logging
logger = logging.getLogger(__name__)


class Humachinate(HumachinateBase):
    """Class for interacting with elements on the screen using pyautogui."""

    def __init__(self):
        super().__init__()

    def find_elements(self, image_path=None, min_confidence=0.8, target_height=None, target_width=None, max_elements=0):
        """Find screen elements that match a given image path with optional size filtering.

        Args:
            image_path (str): Path to the image file to locate on the screen.
            min_confidence (float): Minimum confidence level for the match.
            target_height (int): Optional target height to filter matches.
            target_width (int): Optional target width to filter matches.
            max_elements (int): Maximum number of elements to return.

        Returns:
            list of dict: A list of coordinates {'x': int, 'y': int} for each found element.
        """
        filtered = []
        try:
            elements = pyautogui.locateAllOnScreen(
                image_path, confidence=min_confidence)
            if target_height is not None and target_width is not None:
                epsilon = 1.0 - min_confidence
                min_height = round(target_height - target_height * epsilon)
                max_height = round(target_height + target_height * epsilon)
                min_width = round(target_width - target_width * epsilon)
                max_width = round(target_width + target_width * epsilon)

                for element in elements:
                    _, _, width, height = element
                    if min_height <= height <= max_height and min_width <= width <= max_width:
                        center_x, center_y = pyautogui.center(element)
                        if not any(abs(e['y'] - center_y) <= max_height for e in filtered):
                            filtered.append({'x': center_x, 'y': center_y})
                            if max_elements and len(filtered) >= max_elements:
                                break
            else:
                for element in elements:
                    center_x, center_y = pyautogui.center(element)
                    filtered.append({'x': center_x, 'y': center_y})
        except Exception as e:
            logger.error(f"Error finding elements on screen: {e}")

        if max_elements:
            return filtered[:max_elements]
        return filtered

    def move_to(self, element_center, offset_x=random.uniform(0.0, 1.5), offset_y=random.uniform(0.0, 1.5)):
        """Move the cursor to the center of an element with optional random offsets."""
        self._move(element_center, offset_x, offset_y)

    def click_at(self, element_center, click_type=ClickType.LEFT):
        """Perform a click at the center of an element."""
        self._move(element_center)
        self._click(click_type)

    def type_at(self, element_center, text, characters_per_minute=280, offset=20, click_type=ClickType.LEFT):
        """Type text at the center of an element."""
        self._move(element_center)
        self._click(click_type)
        self.silent_type(text, characters_per_minute, offset)

    def scroll_to(self, element_center):
        """Scroll to an element center; not implemented in this class."""
        raise NotImplementedError(
            "Scroll functionality is not supported for the Humachinate class.")
