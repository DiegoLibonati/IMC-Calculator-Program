import logging

from src.models.InterfaceApp import InterfaceApp
from src.utils.constants import PRIMARY
from src.utils.constants import ERROR_MESSAGE_INVALID_VALUES


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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


def test_calculate_imc(interface_app: InterfaceApp) -> None:
    weight = 90
    height = 185

    interface_app.entry_weight.set(weight)
    interface_app.entry_height.set(height)

    interface_app.calculate_imc()

    assert interface_app.entry_result.get() == "26.3"
    assert interface_app.label_result.get() == "You are overweight."


def test_calculate_imc_invalid_values(interface_app: InterfaceApp) -> None:
    weight = "asd"
    height = 185

    interface_app.entry_weight.set(weight)
    interface_app.entry_height.set(height)

    interface_app.calculate_imc()

    assert interface_app.label_result.get() == ERROR_MESSAGE_INVALID_VALUES


def test_range_result(interface_app: InterfaceApp) -> None:
    interface_app.range_result(result=18)

    assert interface_app.label_result.get() == "You are thin."

    interface_app.range_result(result=25)

    assert interface_app.label_result.get() == "You have a normal weight."
    
    interface_app.range_result(result=27)

    assert interface_app.label_result.get() == "You are overweight."

    interface_app.range_result(result=31)

    assert interface_app.label_result.get() == "Obesity status."