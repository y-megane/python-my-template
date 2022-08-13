import logging
import logging.config

import yaml  # type: ignore

config = yaml.safe_load(open("./config/logging.yml"))
logging.config.dictConfig(config)
