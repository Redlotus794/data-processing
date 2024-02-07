"""
环境参数
"""
from dynaconf import Dynaconf


Settings = Dynaconf(
            environments=True,
            settings_files=['settings.toml']
        )

Settings.validators.validate()
print("settings loaded: ", Settings.ENV_NAME);
