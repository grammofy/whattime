from datetime import datetime

from whattime import season_info, SeasonType
from whattime.season import SeasonInfo


def test_is_pipon(months):
    """Test returns True for Pipon months"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.CREE)

    assert info_for(months.january).is_pipon is True
    assert info_for(months.february).is_pipon is True
    assert info_for(months.march).is_pipon is False
    assert info_for(months.april).is_pipon is False
    assert info_for(months.may).is_pipon is False
    assert info_for(months.june).is_pipon is False
    assert info_for(months.july).is_pipon is False
    assert info_for(months.august).is_pipon is False
    assert info_for(months.september).is_pipon is False
    assert info_for(months.october).is_pipon is False
    assert info_for(months.november).is_pipon is False
    assert info_for(months.december).is_pipon is False


def test_is_sekwun(months):
    """Test returns True for Sekwun months"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.CREE)

    assert info_for(months.january).is_sekwun is False
    assert info_for(months.february).is_sekwun is False
    assert info_for(months.march).is_sekwun is True
    assert info_for(months.april).is_sekwun is True
    assert info_for(months.may).is_sekwun is False
    assert info_for(months.june).is_sekwun is False
    assert info_for(months.july).is_sekwun is False
    assert info_for(months.august).is_sekwun is False
    assert info_for(months.september).is_sekwun is False
    assert info_for(months.october).is_sekwun is False
    assert info_for(months.november).is_sekwun is False
    assert info_for(months.december).is_sekwun is False


def test_is_mithoskumin(months):
    """Test returns True for Mithoskumin months"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.CREE)

    assert info_for(months.january).is_mithoskumin is False
    assert info_for(months.february).is_mithoskumin is False
    assert info_for(months.march).is_mithoskumin is False
    assert info_for(months.april).is_mithoskumin is False
    assert info_for(months.may).is_mithoskumin is True
    assert info_for(months.june).is_mithoskumin is True
    assert info_for(months.july).is_mithoskumin is False
    assert info_for(months.august).is_mithoskumin is False
    assert info_for(months.september).is_mithoskumin is False
    assert info_for(months.october).is_mithoskumin is False
    assert info_for(months.november).is_mithoskumin is False
    assert info_for(months.december).is_mithoskumin is False


def test_is_nepin(months):
    """Test returns True for Nepin months"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.CREE)

    assert info_for(months.january).is_nepin is False
    assert info_for(months.february).is_nepin is False
    assert info_for(months.march).is_nepin is False
    assert info_for(months.april).is_nepin is False
    assert info_for(months.may).is_nepin is False
    assert info_for(months.june).is_nepin is False
    assert info_for(months.july).is_nepin is True
    assert info_for(months.august).is_nepin is True
    assert info_for(months.september).is_nepin is False
    assert info_for(months.october).is_nepin is False
    assert info_for(months.november).is_nepin is False
    assert info_for(months.december).is_nepin is False


def test_is_tukwakin(months):
    """Test returns True for Tukwakin months"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.CREE)

    assert info_for(months.january).is_tukwakin is False
    assert info_for(months.february).is_tukwakin is False
    assert info_for(months.march).is_tukwakin is False
    assert info_for(months.april).is_tukwakin is False
    assert info_for(months.may).is_tukwakin is False
    assert info_for(months.june).is_tukwakin is False
    assert info_for(months.july).is_tukwakin is False
    assert info_for(months.august).is_tukwakin is False
    assert info_for(months.september).is_tukwakin is True
    assert info_for(months.october).is_tukwakin is True
    assert info_for(months.november).is_tukwakin is False
    assert info_for(months.december).is_tukwakin is False


def test_is_mikiskaw(months):
    """Test returns True for Mikiskaw months"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.CREE)

    assert info_for(months.january).is_mikiskaw is False
    assert info_for(months.february).is_mikiskaw is False
    assert info_for(months.march).is_mikiskaw is False
    assert info_for(months.april).is_mikiskaw is False
    assert info_for(months.may).is_mikiskaw is False
    assert info_for(months.june).is_mikiskaw is False
    assert info_for(months.july).is_mikiskaw is False
    assert info_for(months.august).is_mikiskaw is False
    assert info_for(months.september).is_mikiskaw is False
    assert info_for(months.october).is_mikiskaw is False
    assert info_for(months.november).is_mikiskaw is True
    assert info_for(months.december).is_mikiskaw is True
