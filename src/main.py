import logging
import logging.config

from database import BaseModel, engine
from models import *  # noqa: F403
from settings import get_settings

settings = get_settings()
BaseModel.metadata.create_all(bind=engine)


logging.config.dictConfig(settings.logging)
logger = logging.getLogger("logger_name")

logger.info("dummy log")
