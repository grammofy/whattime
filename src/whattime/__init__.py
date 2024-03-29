# -*- coding: utf-8 -*-

from pkg_resources import get_distribution, DistributionNotFound

try:
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'

__all__ = [
    'whattime',
    'TimeType',
    'Hemisphere',
    'SeasonType',
    'week_info',
    'day_time_info',
    'season_info'
]

from .utils import whattime, week_info, day_time_info, season_info
from .type import TimeType, Hemisphere, SeasonType
