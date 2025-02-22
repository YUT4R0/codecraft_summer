from src.model.entities.subscribers import Subscribers
from src.model.configs.connection import DBConnectionHanlder
from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface


class SubscribersRepository(SubscribersRepositoryInterface):
    def insert(self, subscriber_data: dict) -> None:
        with DBConnectionHanlder() as db:
            try:
                new_subscriber = Subscribers(
                    userName=subscriber_data.get('userName'),
                    email=subscriber_data.get('email'),
                    link=subscriber_data.get('link'),
                    event_id=subscriber_data.get('event_id')
                )
                db.session.add(new_subscriber)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_subscriber(self, email: str, event_id: int) -> Subscribers:
        with DBConnectionHanlder() as db:
            data = (
                db.session
                .query(Subscribers)
                .filter(Subscribers.email == email, Subscribers.event_id == event_id)
                .one_or_none()
            )
            return data
