from tkinter import CENTER, FLAT

import pytest

from src.ui.styles import Styles


@pytest.mark.unit
class TestStyles:
    def test_primary_color_is_correct(self) -> None:
        assert Styles.PRIMARY_COLOR == "#20063B"

    def test_white_color_is_correct(self) -> None:
        assert Styles.WHITE_COLOR == "#FFFFFF"

    def test_black_color_is_correct(self) -> None:
        assert Styles.BLACK_COLOR == "#000000"

    def test_font_times_base_is_times(self) -> None:
        assert Styles.FONT_TIMES == "Times"

    def test_font_times_12_contains_size(self) -> None:
        assert "12" in Styles.FONT_TIMES_12

    def test_font_times_13_contains_size(self) -> None:
        assert "13" in Styles.FONT_TIMES_13

    def test_font_times_14_contains_size(self) -> None:
        assert "14" in Styles.FONT_TIMES_14

    def test_font_times_15_contains_size(self) -> None:
        assert "15" in Styles.FONT_TIMES_15

    def test_font_times_20_contains_size(self) -> None:
        assert "20" in Styles.FONT_TIMES_20

    def test_center_matches_tkinter_constant(self) -> None:
        assert Styles.CENTER == CENTER

    def test_anchor_center_matches_center(self) -> None:
        assert Styles.ANCHOR_CENTER == CENTER

    def test_relief_flat_matches_tkinter_constant(self) -> None:
        assert Styles.RELIEF_FLAT == FLAT
