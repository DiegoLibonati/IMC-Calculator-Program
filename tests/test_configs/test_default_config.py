from src.configs.default_config import DefaultConfig


class TestDefaultConfig:
    def test_debug_is_false(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.DEBUG is False

    def test_testing_is_false(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.TESTING is False

    def test_tz_default(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.TZ == "America/Argentina/Buenos_Aires"

    def test_env_name_default(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.ENV_NAME == "template tkinter python"

    def test_tz_is_string(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert isinstance(config.TZ, str)

    def test_env_name_is_string(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert isinstance(config.ENV_NAME, str)
