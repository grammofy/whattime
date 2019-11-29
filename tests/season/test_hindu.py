from datetime import datetime

from whattime import season_info, SeasonType
from whattime.season import SeasonInfo


def info_for_before_mid_of(month: datetime) -> SeasonInfo:
    return season_info(month.replace(day=14), SeasonType.HINDU)


def info_for_after_mid_of(month: datetime) -> SeasonInfo:
    return season_info(month.replace(day=15), SeasonType.HINDU)


def test_is_vasanta(months):
    """Test returns True for all days in Vasanta"""

    assert info_for_before_mid_of(months.january).is_vasanta is False
    assert info_for_after_mid_of(months.january).is_vasanta is False

    assert info_for_before_mid_of(months.february).is_vasanta is False
    assert info_for_after_mid_of(months.february).is_vasanta is False

    assert info_for_before_mid_of(months.march).is_vasanta is False
    assert info_for_after_mid_of(months.march).is_vasanta is True

    assert info_for_before_mid_of(months.april).is_vasanta is True
    assert info_for_after_mid_of(months.april).is_vasanta is True

    assert info_for_before_mid_of(months.may).is_vasanta is True
    assert info_for_after_mid_of(months.may).is_vasanta is False

    assert info_for_before_mid_of(months.june).is_vasanta is False
    assert info_for_after_mid_of(months.june).is_vasanta is False

    assert info_for_before_mid_of(months.july).is_vasanta is False
    assert info_for_after_mid_of(months.july).is_vasanta is False

    assert info_for_before_mid_of(months.august).is_vasanta is False
    assert info_for_after_mid_of(months.august).is_vasanta is False

    assert info_for_before_mid_of(months.september).is_vasanta is False
    assert info_for_after_mid_of(months.september).is_vasanta is False

    assert info_for_before_mid_of(months.october).is_vasanta is False
    assert info_for_after_mid_of(months.october).is_vasanta is False

    assert info_for_before_mid_of(months.november).is_vasanta is False
    assert info_for_after_mid_of(months.november).is_vasanta is False

    assert info_for_before_mid_of(months.december).is_vasanta is False
    assert info_for_after_mid_of(months.december).is_vasanta is False


def test_is_greeshma(months):
    """Test returns True for all days in Greeshma"""

    assert info_for_before_mid_of(months.january).is_greeshma is False
    assert info_for_after_mid_of(months.january).is_greeshma is False

    assert info_for_before_mid_of(months.february).is_greeshma is False
    assert info_for_after_mid_of(months.february).is_greeshma is False

    assert info_for_before_mid_of(months.march).is_greeshma is False
    assert info_for_after_mid_of(months.march).is_greeshma is False

    assert info_for_before_mid_of(months.april).is_greeshma is False
    assert info_for_after_mid_of(months.april).is_greeshma is False

    assert info_for_before_mid_of(months.may).is_greeshma is False
    assert info_for_after_mid_of(months.may).is_greeshma is True

    assert info_for_before_mid_of(months.june).is_greeshma is True
    assert info_for_after_mid_of(months.june).is_greeshma is True

    assert info_for_before_mid_of(months.july).is_greeshma is True
    assert info_for_after_mid_of(months.july).is_greeshma is False

    assert info_for_before_mid_of(months.august).is_greeshma is False
    assert info_for_after_mid_of(months.august).is_greeshma is False

    assert info_for_before_mid_of(months.september).is_greeshma is False
    assert info_for_after_mid_of(months.september).is_greeshma is False

    assert info_for_before_mid_of(months.october).is_greeshma is False
    assert info_for_after_mid_of(months.october).is_greeshma is False

    assert info_for_before_mid_of(months.november).is_greeshma is False
    assert info_for_after_mid_of(months.november).is_greeshma is False

    assert info_for_before_mid_of(months.december).is_greeshma is False
    assert info_for_after_mid_of(months.december).is_greeshma is False


def test_is_varsha(months):
    """Test returns True for all days in Varsha"""

    assert info_for_before_mid_of(months.january).is_varsha is False
    assert info_for_after_mid_of(months.january).is_varsha is False

    assert info_for_before_mid_of(months.february).is_varsha is False
    assert info_for_after_mid_of(months.february).is_varsha is False

    assert info_for_before_mid_of(months.march).is_varsha is False
    assert info_for_after_mid_of(months.march).is_varsha is False

    assert info_for_before_mid_of(months.april).is_varsha is False
    assert info_for_after_mid_of(months.april).is_varsha is False

    assert info_for_before_mid_of(months.may).is_varsha is False
    assert info_for_after_mid_of(months.may).is_varsha is False

    assert info_for_before_mid_of(months.june).is_varsha is False
    assert info_for_after_mid_of(months.june).is_varsha is False

    assert info_for_before_mid_of(months.july).is_varsha is False
    assert info_for_after_mid_of(months.july).is_varsha is True

    assert info_for_before_mid_of(months.august).is_varsha is True
    assert info_for_after_mid_of(months.august).is_varsha is True

    assert info_for_before_mid_of(months.september).is_varsha is True
    assert info_for_after_mid_of(months.september).is_varsha is False

    assert info_for_before_mid_of(months.october).is_varsha is False
    assert info_for_after_mid_of(months.october).is_varsha is False

    assert info_for_before_mid_of(months.november).is_varsha is False
    assert info_for_after_mid_of(months.november).is_varsha is False

    assert info_for_before_mid_of(months.december).is_varsha is False
    assert info_for_after_mid_of(months.december).is_varsha is False


