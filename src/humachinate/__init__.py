import sys
import logging

from .base import ClickType
from .browsers import *
from .standalone import *

# Setup logging


def setup_logging(loglevel):
    """Setup basic logging.

    Configure the logging library to output messages with a severity level
    of `loglevel` or higher to the standard output stream.

    Args:
      loglevel (int): Minimum loglevel for emitting messages, typically
                      obtained from `logging.DEBUG`, `logging.INFO`, etc.
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    if not logging.root.handlers:  # Ensuring that root logger does not duplicate handlers
        logging.basicConfig(
            level=loglevel,
            stream=sys.stdout,
            format=logformat,
            datefmt="%Y-%m-%d %H:%M:%S"
        )


# Default logging setup
setup_logging(logging.INFO)

# Version handling
if sys.version_info[:2] >= (3, 11):
    # Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
