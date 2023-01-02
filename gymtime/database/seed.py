from .models import Gym, Section, Record
from .db import engine
from sqlmodel import Session, select
from datetime import datetime


def main():
    with Session(engine) as session:
        # Drop all (there's probably a better way to do this)
        for record in session.exec(select(Record)).all():
            session.delete(record)
        for section in session.exec(select(Section)).all():
            session.delete(section)
        for gym in session.exec(select(Gym)).all():
            session.delete(gym)
        session.commit()

        marino = Gym(slug="marino", name="Marino Center", short_name="Marino")
        squash = Gym(
            slug="squashbusters", name="Squasbusters Center", short_name="Squash"
        )
        session.add(marino)
        session.add(squash)
        session.commit()

        marino_weight_room = Section(
            slug="weight-room",
            name="Weight Room",
            short_name="weight",
            gym_id=marino.id,
        )
        marino_track = Section(
            slug="track",
            name="Track",
            short_name="track",
            gym_id=marino.id,
        )
        session.add(marino_weight_room)
        session.add(marino_track)

        squash_floor_four = Section(
            slug="floor-four",
            name="Flour Four",
            short_name="four",
            gym_id=squash.id,
        )
        session.add(squash_floor_four)
        session.commit()

        # Sample records
        marino_track_day1_0500 = Record(
            time=datetime(year=2023, month=1, day=1, hour=5, minute=0),
            count=6,
            section_id=marino_track.id,
        )
        marino_track_day1_0530 = Record(
            time=datetime(year=2023, month=1, day=1, hour=5, minute=30),
            count=7,
            section_id=marino_track.id,
        )
        marino_track_day1_0600 = Record(
            time=datetime(year=2023, month=1, day=1, hour=6, minute=0),
            count=6,
            section_id=marino_track.id,
        )
        marino_track_day1_0630 = Record(
            time=datetime(year=2023, month=1, day=1, hour=6, minute=30),
            count=3,
            section_id=marino_track.id,
        )
        marino_track_day1_0700 = Record(
            time=datetime(year=2023, month=1, day=1, hour=7, minute=0),
            count=2,
            section_id=marino_track.id,
        )

        marino_track_day2_0500 = Record(
            time=datetime(year=2023, month=1, day=2, hour=5, minute=0),
            count=3,
            section_id=marino_track.id,
        )
        marino_track_day2_0530 = Record(
            time=datetime(year=2023, month=1, day=2, hour=5, minute=30),
            count=10,
            section_id=marino_track.id,
        )
        marino_track_day2_0600 = Record(
            time=datetime(year=2023, month=1, day=2, hour=6, minute=0),
            count=16,
            section_id=marino_track.id,
        )
        marino_track_day2_0630 = Record(
            time=datetime(year=2023, month=1, day=2, hour=6, minute=30),
            count=13,
            section_id=marino_track.id,
        )
        marino_track_day2_0700 = Record(
            time=datetime(year=2023, month=1, day=2, hour=7, minute=0),
            count=5,
            section_id=marino_track.id,
        )
        session.add(marino_track_day1_0500)
        session.add(marino_track_day1_0530)
        session.add(marino_track_day1_0600)
        session.add(marino_track_day1_0630)
        session.add(marino_track_day1_0700)
        session.add(marino_track_day2_0500)
        session.add(marino_track_day2_0530)
        session.add(marino_track_day2_0600)
        session.add(marino_track_day2_0630)
        session.add(marino_track_day2_0700)
        session.commit()