def test_is_sharad(months):
    """Test returns True for all days in Sharad"""

    assert info_for_before_mid_of(months.january).is_sharad is False
    assert info_for_after_mid_of(months.january).is_sharad is False

    assert info_for_before_mid_of(months.february).is_sharad is False
    assert info_for_after_mid_of(months.february).is_sharad is False

    assert info_for_before_mid_of(months.march).is_sharad is False
    assert info_for_after_mid_of(months.march).is_sharad is False

    assert info_for_before_mid_of(months.april).is_sharad is False
    assert info_for_after_mid_of(months.april).is_sharad is False

    assert info_for_before_mid_of(months.may).is_sharad is False
    assert info_for_after_mid_of(months.may).is_sharad is False

    assert info_for_before_mid_of(months.june).is_sharad is False
    assert info_for_after_mid_of(months.june).is_sharad is False

    assert info_for_before_mid_of(months.july).is_sharad is False
    assert info_for_after_mid_of(months.july).is_sharad is False

    assert info_for_before_mid_of(months.august).is_sharad is False
    assert info_for_after_mid_of(months.august).is_sharad is False

    assert info_for_before_mid_of(months.september).is_sharad is False
    assert info_for_after_mid_of(months.september).is_sharad is True

    assert info_for_before_mid_of(months.october).is_sharad is True
    assert info_for_after_mid_of(months.october).is_sharad is True

    assert info_for_before_mid_of(months.november).is_sharad is True
    assert info_for_after_mid_of(months.november).is_sharad is False

    assert info_for_before_mid_of(months.december).is_sharad is False
    assert info_for_after_mid_of(months.december).is_sharad is False


def test_is_hemanta(months):
    """Test returns True for all days in Hemanta"""

    assert info_for_before_mid_of(months.january).is_hemanta is True
    assert info_for_after_mid_of(months.january).is_hemanta is False

    assert info_for_before_mid_of(months.february).is_hemanta is False
    assert info_for_after_mid_of(months.february).is_hemanta is False

    assert info_for_before_mid_of(months.march).is_hemanta is False
    assert info_for_after_mid_of(months.march).is_hemanta is False

    assert info_for_before_mid_of(months.april).is_hemanta is False
    assert info_for_after_mid_of(months.april).is_hemanta is False

    assert info_for_before_mid_of(months.may).is_hemanta is False
    assert info_for_after_mid_of(months.may).is_hemanta is False

    assert info_for_before_mid_of(months.june).is_hemanta is False
    assert info_for_after_mid_of(months.june).is_hemanta is False

    assert info_for_before_mid_of(months.july).is_hemanta is False
    assert info_for_after_mid_of(months.july).is_hemanta is False

    assert info_for_before_mid_of(months.august).is_hemanta is False
    assert info_for_after_mid_of(months.august).is_hemanta is False

    assert info_for_before_mid_of(months.september).is_hemanta is False
    assert info_for_after_mid_of(months.september).is_hemanta is False

    assert info_for_before_mid_of(months.october).is_hemanta is False
    assert info_for_after_mid_of(months.october).is_hemanta is False

    assert info_for_before_mid_of(months.november).is_hemanta is False
    assert info_for_after_mid_of(months.november).is_hemanta is True

    assert info_for_before_mid_of(months.december).is_hemanta is True
    assert info_for_after_mid_of(months.december).is_hemanta is True


def test_is_shishira(months):
    """Test returns True for all days in Shishira"""

    assert info_for_before_mid_of(months.january).is_shishira is False
    assert info_for_after_mid_of(months.january).is_shishira is True

    assert info_for_before_mid_of(months.february).is_shishira is True
    assert info_for_after_mid_of(months.february).is_shishira is True

    assert info_for_before_mid_of(months.march).is_shishira is True
    assert info_for_after_mid_of(months.march).is_shishira is False

    assert info_for_before_mid_of(months.april).is_shishira is False
    assert info_for_after_mid_of(months.april).is_shishira is False

    assert info_for_before_mid_of(months.may).is_shishira is False
    assert info_for_after_mid_of(months.may).is_shishira is False

    assert info_for_before_mid_of(months.june).is_shishira is False
    assert info_for_after_mid_of(months.june).is_shishira is False

    assert info_for_before_mid_of(months.july).is_shishira is False
    assert info_for_after_mid_of(months.july).is_shishira is False

    assert info_for_before_mid_of(months.august).is_shishira is False
    assert info_for_after_mid_of(months.august).is_shishira is False

    assert info_for_before_mid_of(months.september).is_shishira is False
    assert info_for_after_mid_of(months.september).is_shishira is False

    assert info_for_before_mid_of(months.october).is_shishira is False
    assert info_for_after_mid_of(months.october).is_shishira is False

    assert info_for_before_mid_of(months.november).is_shishira is False
    assert info_for_after_mid_of(months.november).is_shishira is False

    assert info_for_before_mid_of(months.december).is_shishira is False
    assert info_for_after_mid_of(months.december).is_shishira is False
