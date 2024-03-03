from . import get_db


class Crud:
    @classmethod
    def insert(cls, instance: object) -> None:
        with get_db() as db:
            db.add(instance)
            db.commit()
