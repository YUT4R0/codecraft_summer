import random

from src.model.entities.events_link import EventsLink
from src.model.configs.connection import DBConnectionHanlder
from .interfaces.events_link_repository import EventsLinkrepositoryInterface


class EventsLinkRepository(EventsLinkrepositoryInterface):
    def insert(self, event_id: int, subs_id: int) -> str:
        with DBConnectionHanlder() as db:
            try:
                link_final = "".join(random.choices("0123456789", k=7))
                formated_link = f"event-{event_id}-subs-{subs_id}-{link_final}"

                new_events_link = EventsLink(
                    event_id,
                    subs_id,
                    formated_link
                )
                db.session.add(new_events_link)
                db.session.commit()

                return formated_link
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_events_link(self, event_id: int, subs_id: int) -> EventsLink:
        with DBConnectionHanlder() as db:
            data = (
                db.session
                .query(EventsLink)
                .filter(
                    EventsLink.id == event_id,
                    EventsLink.subscriber_id == subs_id,
                )
                .one_or_none()
            )
            return data
