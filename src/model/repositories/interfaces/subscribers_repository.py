from src.model.entities.subscribers import Subscribers
from abc import ABC, abstractmethod


class SubscribersRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, subscriber_data: dict) -> None: pass
    @abstractmethod
    def select_subscriber(self, email: str, event_id: int) -> Subscribers: pass
