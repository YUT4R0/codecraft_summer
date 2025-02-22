import pytest
from .events_repository import EventsRepository


@pytest.mark.skip("Insert in db")
def test_insert_events():
    event_name = "evento legal test"
    event_repo = EventsRepository()
    event_repo.insert(event_name)


@pytest.mark.skip("Select in db")
def test_get_event():
    event_name = "evento legal test"
    event_repo = EventsRepository()
    event = event_repo.select_event(event_name)

    print(event)
    print(event.eventName)
