import pytest

from src.model.repositories.events_link_repository import EventsLinkRepository


def test_insert_subscriber():
    event_id = 12
    subs_id = 18
    events_link_repo = EventsLinkRepository()

    events_link_repo.insert(event_id, subs_id)
