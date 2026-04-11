from tkinter import CENTER, FLAT

from src.ui.styles import Styles


class TestStyles:
    def test_primary_color(self) -> None:
        assert Styles.PRIMARY_COLOR == "#20063B"

    def test_white_color(self) -> None:
        assert Styles.WHITE_COLOR == "#FFFFFF"

    def test_black_color(self) -> None:
        assert Styles.BLACK_COLOR == "#000000"

    def test_font_times(self) -> None:
        assert Styles.FONT_TIMES == "Times"

    def test_font_times_12(self) -> None:
        assert Styles.FONT_TIMES_12 == "Times 12"

    def test_font_times_13(self) -> None:
        assert Styles.FONT_TIMES_13 == "Times 13"

    def test_font_times_14(self) -> None:
        assert Styles.FONT_TIMES_14 == "Times 14"

    def test_font_times_15(self) -> None:
        assert Styles.FONT_TIMES_15 == "Times 15"

    def test_font_times_20(self) -> None:
        assert Styles.FONT_TIMES_20 == "Times 20"

    def test_center(self) -> None:
        assert Styles.CENTER == CENTER

    def test_anchor_center(self) -> None:
        assert Styles.ANCHOR_CENTER == CENTER

    def test_relief_flat(self) -> None:
        assert Styles.RELIEF_FLAT == FLAT

    def test_instantiation(self) -> None:
        styles: Styles = Styles()
        assert styles is not None
