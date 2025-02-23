import random

from src.model.entities.events_link import EventsLink
from src.model.configs.connection import DBConnectionHanlder
from .interfaces.events_link_repository import EventsLinkrepositoryInterface


class EventsLinkRepository(EventsLinkrepositoryInterface):
    def insert(self, event_id: int, subscriber_id: int) -> str:
        with DBConnectionHanlder() as db:
            try:
                link_final = "".join(random.choices("0123456789", k=7))
                link = f"event-{event_id}-subs-{subscriber_id}-{link_final}"

                new_events_link = EventsLink(
                    link=link,
                    event_id=event_id,
                    subscriber_id=subscriber_id
                )
                db.session.add(new_events_link)
                db.session.commit()

                return link
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_events_link(self, event_id: int, subscriber_id: int) -> EventsLink:
        with DBConnectionHanlder() as db:
            data = (
                db.session
                .query(EventsLink)
                .filter(
                    EventsLink.id == event_id,
                    EventsLink.subscriber_id == subscriber_id,
                )
                .one_or_none()
            )
            return data
