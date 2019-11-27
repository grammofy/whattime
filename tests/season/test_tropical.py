from datetime import datetime

from whattime import Hemisphere, season_info, SeasonType
from whattime.season import SeasonInfo


# Wet season:

def test_is_wet_season_for_northern_hemisphere(months):
    """Test returns true for wet season months on the northern hemisphere"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.TROPICAL, Hemisphere.NORTHERN)

    assert info_for(months.january).is_wet_season is False
    assert info_for(months.february).is_wet_season is False
    assert info_for(months.march).is_wet_season is False
    assert info_for(months.april).is_wet_season is False
    assert info_for(months.may).is_wet_season is True
    assert info_for(months.june).is_wet_season is True
    assert info_for(months.july).is_wet_season is True
    assert info_for(months.august).is_wet_season is True
    assert info_for(months.september).is_wet_season is True
    assert info_for(months.october).is_wet_season is True
    assert info_for(months.november).is_wet_season is False
    assert info_for(months.december).is_wet_season is False


def test_is_wet_season_for_southern_hemisphere(months):
    """Test returns true for wet season months on the southern hemisphere"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.TROPICAL, Hemisphere.SOUTHERN)

    assert info_for(months.january).is_wet_season is True
    assert info_for(months.february).is_wet_season is True
    assert info_for(months.march).is_wet_season is True
    assert info_for(months.april).is_wet_season is True
    assert info_for(months.may).is_wet_season is False
    assert info_for(months.june).is_wet_season is False
    assert info_for(months.july).is_wet_season is False
    assert info_for(months.august).is_wet_season is False
    assert info_for(months.september).is_wet_season is False
    assert info_for(months.october).is_wet_season is False
    assert info_for(months.november).is_wet_season is True
    assert info_for(months.december).is_wet_season is True


# Dry season:

def test_is_dry_season_for_northern_hemisphere(months):
    """Test returns true for dry season months on the northern hemisphere"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.TROPICAL, Hemisphere.NORTHERN)

    assert info_for(months.january).is_dry_season is True
    assert info_for(months.february).is_dry_season is True
    assert info_for(months.march).is_dry_season is True
    assert info_for(months.april).is_dry_season is True
    assert info_for(months.may).is_dry_season is False
    assert info_for(months.june).is_dry_season is False
    assert info_for(months.july).is_dry_season is False
    assert info_for(months.august).is_dry_season is False
    assert info_for(months.september).is_dry_season is False
    assert info_for(months.october).is_dry_season is False
    assert info_for(months.november).is_dry_season is True
    assert info_for(months.december).is_dry_season is True


def test_is_dry_season_for_southern_hemisphere(months):
    """Test returns true for dry season months on the southern hemisphere"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.TROPICAL, Hemisphere.SOUTHERN)

    assert info_for(months.january).is_dry_season is False
    assert info_for(months.february).is_dry_season is False
    assert info_for(months.march).is_dry_season is False
    assert info_for(months.april).is_dry_season is False
    assert info_for(months.may).is_dry_season is True
    assert info_for(months.june).is_dry_season is True
    assert info_for(months.july).is_dry_season is True
    assert info_for(months.august).is_dry_season is True
    assert info_for(months.september).is_dry_season is True
    assert info_for(months.october).is_dry_season is True
    assert info_for(months.november).is_dry_season is False
    assert info_for(months.december).is_dry_season is False
