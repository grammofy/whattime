from datetime import datetime

from whattime import whattime, Hemisphere, SeasonType
from whattime.utils import TimeInfo


def test_whattime():
    """Test whattime is a wrapper function for instantiating a TimeInfo object"""

    now = datetime.utcnow()
    info = whattime(now, hemisphere=Hemisphere.SOUTHERN)

    assert isinstance(info, TimeInfo)


def test_whattime_with_custom_season_type():
    """Test whattime allows to customize the season type"""

    now = datetime.utcnow()
    info = whattime(now, season_type=SeasonType.TROPICAL, hemisphere=Hemisphere.SOUTHERN)

    assert isinstance(info, TimeInfo)
