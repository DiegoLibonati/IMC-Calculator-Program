import logging

from src.ui.interface_app import InterfaceApp
from src.utils.messages import MESSAGE_ERROR_INVALID_VALUES, MESSAGE_OVERWEIGHT
from src.utils.styles import PRIMARY

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

CUSTOM_BG = "" or PRIMARY


def test_initial_config_tk_app(interface_app: InterfaceApp) -> None:
    root = interface_app.root
    root.update()

    title = root.title()
    geometry = root.geometry().split("+")[0]
    resizable = root.resizable()
    config_bg = root.cget("bg")

    assert title == "IMC Calculator"
    assert geometry == "600x300"
    assert resizable == (False, False)
    assert config_bg == CUSTOM_BG


def test_calculate_and_update(interface_app: InterfaceApp) -> None:
    weight = 90
    height = 185

    interface_app.entry_weight.set(str(weight))
    interface_app.entry_height.set(str(height))

    interface_app._calculate_and_update()

    assert interface_app.entry_result.get() == "26.3"
    assert interface_app.label_result.get() == MESSAGE_OVERWEIGHT


def test_calculate_and_update_invalid_values(interface_app: InterfaceApp) -> None:
    interface_app.entry_weight.set("asd")
    interface_app.entry_height.set("185")

    interface_app._calculate_and_update()

    assert interface_app.label_result.get() == MESSAGE_ERROR_INVALID_VALUES
