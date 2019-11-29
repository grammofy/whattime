import inspect
import sys
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Set, Dict, Tuple, Type, Union
from warnings import warn

from lazy import lazy as lazy_property

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
        lazy_property.invalidate(self, 'inverse_mapping')

    @lazy_property
    def inverse_mapping(self) -> Dict[TimeType, Tuple]:
        print("running inverse_mapping lazy-load…")
        return {v: k for k, v in self.mapping.items()}

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

    @lazy_property
    def is_spring(self) -> bool:
        """Return whether the given date is in spring on the given hemisphere"""

        return self._is_in_season(TimeType.SPRING)

    @lazy_property
    def is_summer(self) -> bool:
        """Return whether the given date is in summer on the given hemisphere"""

        return self._is_in_season(TimeType.SUMMER)

    @lazy_property
    def is_autumn(self) -> bool:
        """Return whether the given date is in autumn on the given hemisphere"""

        return self._is_in_season(TimeType.AUTUMN)

    @lazy_property
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

    @lazy_property
    def is_wet_season(self):
        """Return whether the given date is in the wet season"""

        return self._is_in_season(TimeType.WET_SEASON)

    @lazy_property
    def is_dry_season(self):
        """Return whether the given date is in the dry season"""

        return self._is_in_season(TimeType.DRY_SEASON)


class NoongarMapping(Mapping):
    __mapping__ = {
        (12, 1): TimeType.BIRAK,
        (2, 3): TimeType.BUNURU,
        (4, 5): TimeType.DJERAN,
        (6, 7): TimeType.MAKURU,
        (8, 9): TimeType.DJILBA,
        (10, 11): TimeType.KAMBARANG
    }

    @lazy_property
    def is_birak(self):
        """Return whether the given date is in Birak"""

        return self._is_in_season(TimeType.BIRAK)

    @lazy_property
    def is_bunuru(self):
        """Return whether the given date is in Bunuru"""

        return self._is_in_season(TimeType.BUNURU)

    @lazy_property
    def is_djeran(self):
        """Return whether the given date is in Djeran"""

        return self._is_in_season(TimeType.DJERAN)

    @lazy_property
    def is_makuru(self):
        """Return whether the given date is in Makuru"""

        return self._is_in_season(TimeType.MAKURU)

    @lazy_property
    def is_djilba(self):
        """Return whether the given date is in Djilba"""

        return self._is_in_season(TimeType.DJILBA)

    @lazy_property
    def is_kambarang(self):
        """Return whether the given date is in Kambarang"""

        return self._is_in_season(TimeType.KAMBARANG)


class CreeMapping(Mapping):
    __mapping__ = {
        (1, 2): TimeType.PIPON,
        (3, 4): TimeType.SEKWUN,
        (5, 6): TimeType.MITHOSKUMIN,
        (7, 8): TimeType.NEPIN,
        (9, 10): TimeType.TUKWAKIN,
        (11, 12): TimeType.MIKISKAW
    }

    @lazy_property
    def is_pipon(self):
        """Return whether the given date is in Pipon (Winter)"""

        return self._is_in_season(TimeType.PIPON)

    @lazy_property
    def is_sekwun(self):
        """Return whether the given date is in Sekwun (Break-up)"""

        return self._is_in_season(TimeType.SEKWUN)

    @lazy_property
    def is_mithoskumin(self):
        """Return whether the given date is in Mithoskumin (Spring)"""

        return self._is_in_season(TimeType.MITHOSKUMIN)

    @lazy_property
    def is_nepin(self):
        """Return whether the given date is in Nepin (Summer)"""

        return self._is_in_season(TimeType.NEPIN)

    @lazy_property
    def is_tukwakin(self):
        """Return whether the given date is in Tukwakin (Autumn)"""

        return self._is_in_season(TimeType.TUKWAKIN)

    @lazy_property
    def is_mikiskaw(self):
        """Return whether the given date is in Mikiskaw (Freeze-up)"""

        return self._is_in_season(TimeType.MIKISKAW)


class SeasonInfo(LocationBasedInfoBase):
    def __init__(self, date: datetime,
                 season_type: SeasonType = SeasonType.GREGORIAN,
                 hemisphere: Hemisphere = None):
        self.season_type = season_type
        super().__init__(date, hemisphere)
        self._setup_properties()

    def _setup_properties(self):
        mapping_object = self._mapping_object
        is_location_dependent = isinstance(mapping_object, LocationDependentMapping)
        is_hemisphere_available = isinstance(self.hemisphere, Hemisphere)

        if is_location_dependent and not is_hemisphere_available:
            message = "The hemisphere must be set when using SeasonType {}."
            raise ValueError(message.format(self.season_type))

        if not is_location_dependent and is_hemisphere_available:
            message = "Setting the hemisphere has no effect when using SeasonType {}."
            warn(message.format(self.season_type))

        def predicate(prop):
            return inspect.isdatadescriptor and isinstance(prop, lazy_property)

        properties = inspect.getmembers(self._mapping_class, predicate)

        for (name, _) in properties:
            setattr(self, name, getattr(mapping_object, name))

    @lazy_property
    def __mapping__(self) -> Dict[Union[str, Tuple], TimeType]:
        return self._mapping_object.mapping

    @lazy_property
    def _mapping_object(self) -> Mapping:
        kwargs = self._init_kwargs(self._mapping_class)
        return self._mapping_class(**kwargs)

    @lazy_property
    def _mapping_class(self) -> Mapping:
        mapping_class_name = '{}Mapping'.format(self.season_type.value.capitalize())
        return getattr(sys.modules[__name__], mapping_class_name)

    def _init_kwargs(self, cls: Type) -> Dict[str, Union[datetime, Hemisphere]]:
        args = inspect.getfullargspec(cls.__init__).args
        return {arg: self.__getattribute__(arg) for arg in args if arg != 'self'}

    @lazy_property
    def types(self) -> Set[TimeType]:
        """Return a set of fitting time types for the given datetime"""

        if not self._types:
            month = self.date.month

            for month_range, time_type in self._mapping_object.mapping.items():
                if month in month_range:
                    self._types.add(time_type)

        return self._types


def season_info(date: datetime,
                season_type: SeasonType = SeasonType.GREGORIAN,
                hemisphere: Hemisphere = None) -> SeasonInfo:
    return SeasonInfo(date, season_type, hemisphere)
