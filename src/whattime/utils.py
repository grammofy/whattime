import inspect
from datetime import datetime
from typing import Set, Dict, Type, Union, Tuple

from lazy import lazy as lazy_property

from .day import DayTimeInfo, day_time_info
from .season import SeasonInfo, season_info
from .type import TimeType, Hemisphere, SeasonType
from .week import WeekInfo, week_info


class TimeInfo(DayTimeInfo, WeekInfo, SeasonInfo):
    _mapping = {}

    @lazy_property
    def __mapping__(self) -> Dict[Union[str, Tuple], TimeType]:
        if not self._mapping:
            for cls in TimeInfo.__bases__:
                kwargs = self._base_kwargs(cls)
                self._mapping.update(cls(**kwargs).__mapping__)

        return self._mapping

    @lazy_property
    def types(self) -> Set[TimeType]:
        if not self._types:
            for cls in TimeInfo.__bases__:
                kwargs = self._base_kwargs(cls)
                self._types = self._types.union(cls(**kwargs).types)

        return self._types

    def _base_kwargs(self, cls: Type) -> Dict[str, Union[datetime, Hemisphere]]:
        args = inspect.getfullargspec(cls.__init__).args
        return {arg: self.__getattribute__(arg) for arg in args if arg != 'self'}


def whattime(date: datetime,
             season_type: SeasonType = SeasonType.GREGORIAN,
             hemisphere: Hemisphere = None) -> TimeInfo:
    return TimeInfo(date, season_type, hemisphere)
