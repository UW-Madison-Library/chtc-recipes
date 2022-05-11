import logging
from datetime import datetime


def configure(cluster_id, process_id):
    timestamp      = datetime.now().strftime('%Y%m%dT%H%M%S.%f')
    log_format     = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logger_handler = logging.FileHandler('wos-explorer-' + cluster_id + '-' + process_id + '-' + timestamp + '.log')
    logger_handler.setFormatter( logging.Formatter(log_format) )

    logger = logging.getLogger("wos_explorer")
    logger.addHandler(logger_handler)
    logger.setLevel(logging.DEBUG)
