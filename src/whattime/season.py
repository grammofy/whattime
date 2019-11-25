import inspect
import re
import sys
from abc import ABC, abstractmethod
from copy import copy
from datetime import datetime
from typing import Set, Dict, Tuple, Type, Union

from .base import LocationBasedInfoBase
from .type import Hemisphere, TimeType, SeasonType


class Mapping:
    __mapping__ = {}

    def __init__(self, date: datetime):
        self.date = date
        self._mapping = None
        self._inverse_mapping = None

    @property
    def mapping(self) -> Dict[Tuple, TimeType]:
        if not self._mapping or self.__mapping__:
            self._mapping = self.__mapping__

        return self._mapping

    @mapping.setter
    def mapping(self, value):
        self._mapping = value
        self._inverse_mapping = None

    @property
    def inverse_mapping(self) -> Dict[TimeType, Tuple]:
        if not self._inverse_mapping:
            self._inverse_mapping = {v: k for k, v in self.mapping.items()}

        return self._inverse_mapping

    def _is_in_season(self, time_type: TimeType) -> bool:
        return self.date.month in self.inverse_mapping[time_type]


class LocationDependentMapping(ABC, Mapping):
    @property
    @abstractmethod
    def __northern_mapping__(self):
        pass

    @property
    @abstractmethod
    def __southern_mapping__(self):
        pass

    def __init__(self, date: datetime, hemisphere: Hemisphere):
        super().__init__(date)
        self.hemisphere = hemisphere

        if self.hemisphere == Hemisphere.NORTHERN:
            self.mapping = self.__northern_mapping__
        else:
            self.mapping = self.__southern_mapping__


class GregorianMapping(LocationDependentMapping):
    """Mapping for the seasons based on the Gregorian calendar"""

    __northern_mapping__ = {
        (1, 2, 12): TimeType.WINTER,  # Jan, Feb, Dec
        (3, 4, 5): TimeType.SPRING,  # Mar, Apr, May
        (6, 7, 8): TimeType.SUMMER,  # Jun, Jul, Aug
        (9, 10, 11): TimeType.AUTUMN,  # Sep, Oct, Nov
    }

    __southern_mapping__ = {
        (1, 2, 12): TimeType.SUMMER,  # Jan, Feb, Dec
        (3, 4, 5): TimeType.AUTUMN,  # Mar, Apr, May
        (6, 7, 8): TimeType.WINTER,  # Jun, Jul, Aug
        (9, 10, 11): TimeType.SPRING,  # Sep, Oct, Nov
    }

    @property
    def is_spring(self) -> bool:
        """Return whether the given date is in spring on the given hemisphere"""

        return self._is_in_season(TimeType.SPRING)

    @property
    def is_summer(self) -> bool:
        """Return whether the given date is in summer on the given hemisphere"""

        return self._is_in_season(TimeType.SUMMER)

    @property
    def is_autumn(self) -> bool:
        """Return whether the given date is in autumn on the given hemisphere"""

        return self._is_in_season(TimeType.AUTUMN)

    @property
    def is_winter(self) -> bool:
        """Return whether the given date is in winter on the given hemisphere"""

        return self._is_in_season(TimeType.WINTER)


class TropicalMapping(LocationDependentMapping):
    """Mapping for seasons based on tropical areas"""

    __northern_mapping__ = {
        (11, 12, 1, 2, 3, 4): TimeType.DRY_SEASON,  # Nov - Apr
        (5, 6, 7, 8, 9, 10): TimeType.WET_SEASON,  # May - Oct
    }

    __southern_mapping__ = {
        (11, 12, 1, 2, 3, 4): TimeType.WET_SEASON,  # Nov - Apr
        (5, 6, 7, 8, 9, 10): TimeType.DRY_SEASON,  # May - Oct
    }

    @property
    def is_wet_season(self):
        """Return whether the given date is in the wet season"""

        return self._is_in_season(TimeType.WET_SEASON)

    @property
    def is_dry_season(self):
        """Return whether the given date is in the dry season"""

        return self._is_in_season(TimeType.DRY_SEASON)


class SeasonInfo(LocationBasedInfoBase):
    __mapping__ = {}

    def __init__(self, date: datetime, hemisphere: Hemisphere,
                 season_type: SeasonType = SeasonType.GREGORIAN):
        self.season_type = season_type
        super().__init__(date, hemisphere)
        self._setup_properties()

    def _setup_properties(self):
        def predicate(prop):
            return inspect.ismemberdescriptor and isinstance(prop, property)

        properties = inspect.getmembers(self._mapping_class, predicate)

        for (name, _) in properties:
            setattr(self, name, getattr(self._mapping_object, name))

        self.__mapping__.update(self._mapping_object.mapping)

    @property
    def _mapping_object(self) -> Mapping:
        kwargs = self._init_kwargs(self._mapping_class)
        return self._mapping_class(**kwargs)

    @property
    def _mapping_class(self) -> Type:
        mapping_class_name = '{}Mapping'.format(self.season_type.value.capitalize())
        return getattr(sys.modules[__name__], mapping_class_name)

    def _init_kwargs(self, cls: Type) -> Dict[str, Union[datetime, Hemisphere]]:
        args = inspect.getfullargspec(cls.__init__).args
        return {arg: self.__getattribute__(arg) for arg in args if arg != 'self'}

    @property
    def types(self) -> Set[TimeType]:
        """Return a set of fitting time types for the given datetime"""

        if not self._types:
            month = self.date.month

            for month_range, time_type in self._mapping_object.mapping.items():
                if month in month_range:
                    self._types.add(time_type)

        return self._types


def season_info(date: datetime, hemisphere: Hemisphere,
                season_type: SeasonType = SeasonType.GREGORIAN) -> SeasonInfo:
    return SeasonInfo(date, hemisphere, season_type)
