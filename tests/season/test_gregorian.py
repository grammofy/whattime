from datetime import datetime

from whattime import Hemisphere, season_info, TimeType
from whattime.season import SeasonInfo


def northern_info(month: datetime) -> SeasonInfo:
    return season_info(month, hemisphere=Hemisphere.NORTHERN)


def southern_info(month: datetime) -> SeasonInfo:
    return season_info(month, hemisphere=Hemisphere.SOUTHERN)


# Spring:

def test_is_spring_for_northern_hemisphere(months):
    """Test returns true for spring months on the northern hemisphere"""

    assert northern_info(months.january).is_spring is False
    assert northern_info(months.february).is_spring is False
    assert northern_info(months.march).is_spring is True
    assert northern_info(months.april).is_spring is True
    assert northern_info(months.may).is_spring is True
    assert northern_info(months.june).is_spring is False
    assert northern_info(months.july).is_spring is False
    assert northern_info(months.august).is_spring is False
    assert northern_info(months.september).is_spring is False
    assert northern_info(months.october).is_spring is False
    assert northern_info(months.november).is_spring is False
    assert northern_info(months.december).is_spring is False


def test_is_spring_for_southern_hemisphere(months):
    """Test returns true for spring months on the southern hemisphere"""

    assert southern_info(months.january).is_spring is False
    assert southern_info(months.february).is_spring is False
    assert southern_info(months.march).is_spring is False
    assert southern_info(months.april).is_spring is False
    assert southern_info(months.may).is_spring is False
    assert southern_info(months.june).is_spring is False
    assert southern_info(months.july).is_spring is False
    assert southern_info(months.august).is_spring is False
    assert southern_info(months.september).is_spring is True
    assert southern_info(months.october).is_spring is True
    assert southern_info(months.november).is_spring is True
    assert southern_info(months.december).is_spring is False


# Summer:

def test_is_summer_for_northern_hemisphere(months):
    """Test returns true for summer months on the northern hemisphere"""

    assert northern_info(months.january).is_summer is False
    assert northern_info(months.february).is_summer is False
    assert northern_info(months.march).is_summer is False
    assert northern_info(months.april).is_summer is False
    assert northern_info(months.may).is_summer is False
    assert northern_info(months.june).is_summer is True
    assert northern_info(months.july).is_summer is True
    assert northern_info(months.august).is_summer is True
    assert northern_info(months.september).is_summer is False
    assert northern_info(months.october).is_summer is False
    assert northern_info(months.november).is_summer is False
    assert northern_info(months.december).is_summer is False


def test_is_summer_for_southern_hemisphere(months):
    """Test returns true for summer months on the southern hemisphere"""

    assert southern_info(months.january).is_summer is True
    assert southern_info(months.february).is_summer is True
    assert southern_info(months.march).is_summer is False
    assert southern_info(months.april).is_summer is False
    assert southern_info(months.may).is_summer is False
    assert southern_info(months.june).is_summer is False
    assert southern_info(months.july).is_summer is False
    assert southern_info(months.august).is_summer is False
    assert southern_info(months.september).is_summer is False
    assert southern_info(months.october).is_summer is False
    assert southern_info(months.november).is_summer is False
    assert southern_info(months.december).is_summer is True


# Autumn:

def test_is_autumn_for_northern_hemisphere(months):
    """Test returns true for autumn months on the northern hemisphere"""

    assert northern_info(months.january).is_autumn is False
    assert northern_info(months.february).is_autumn is False
    assert northern_info(months.march).is_autumn is False
    assert northern_info(months.april).is_autumn is False
    assert northern_info(months.may).is_autumn is False
    assert northern_info(months.june).is_autumn is False
    assert northern_info(months.july).is_autumn is False
    assert northern_info(months.august).is_autumn is False
    assert northern_info(months.september).is_autumn is True
    assert northern_info(months.october).is_autumn is True
    assert northern_info(months.november).is_autumn is True
    assert northern_info(months.december).is_autumn is False


def test_is_autumn_for_southern_hemisphere(months):
    """Test returns true for autumn months on the southern hemisphere"""

    assert southern_info(months.january).is_autumn is False
    assert southern_info(months.february).is_autumn is False
    assert southern_info(months.march).is_autumn is True
    assert southern_info(months.april).is_autumn is True
    assert southern_info(months.may).is_autumn is True
    assert southern_info(months.june).is_autumn is False
    assert southern_info(months.july).is_autumn is False
    assert southern_info(months.august).is_autumn is False
    assert southern_info(months.september).is_autumn is False
    assert southern_info(months.october).is_autumn is False
    assert southern_info(months.november).is_autumn is False
    assert southern_info(months.december).is_autumn is False


# Winter:

def test_is_winter_for_northern_hemisphere(months):
    """Test returns true for winter months on the northern hemisphere"""

    assert northern_info(months.january).is_winter is True
    assert northern_info(months.february).is_winter is True
    assert northern_info(months.march).is_winter is False
    assert northern_info(months.april).is_winter is False
    assert northern_info(months.may).is_winter is False
    assert northern_info(months.june).is_winter is False
    assert northern_info(months.july).is_winter is False
    assert northern_info(months.august).is_winter is False
    assert northern_info(months.september).is_winter is False
    assert northern_info(months.october).is_winter is False
    assert northern_info(months.november).is_winter is False
    assert northern_info(months.december).is_winter is True


def test_is_winter_for_southern_hemisphere(months):
    """Test returns true for winter months on the southern hemisphere"""

    assert southern_info(months.january).is_winter is False
    assert southern_info(months.february).is_winter is False
    assert southern_info(months.march).is_winter is False
    assert southern_info(months.april).is_winter is False
    assert southern_info(months.may).is_winter is False
    assert southern_info(months.june).is_winter is True
    assert southern_info(months.july).is_winter is True
    assert southern_info(months.august).is_winter is True
    assert southern_info(months.september).is_winter is False
    assert southern_info(months.october).is_winter is False
    assert southern_info(months.november).is_winter is False
    assert southern_info(months.december).is_winter is False


def test_types(months):
    """Test returns the right time types on the northern hemisphere"""

    for month in months:
        southern = southern_info(month)

        if southern.is_spring:
            assert TimeType.SPRING in southern.types

        if southern.is_summer:
            assert TimeType.SUMMER in southern.types

        if southern.is_autumn:
            assert TimeType.AUTUMN in southern.types

        if southern.is_winter:
            assert TimeType.WINTER in southern.types

        northern = northern_info(month)

        if northern.is_spring:
            assert TimeType.SPRING in northern.types

        if northern.is_summer:
            assert TimeType.SUMMER in northern.types

        if northern.is_autumn:
            assert TimeType.AUTUMN in northern.types

        if northern.is_winter:
            assert TimeType.WINTER in northern.types


