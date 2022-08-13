import logging
import logging.config

import yaml

config = yaml.safe_load(open("./config/logging.yml"))
logging.config.dictConfig(config)
