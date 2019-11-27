from datetime import datetime

from whattime import Hemisphere, TimeType, whattime, SeasonType
from whattime.utils import TimeInfo


def test_time_info(southern_winter_monday: datetime):
    """Test TimeInfo combines multiple info"""

    monday_noon = southern_winter_monday.replace(hour=12, minute=30)
    info = TimeInfo(monday_noon, hemisphere=Hemisphere.SOUTHERN)

    assert info.types == {TimeType.MONDAY, TimeType.WEEKDAY, TimeType.NOON, TimeType.WINTER}

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

    assert info.is_spring is False
    assert info.is_summer is False
    assert info.is_autumn is False
    assert info.is_winter is True


def test_time_info_with_custom_season_type(southern_winter_monday: datetime):
    """Test TimeInfo allows to adjust the season type"""

    monday_noon = southern_winter_monday.replace(hour=12, minute=30)
    info = TimeInfo(monday_noon, SeasonType.TROPICAL, Hemisphere.SOUTHERN)

    assert info.types == {TimeType.MONDAY, TimeType.WEEKDAY, TimeType.NOON, TimeType.DRY_SEASON}
    assert info.is_wet_season is False
    assert info.is_dry_season is True
