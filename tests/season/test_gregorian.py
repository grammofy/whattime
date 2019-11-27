from whattime import Hemisphere, season_info


# Spring:

def test_is_spring_for_northern_hemisphere(months):
    """Test returns true for spring months on the northern hemisphere"""

    assert season_info(months.january, hemisphere=Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.february, hemisphere=Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.march, hemisphere=Hemisphere.NORTHERN).is_spring is True
    assert season_info(months.april, hemisphere=Hemisphere.NORTHERN).is_spring is True
    assert season_info(months.may, hemisphere=Hemisphere.NORTHERN).is_spring is True
    assert season_info(months.june, hemisphere=Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.july, hemisphere=Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.august, hemisphere=Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.september, hemisphere=Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.october, hemisphere=Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.november, hemisphere=Hemisphere.NORTHERN).is_spring is False
    assert season_info(months.december, hemisphere=Hemisphere.NORTHERN).is_spring is False


def test_is_spring_for_southern_hemisphere(months):
    """Test returns true for spring months on the southern hemisphere"""

    assert season_info(months.january, hemisphere=Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.february, hemisphere=Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.march, hemisphere=Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.april, hemisphere=Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.may, hemisphere=Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.june, hemisphere=Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.july, hemisphere=Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.august, hemisphere=Hemisphere.SOUTHERN).is_spring is False
    assert season_info(months.september, hemisphere=Hemisphere.SOUTHERN).is_spring is True
    assert season_info(months.october, hemisphere=Hemisphere.SOUTHERN).is_spring is True
    assert season_info(months.november, hemisphere=Hemisphere.SOUTHERN).is_spring is True
    assert season_info(months.december, hemisphere=Hemisphere.SOUTHERN).is_spring is False


# Summer:

def test_is_summer_for_northern_hemisphere(months):
    """Test returns true for summer months on the northern hemisphere"""

    assert season_info(months.january, hemisphere=Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.february, hemisphere=Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.march, hemisphere=Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.april, hemisphere=Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.may, hemisphere=Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.june, hemisphere=Hemisphere.NORTHERN).is_summer is True
    assert season_info(months.july, hemisphere=Hemisphere.NORTHERN).is_summer is True
    assert season_info(months.august, hemisphere=Hemisphere.NORTHERN).is_summer is True
    assert season_info(months.september, hemisphere=Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.october, hemisphere=Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.november, hemisphere=Hemisphere.NORTHERN).is_summer is False
    assert season_info(months.december, hemisphere=Hemisphere.NORTHERN).is_summer is False


def test_is_summer_for_southern_hemisphere(months):
    """Test returns true for summer months on the southern hemisphere"""

    assert season_info(months.january, hemisphere=Hemisphere.SOUTHERN).is_summer is True
    assert season_info(months.february, hemisphere=Hemisphere.SOUTHERN).is_summer is True
    assert season_info(months.march, hemisphere=Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.april, hemisphere=Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.may, hemisphere=Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.june, hemisphere=Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.july, hemisphere=Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.august, hemisphere=Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.september, hemisphere=Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.october, hemisphere=Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.november, hemisphere=Hemisphere.SOUTHERN).is_summer is False
    assert season_info(months.december, hemisphere=Hemisphere.SOUTHERN).is_summer is True


# Autumn:

def test_is_autumn_for_northern_hemisphere(months):
    """Test returns true for autumn months on the northern hemisphere"""

    assert season_info(months.january, hemisphere=Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.february, hemisphere=Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.march, hemisphere=Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.april, hemisphere=Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.may, hemisphere=Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.june, hemisphere=Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.july, hemisphere=Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.august, hemisphere=Hemisphere.NORTHERN).is_autumn is False
    assert season_info(months.september, hemisphere=Hemisphere.NORTHERN).is_autumn is True
    assert season_info(months.october, hemisphere=Hemisphere.NORTHERN).is_autumn is True
    assert season_info(months.november, hemisphere=Hemisphere.NORTHERN).is_autumn is True
    assert season_info(months.december, hemisphere=Hemisphere.NORTHERN).is_autumn is False


def test_is_autumn_for_southern_hemisphere(months):
    """Test returns true for autumn months on the southern hemisphere"""

    assert season_info(months.january, hemisphere=Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.february, hemisphere=Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.march, hemisphere=Hemisphere.SOUTHERN).is_autumn is True
    assert season_info(months.april, hemisphere=Hemisphere.SOUTHERN).is_autumn is True
    assert season_info(months.may, hemisphere=Hemisphere.SOUTHERN).is_autumn is True
    assert season_info(months.june, hemisphere=Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.july, hemisphere=Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.august, hemisphere=Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.september, hemisphere=Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.october, hemisphere=Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.november, hemisphere=Hemisphere.SOUTHERN).is_autumn is False
    assert season_info(months.december, hemisphere=Hemisphere.SOUTHERN).is_autumn is False


# Winter:

def test_is_winter_for_northern_hemisphere(months):
    """Test returns true for winter months on the northern hemisphere"""

    assert season_info(months.january, hemisphere=Hemisphere.NORTHERN).is_winter is True
    assert season_info(months.february, hemisphere=Hemisphere.NORTHERN).is_winter is True
    assert season_info(months.march, hemisphere=Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.april, hemisphere=Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.may, hemisphere=Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.june, hemisphere=Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.july, hemisphere=Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.august, hemisphere=Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.september, hemisphere=Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.october, hemisphere=Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.november, hemisphere=Hemisphere.NORTHERN).is_winter is False
    assert season_info(months.december, hemisphere=Hemisphere.NORTHERN).is_winter is True


def test_is_winter_for_southern_hemisphere(months):
    """Test returns true for winter months on the southern hemisphere"""

    assert season_info(months.january, hemisphere=Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.february, hemisphere=Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.march, hemisphere=Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.april, hemisphere=Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.may, hemisphere=Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.june, hemisphere=Hemisphere.SOUTHERN).is_winter is True
    assert season_info(months.july, hemisphere=Hemisphere.SOUTHERN).is_winter is True
    assert season_info(months.august, hemisphere=Hemisphere.SOUTHERN).is_winter is True
    assert season_info(months.september, hemisphere=Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.october, hemisphere=Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.november, hemisphere=Hemisphere.SOUTHERN).is_winter is False
    assert season_info(months.december, hemisphere=Hemisphere.SOUTHERN).is_winter is False
