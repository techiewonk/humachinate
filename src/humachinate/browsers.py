import asyncio
import random
import logging
from .base import HumachinateBase, ClickType

# Set up logging
logger = logging.getLogger(__name__)


class HumachinateSelenium(HumachinateBase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    async def _get_browser_properties_if_not_found(self):
        await super()._get_browser_properties_if_not_found(self.driver.save_screenshot)

    def get_center(self, element):
        """Calculate center of an element in Selenium."""
        asyncio.run(self._get_browser_properties_if_not_found())
        element_location = element.location
        element_size = element.size
        return self._get_center(element_location, element_size)

    def move_to(self, element, offset_x=random.uniform(0.0, 1.5), offset_y=random.uniform(0.0, 1.5)):
        """Move cursor to an element with random offset adjustments."""
        center = self.get_center(element)
        self._move(center, offset_x, offset_y)

    def click_at(self, element, click_type=ClickType.LEFT):
        """Click at the center of an element."""
        center = self.get_center(element)
        self._move(center)
        self._click(click_type)

    def type_at(self, element, text, characters_per_minute=280, offset=20, click_type=ClickType.LEFT):
        """Type text at the element location."""
        center = self.get_center(element)
        self._move(center)
        self._click(click_type)
        self.silent_type(text, characters_per_minute, offset)

    def scroll_to(self, element):
        """Scroll smoothly to an element."""
        asyncio.run(self._get_browser_properties_if_not_found())
        element_rect = element.rect
        self._scroll_smoothly_to_element(element_rect)


class HumachinatePuppeteer(HumachinateBase):
    def __init__(self, page):
        super().__init__()
        self.page = page

    async def _get_browser_properties_if_not_found(self):
        """Retrieve browser properties asynchronously using Puppeteer's screenshot capabilities."""
        async def screenshot_func(path):
            await self.page.screenshot(path=path)
        await super()._get_browser_properties_if_not_found(screenshot_func)

    async def get_center(self, element):
        """Calculate center of an element using its bounding box in Puppeteer."""
        await self._get_browser_properties_if_not_found()
        rect = await element.boundingBox()
        if rect is None:
            logger.warning("Bounding box not found for element.")
            return None
        return self._get_center(rect, rect)

    async def move_to(self, element, offset_x=random.uniform(0.0, 1.5), offset_y=random.uniform(0.0, 1.5)):
        """Asynchronously move to an element with random offsets."""
        center = await self.get_center(element)
        self._move(center, offset_x, offset_y)

    async def click_at(self, element, click_type=ClickType.LEFT):
        """Asynchronously click at an element's center."""
        center = await self.get_center(element)
        self._move(center)
        self._click(click_type)

    async def type_at(self, element, text, characters_per_minute=280, offset=20, click_type=ClickType.LEFT):
        """Asynchronously type text at an element's location."""
        center = await self.get_center(element)
        self._move(center)
        self._click(click_type)
        self.silent_type(text, characters_per_minute, offset)

    async def scroll_to(self, element):
        """Asynchronously scroll to an element's location."""
        await self._get_browser_properties_if_not_found()
        element_rect = await element.boundingBox()
        if element_rect is None:
            logger.warning("Bounding box not found for scrolling.")
            return None
        self._scroll_smoothly_to_element(element_rect)


class HumachinatePlaywright(HumachinateBase):
    def __init__(self, page):
        super().__init__()
        self.page = page

    async def _get_browser_properties_if_not_found(self):
        """Retrieve browser properties asynchronously using Playwright's screenshot capabilities with clipping."""
        async def screenshot_func(path):
            viewport_size = self.page.viewport_size
            clip = {
                'x': 0, 'y': 0, 'width': viewport_size['width'] // 2, 'height': viewport_size['height'] // 2}
            await self.page.screenshot(path=path, clip=clip)
        await super()._get_browser_properties_if_not_found(screenshot_func)

    async def get_center(self, element):
        """Calculate center of an element using its bounding box in Playwright."""
        await self._get_browser_properties_if_not_found()
        rect = await element.bounding_box()
        if rect is None:
            logger.warning("Bounding box not found for element.")
            return None
        return self._get_center(rect, rect)

    async def move_to(self, element, offset_x=random.uniform(0.0, 1.5), offset_y=random.uniform(0.0, 1.5)):
        """Asynchronously move to an element with random offsets."""
        center = await self.get_center(element)
        self._move(center, offset_x, offset_y)

    async def click_at(self, element, click_type=ClickType.LEFT):
        """Asynchronously click at an element's center."""
        center = await self.get_center(element)
        self._move(center)
        self._click(click_type)

    async def type_at(self, element, text, characters_per_minute=280, offset=20, click_type=ClickType.LEFT):
        """Asynchronously type text at an element's location."""
        center = await self.get_center(element)
        self._move(center)
        self._click(click_type)
        self.silent_type(text, characters_per_minute, offset)

    async def scroll_to(self, element):
        """Asynchronously scroll to an element's location."""
        await self._get_browser_properties_if_not_found()
        element_rect = await element.bounding_box()
        if element_rect is None:
            logger.warning("Bounding box not found for scrolling.")
            return None
        self._scroll_smoothly_to_element(element_rect)
