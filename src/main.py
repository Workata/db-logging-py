from db import BaseModel, engine
from logs import DatabaseHandler
import logging


BaseModel.metadata.create_all(bind=engine)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.DEBUG
)

logger = logging.getLogger("general")
handler = DatabaseHandler()
logger.addHandler(handler)

logger.info("log something")

