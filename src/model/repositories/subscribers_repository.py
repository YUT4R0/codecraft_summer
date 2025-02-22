from sqlalchemy import func, desc

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

    def select_subscribers_by_link(self, link: str, event_id: int) -> list:
        with DBConnectionHanlder() as db:
            data = (
                db.session
                .query(Subscribers)
                .filter(Subscribers.link == link, Subscribers.event_id == event_id)
                .all()
            )
            return data

    def get_ranking(self, event_id: int) -> tuple:
        with DBConnectionHanlder() as db:
            result = (
                db.session
                .query(
                    Subscribers.link,
                    func.count(Subscribers.id).label("total")
                )
                .filter(
                    Subscribers.event_id == event_id,
                    Subscribers.link.isnot(None)
                )
                .group_by(Subscribers.link)
                .order_by(desc("total"))
                .all()
            )

            return result
