from logging import Handler, LogRecord, NOTSET
from models import Log
from db import get_db


class DatabaseHandler(Handler):

    # def __init__(self, level=NOTSET) -> None:
    #     super().__init__(level)
    #     self._db = get_db()

    def emit(self, record: LogRecord) -> None:
        msg = self.format(record)
        log = Log(
            message=msg,
            priority=record.levelname,
        )
        db = get_db()
        with db as db:
            db.add(log)
            db.commit()
