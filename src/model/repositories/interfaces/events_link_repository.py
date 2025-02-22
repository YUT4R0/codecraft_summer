from abc import ABC, abstractmethod

from src.model.entities.events_link import EventsLink


class EventsLinkrepositoryInterface(ABC):
    @abstractmethod
    def insert(self, event_id: int, subs_id: int) -> str: pass

    @abstractmethod
    def select_events_link(self, event_id: int,
                           subs_id: int) -> EventsLink: pass
