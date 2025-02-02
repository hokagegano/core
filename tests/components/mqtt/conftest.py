"""Test fixtures for mqtt component."""

from random import getrandbits
from unittest.mock import patch

import pytest
from typing_extensions import Generator

from homeassistant.components import mqtt

ENTRY_DEFAULT_BIRTH_MESSAGE = {
    mqtt.CONF_BROKER: "mock-broker",
    mqtt.CONF_BIRTH_MESSAGE: {
        mqtt.ATTR_TOPIC: "homeassistant/status",
        mqtt.ATTR_PAYLOAD: "online",
        mqtt.ATTR_QOS: 0,
        mqtt.ATTR_RETAIN: False,
    },
}


@pytest.fixture(autouse=True)
def patch_hass_config(mock_hass_config: None) -> None:
    """Patch configuration.yaml."""


@pytest.fixture
def temp_dir_prefix() -> str:
    """Set an alternate temp dir prefix."""
    return "test"


@pytest.fixture
def mock_temp_dir(temp_dir_prefix: str) -> Generator[str]:
    """Mock the certificate temp directory."""
    with patch(
        # Patch temp dir name to avoid tests fail running in parallel
        "homeassistant.components.mqtt.util.TEMP_DIR_NAME",
        f"home-assistant-mqtt-{temp_dir_prefix}-{getrandbits(10):03x}",
    ) as mocked_temp_dir:
        yield mocked_temp_dir
