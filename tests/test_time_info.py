from datetime import datetime

from whattime import TimeType
from whattime import time_info


def test_time_info(monday: datetime):
    """Test time_info combines multiple info"""

    monday_noon = monday.replace(hour=12, minute=30)
    info = time_info(monday_noon)

    assert info.types == {TimeType.MONDAY, TimeType.WEEKDAY, TimeType.NOON}

    assert info.is_monday is True
    assert info.is_tuesday is False
    assert info.is_wednesday is False
    assert info.is_thursday is False
    assert info.is_friday is False
    assert info.is_saturday is False
    assert info.is_sunday is False
    assert info.is_weekend is False
    assert info.is_weekday is True

    assert info.is_morning is False
    assert info.is_midmorning is False
    assert info.is_noon is True
    assert info.is_afternoon is False
    assert info.is_evening is False
    assert info.is_night is False
