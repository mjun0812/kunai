import kunai
import logging

logger = logging.getLogger()

kunai.utils.setup_logger("./test.log")

logger.info("aaaa")
logger.error("bbbb")
