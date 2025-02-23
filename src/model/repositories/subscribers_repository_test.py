from .subscribers_repository import SubscribersRepository
import pytest


@pytest.mark.skip("Insert in DB")
def test_insert():
    sub_data = {
        "userName": "kenedy",
        "email": "kenedy@gmail.com",
        "event_id": 4
    }
    sub_repo = SubscribersRepository()
    sub_repo.insert(subscriber_data=sub_data)


@pytest.mark.skip("Select in DB")
def test_select_subscriber():
    email = "kenedy@gmail.com"
    event_id = 4
    sub_repo = SubscribersRepository()
    data = sub_repo.select_subscriber(email, event_id)
    print(data.userName)


@pytest.mark.skip("Select ranking in DB")
def test_ranking():
    event_id = 4
    sub_repo = SubscribersRepository()
    res = sub_repo.get_ranking(event_id)

    for item in res:
        print(f"\nlink: {item.link}, total: {item.total}")
