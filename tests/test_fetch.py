import pytest
from sqlmodel import Session, select
from datetime import datetime
from gymtime.functions.fetch import fetch_records, fetch_average_for_time
from gymtime.database.db import engine
from gymtime.database.models import Gym, Section


@pytest.fixture
def marino_track() -> Section:
    with Session(engine) as session:
        marino = session.exec(select(Gym).where(Gym.slug == "marino")).one()
        track_section = session.exec(
            select(Section)
            .where(Section.gym_id == marino.id)
            .where(Section.slug == "track")
        ).one()
        return track_section


def test_init(marino_track: Section):
    assert marino_track.gym_id == 1
    assert marino_track.slug == "track"
    assert marino_track.name == "Track"


def test_fetch_records(marino_track: Section):
    records_day1 = fetch_records(
        section_id=marino_track.id,
        from_date=datetime(year=2023, month=1, day=1),
        to_date=datetime(year=2023, month=1, day=1),
    )

    assert records_day1[0].count == 6
    assert records_day1[1].count == 7

    records_day2 = fetch_records(
        section_id=marino_track.id,
        from_date=datetime(year=2023, month=1, day=2),
        to_date=datetime(year=2023, month=1, day=2),
    )

    assert records_day2[0].count == 3
    assert records_day2[1].count == 10


def test_fetch_average_for_time(marino_track: Section):
    average_sunday_0500 = fetch_average_for_time(
        section_id=marino_track.id,
        day_of_week=0,  # sunday
        hour=5,
        days_back=7,
    )
    assert average_sunday_0500 == pytest.approx(5.75)

    average_sunday_0600 = fetch_average_for_time(
        section_id=marino_track.id,
        day_of_week=0,  # sunday
        hour=6,
        days_back=7,
    )
    assert average_sunday_0600 == pytest.approx(5)

    average_monday_0600 = fetch_average_for_time(
        section_id=marino_track.id,
        day_of_week=1,  # monday
        hour=5,
        days_back=7,
    )
    assert average_monday_0600 == pytest.approx(7.5)
