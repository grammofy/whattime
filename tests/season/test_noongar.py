from datetime import datetime

from whattime import season_info, SeasonType
from whattime.season import SeasonInfo


def test_is_birak(months):
    """Test returns True for Birak months"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.NOONGAR)

    assert info_for(months.january).is_birak is True
    assert info_for(months.february).is_birak is False
    assert info_for(months.march).is_birak is False
    assert info_for(months.april).is_birak is False
    assert info_for(months.may).is_birak is False
    assert info_for(months.june).is_birak is False
    assert info_for(months.july).is_birak is False
    assert info_for(months.august).is_birak is False
    assert info_for(months.september).is_birak is False
    assert info_for(months.october).is_birak is False
    assert info_for(months.november).is_birak is False
    assert info_for(months.december).is_birak is True


def test_is_bunuru(months):
    """Test returns True for Bunuru months"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.NOONGAR)

    assert info_for(months.january).is_bunuru is False
    assert info_for(months.february).is_bunuru is True
    assert info_for(months.march).is_bunuru is True
    assert info_for(months.april).is_bunuru is False
    assert info_for(months.may).is_bunuru is False
    assert info_for(months.june).is_bunuru is False
    assert info_for(months.july).is_bunuru is False
    assert info_for(months.august).is_bunuru is False
    assert info_for(months.september).is_bunuru is False
    assert info_for(months.october).is_bunuru is False
    assert info_for(months.november).is_bunuru is False
    assert info_for(months.december).is_bunuru is False


def test_is_djeran(months):
    """Test returns True for Djeran months"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.NOONGAR)

    assert info_for(months.january).is_djeran is False
    assert info_for(months.february).is_djeran is False
    assert info_for(months.march).is_djeran is False
    assert info_for(months.april).is_djeran is True
    assert info_for(months.may).is_djeran is True
    assert info_for(months.june).is_djeran is False
    assert info_for(months.july).is_djeran is False
    assert info_for(months.august).is_djeran is False
    assert info_for(months.september).is_djeran is False
    assert info_for(months.october).is_djeran is False
    assert info_for(months.november).is_djeran is False
    assert info_for(months.december).is_djeran is False


def test_is_makuru(months):
    """Test returns True for Makuru months"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.NOONGAR)

    assert info_for(months.january).is_makuru is False
    assert info_for(months.february).is_makuru is False
    assert info_for(months.march).is_makuru is False
    assert info_for(months.april).is_makuru is False
    assert info_for(months.may).is_makuru is False
    assert info_for(months.june).is_makuru is True
    assert info_for(months.july).is_makuru is True
    assert info_for(months.august).is_makuru is False
    assert info_for(months.september).is_makuru is False
    assert info_for(months.october).is_makuru is False
    assert info_for(months.november).is_makuru is False
    assert info_for(months.december).is_makuru is False


def test_is_djilba(months):
    """Test returns True for Djilba months"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.NOONGAR)

    assert info_for(months.january).is_djilba is False
    assert info_for(months.february).is_djilba is False
    assert info_for(months.march).is_djilba is False
    assert info_for(months.april).is_djilba is False
    assert info_for(months.may).is_djilba is False
    assert info_for(months.june).is_djilba is False
    assert info_for(months.july).is_djilba is False
    assert info_for(months.august).is_djilba is True
    assert info_for(months.september).is_djilba is True
    assert info_for(months.october).is_djilba is False
    assert info_for(months.november).is_djilba is False
    assert info_for(months.december).is_djilba is False


def test_is_kambarang(months):
    """Test returns True for Kambarang months"""

    def info_for(month: datetime) -> SeasonInfo:
        return season_info(month, SeasonType.NOONGAR)

    assert info_for(months.january).is_kambarang is False
    assert info_for(months.february).is_kambarang is False
    assert info_for(months.march).is_kambarang is False
    assert info_for(months.april).is_kambarang is False
    assert info_for(months.may).is_kambarang is False
    assert info_for(months.june).is_kambarang is False
    assert info_for(months.july).is_kambarang is False
    assert info_for(months.august).is_kambarang is False
    assert info_for(months.september).is_kambarang is False
    assert info_for(months.october).is_kambarang is True
    assert info_for(months.november).is_kambarang is True
    assert info_for(months.december).is_kambarang is False
