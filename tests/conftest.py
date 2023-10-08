"""Configure pytest for the tests in this directory."""
from pathlib import Path

import pytest

from simple_toml_settings.settings import TOMLSettings


class TestSettings(TOMLSettings):
    """Define a class for testing the Settings class."""

    test_string_var: str = "test_value"
    test_int_var: int = 42


@pytest.fixture()
def settings(fs):
    """Return a Settings object for testing.

    This fixture creates a fake home directory in a virtual filesystem. It then
    creates a Settings object for the test and returns it. This Settings object
    creates a settings file in the fake home directory.
    """
    # Create a fake home directory for the test
    fs.create_dir(Path.home())

    # Create a Settings object for the test
    settings = TestSettings("test_app")

    return settings
