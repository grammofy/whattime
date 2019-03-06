from whattime import TimeType
from whattime import WeekInfo


def test_time_type_state_is_weekday(monday, tuesday, wednesday, thursday, friday, saturday, sunday):
    """ Test WeekInfo is_weekday of given datetime """

    assert WeekInfo(monday).is_weekday is True
    assert WeekInfo(tuesday).is_weekday is True
    assert WeekInfo(wednesday).is_weekday is True
    assert WeekInfo(thursday).is_weekday is True
    assert WeekInfo(friday).is_weekday is True
    assert WeekInfo(saturday).is_weekday is False
    assert WeekInfo(sunday).is_weekday is False


def test_time_type_state_is_weekend(monday, tuesday, wednesday, thursday, friday, saturday, sunday):
    """ Test WeekInfo is_weekday of given datetime """

    assert WeekInfo(monday).is_weekend is False
    assert WeekInfo(tuesday).is_weekend is False
    assert WeekInfo(wednesday).is_weekend is False
    assert WeekInfo(thursday).is_weekend is False
    assert WeekInfo(friday).is_weekend is False
    assert WeekInfo(saturday).is_weekend is True
    assert WeekInfo(sunday).is_weekend is True


def test_time_type_state_certain_day(days, monday, tuesday, wednesday, thursday, friday, saturday,
                                     sunday):
    """ Test WeekInfo days of given datetime """

    for day in days:
        assert WeekInfo(day).is_monday is (day is monday)
        assert WeekInfo(day).is_tuesday is (day is tuesday)
        assert WeekInfo(day).is_wednesday is (day is wednesday)
        assert WeekInfo(day).is_thursday is (day is thursday)
        assert WeekInfo(day).is_friday is (day is friday)
        assert WeekInfo(day).is_saturday is (day is saturday)
        assert WeekInfo(day).is_sunday is (day is sunday)


def test_time_type_state_types(monday, tuesday, wednesday, thursday, friday, saturday, sunday):
    """ Test fitting types for the given datetime """

    assert WeekInfo(monday).types == {TimeType.MONDAY, TimeType.WEEKDAY}
    assert WeekInfo(tuesday).types == {TimeType.TUESDAY, TimeType.WEEKDAY}
    assert WeekInfo(wednesday).types == {TimeType.WEDNESDAY, TimeType.WEEKDAY}
    assert WeekInfo(thursday).types == {TimeType.THURSDAY, TimeType.WEEKDAY}
    assert WeekInfo(friday).types == {TimeType.FRIDAY, TimeType.WEEKDAY}
    assert WeekInfo(saturday).types == {TimeType.SATURDAY, TimeType.WEEKEND}
    assert WeekInfo(sunday).types == {TimeType.SUNDAY, TimeType.WEEKEND}
