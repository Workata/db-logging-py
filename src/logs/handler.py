from logging import Handler, LogRecord
from models import Log
from database import Crud


class DatabaseHandler(Handler):
    def emit(self, record: LogRecord) -> None:
        msg = self.format(record)
        log = Log(
            message=msg,
            name=record.name,
            priority=record.levelname,
        )
        Crud.insert(log)
