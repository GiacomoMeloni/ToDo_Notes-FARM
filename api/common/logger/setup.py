import os
import yaml
import logging.config

from api.app.config import settings


def logger_setup(path: str = os.path.join(settings.ROOT_API_PATH, 'logging.yaml'),
                 default_level=logging.INFO):
    try:
        os.mkdir(os.path.join(settings.RESOURCE_PATH, 'logs'))
    except FileExistsError:
        pass

    if os.path.exists(path):
        with open(path, 'rt') as log_config_file:
            log_config = yaml.safe_load(log_config_file.read())
        logging.config.dictConfig(log_config)
    else:
        logging.basicConfig(level=default_level)
