from datetime import datetime

from whattime import Hemisphere, season_info, SeasonType
from whattime.season import SeasonInfo


# Gregorian seasons:
# Spring:


def test_is_spring_for_northern_hemisphere(months):
    """Test returns true for spring months on the northern hemisphere"""

    assert season_info(months.january, Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.february, Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.march, Hemisphere.NORTHERN).is_spring is True
    assert season_info(months.april, Hemisphere.NORTHERN).is_spring is True
    assert season_info(months.may, Hemisphere.NORTHERN).is_spring is True
    assert season_info(months.june, Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.july, Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.august, Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.september, Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.october, Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.november, Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.december, Hemisphere.NORTHERN).is_spring is False


def test_is_spring_for_southern_hemisphere(months):
    """Test returns true for spring months on the southern hemisphere"""

    assert season_info(months.january, Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.february, Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.march, Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.april, Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.may, Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.june, Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.july, Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.august, Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.september, Hemisphere.SOUTHERN).is_spring is True
    assert season_info(months.october, Hemisphere.SOUTHERN).is_spring is True
    assert season_info(months.november, Hemisphere.SOUTHERN).is_spring is True
    assert season_info(months.december, Hemisphere.SOUTHERN).is_spring is False


# Summer:

def test_is_summer_for_northern_hemisphere(months):
    """Test returns true for summer months on the northern hemisphere"""

    assert season_info(months.january, Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.february, Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.march, Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.april, Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.may, Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.june, Hemisphere.NORTHERN).is_summer is True
    assert season_info(months.july, Hemisphere.NORTHERN).is_summer is True
    assert season_info(months.august, Hemisphere.NORTHERN).is_summer is True
    assert season_info(months.september, Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.october, Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.november, Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.december, Hemisphere.NORTHERN).is_summer is False


def test_is_summer_for_southern_hemisphere(months):
    """Test returns true for summer months on the southern hemisphere"""

    assert season_info(months.january, Hemisphere.SOUTHERN).is_summer is True
    assert season_info(months.february, Hemisphere.SOUTHERN).is_summer is True
    assert season_info(months.march, Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.april, Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.may, Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.june, Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.july, Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.august, Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.september, Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.october, Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.november, Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.december, Hemisphere.SOUTHERN).is_summer is True


# Autumn:

def test_is_autumn_for_northern_hemisphere(months):
    """Test returns true for autumn months on the northern hemisphere"""

    assert season_info(months.january, Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.february, Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.march, Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.april, Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.may, Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.june, Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.july, Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.august, Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.september, Hemisphere.NORTHERN).is_autumn is True
    assert season_info(months.october, Hemisphere.NORTHERN).is_autumn is True
    assert season_info(months.november, Hemisphere.NORTHERN).is_autumn is True
    assert season_info(months.december, Hemisphere.NORTHERN).is_autumn is False


def test_is_autumn_for_southern_hemisphere(months):
    """Test returns true for autumn months on the southern hemisphere"""

    assert season_info(months.january, Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.february, Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.march, Hemisphere.SOUTHERN).is_autumn is True
    assert season_info(months.april, Hemisphere.SOUTHERN).is_autumn is True
    assert season_info(months.may, Hemisphere.SOUTHERN).is_autumn is True
    assert season_info(months.june, Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.july, Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.august, Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.september, Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.october, Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.november, Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.december, Hemisphere.SOUTHERN).is_autumn is False


# Winter:

def test_is_winter_for_northern_hemisphere(months):
    """Test returns true for winter months on the northern hemisphere"""

    assert season_info(months.january, Hemisphere.NORTHERN).is_winter is True
    assert season_info(months.february, Hemisphere.NORTHERN).is_winter is True
    assert season_info(months.march, Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.april, Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.may, Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.june, Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.july, Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.august, Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.september, Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.october, Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.november, Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.december, Hemisphere.NORTHERN).is_winter is True


def test_is_winter_for_southern_hemisphere(months):
    """Test returns true for winter months on the southern hemisphere"""

    assert season_info(months.january, Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.february, Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.march, Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.april, Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.may, Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.june, Hemisphere.SOUTHERN).is_winter is True
    assert season_info(months.july, Hemisphere.SOUTHERN).is_winter is True
    assert season_info(months.august, Hemisphere.SOUTHERN).is_winter is True
    assert season_info(months.september, Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.october, Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.november, Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.december, Hemisphere.SOUTHERN).is_winter is False


# Tropical seasons:
# Wet season:

def test_is_wet_season_for_northern_hemisphere(months):
    """Test returns true for wet season months on the northern hemisphere"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, Hemisphere.NORTHERN, SeasonType.TROPICAL)

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
        return season_info(month, Hemisphere.SOUTHERN, SeasonType.TROPICAL)

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
        return season_info(month, Hemisphere.NORTHERN, SeasonType.TROPICAL)

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
        return season_info(month, Hemisphere.SOUTHERN, SeasonType.TROPICAL)

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
