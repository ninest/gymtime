from gymtime.util.round_time import round_hour
from datetime import datetime


def create_dt(hour, minute, second) -> datetime:
    return datetime(
        year=2023,
        month=1,
        day=1,
        hour=hour,
        minute=minute,
        second=second,
        microsecond=0,
    )


def test_round_time():
    noon = create_dt(12, 0, 0)
    assert round_hour(noon) == noon

    half_noon = create_dt(12, 29, 1)
    assert round_hour(half_noon) == noon

    half_noon_one = create_dt(12, 31, 1)
    assert round_hour(half_noon_one) == create_dt(12, 30, 0)

    almost_one = create_dt(12, 51, 34)
    assert round_hour(almost_one) == create_dt(12, 30, 0)

    almost_tomorrow = create_dt(23, 59, 59)
    assert round_hour(almost_tomorrow) == datetime(
        year=2023,
        month=1,
        day=1,
        hour=23,
        minute=30,
        second=0,
        microsecond=0,
    )
