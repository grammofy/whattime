from typing import Set

from .day import DayTimeInfo
from .type import TimeType
from .week import WeekInfo


class TimeInfo(DayTimeInfo, WeekInfo):

    @property
    def types(self) -> Set[TimeType]:
        if not self._types:
            for info_type in TimeInfo.__bases__:
                self._types = self._types.union(info_type(self.date).types)

        return self._types


time_info = TimeInfo
