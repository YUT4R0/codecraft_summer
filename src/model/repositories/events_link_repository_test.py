import pytest

from src.model.repositories.events_link_repository import EventsLinkRepository


@pytest.mark.skip.name("Insert in db")
def test_insert_event_link():
    event_id = 12
    subs_id = 18
    events_link_repo = EventsLinkRepository()

    events_link_repo.insert(event_id, subs_id)


def test_select_event_link():
    event_id = 12
    subs_id = 18
    events_link_repo = EventsLinkRepository()
    events_link_repo.select_events_link(event_id, subs_id)
