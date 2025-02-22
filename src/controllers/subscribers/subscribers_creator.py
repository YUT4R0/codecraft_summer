from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface


class SubscribersCreator:
    def __init__(self, subs_repo: SubscribersRepositoryInterface):
        self.__subs_repo = subs_repo

    def create(self, http_request: HttpRequest) -> HttpResponse:
        subscriber_info = http_request.body["data"]
        email = subscriber_info["email"]
        event_id = subscriber_info["event_id"]
        self.__check_subscriber(email, event_id)
        self.__insert_subscriber(subscriber_info)
        return self.__format_response(subscriber_info)

    def __check_subscriber(self, email: str, event_id: str) -> None:
        res = self.__subs_repo.select_subscriber(email, event_id)
        if res:
            raise Exception(f"subscriber with email '{email}' already exists!")

    def __insert_subscriber(self, subscriber_info: dict) -> None:
        self.__subs_repo.insert(subscriber_info)

    def __format_response(self, subscriber_info: dict) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "Type": "subscriber",
                    "count": 1,
                    "attributes": subscriber_info
                }
            },
            status_code=201
        )
