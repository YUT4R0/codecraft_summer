from src.model.configs.connection import DBConnectionHanlder
from src.model.entities.events import Events


class EventsRepository:
    def insert(self, event_name: str) -> None:
        with DBConnectionHanlder() as db:
            try:
                new_event = Events(eventName=event_name)
                db.session.add(new_event)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_event(self, event_name) -> Events:
        with DBConnectionHanlder() as db:
            data = (
                db.session
                .query(Events)
                .where(Events.eventName == event_name)
                .one_or_none()
            )
            return data
