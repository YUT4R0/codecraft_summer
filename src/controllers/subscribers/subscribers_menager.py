from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface


class SubscribersManager:
    def __init__(self, subscribers_repo: SubscribersRepositoryInterface):
        self.__subscribers_repo = subscribers_repo

    def get_subscribers_by_link(self, http_request: HttpRequest) -> HttpResponse:
        link = http_request.param["link"]
        event_id = http_request.param["event_id"]
        subs = self.__subscribers_repo.select_subscribers_by_link(
            link, event_id)
        return self.__format_subs_by_link(subs)

    def get_event_ranking(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        event_ranking = self.__subscribers_repo.get_ranking(event_id)
        return self.__format_event_ranking(event_ranking)

    def __format_subs_by_link(self, subs: list) -> HttpResponse:
        formated_subscriber = []
        for sub in subs:
            formated_subscriber.append(
                {
                    "userName": sub.name,
                    "email": sub.email
                }
            )
        return HttpResponse(
            body={
                "data": {
                    "Type": "subscriber",
                    "count": len(formated_subscriber),
                    "subscribers": formated_subscriber
                }
            },
            status_code=201
        )

    def __format_event_ranking(self, event_ranking: list) -> HttpResponse:
        formated_event_ranking = []
        for pos in event_ranking:
            formated_event_ranking.append(
                {
                    "link": pos.link,
                    "total_subscribers": pos.total
                }
            )
        return HttpResponse(
            body={
                "data": {
                    "Type": "ranking",
                    "count": len(formated_event_ranking),
                    "ranking": formated_event_ranking
                }
            },
            status_code=201
        )
