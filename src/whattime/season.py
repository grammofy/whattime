import inspect
import sys
from abc import ABC, abstractmethod
from datetime import datetime, date
from typing import Set, Dict, Tuple, Type, Union
from warnings import warn

from lazy import lazy as lazy_property

from .base import LocationBasedInfoBase
from .type import Hemisphere, TimeType, SeasonType


class _Interval:
    """Interval class for internal purposes. Supposed to be used in Mapping classes.

    Facilitates defining a comparable date interval by only passing the day and
    month of the start and end date.
    """

    def __init__(self, a: Tuple[int, int], b: Tuple[int, int]):
        # We use the year 4, which is a leap year, in order to be able to allow 29th Feb
        # as date.
        year = 4
        self.start = date(year, a[1], a[0])
        self.end = date(year, b[1], b[0])

    def includes(self, date: date) -> bool:
        """Return whether the given date is in the interval"""

        return self.start <= date <= self.end


# Just so we can use a shorter name when defining an _Interval.
# So, a date interval can be defined by e.g. _I(a=(1, 1), b=(21, 6)).
_I = _Interval


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
        return {v: k for k, v in self.mapping.items()}

    def _is_in_season(self, time_type: TimeType) -> bool:
        date_range = self.inverse_mapping[time_type]

        if all(isinstance(month, int) for month in date_range):
            return self.date.month in date_range
        elif all(isinstance(item, _Interval) for item in date_range):
            return any(self._is_in_interval(interval) for interval in date_range)
        else:
            return False

    def _is_in_interval(self, interval: _Interval) -> bool:
        current_date = self.date.date().replace(year=interval.start.year)
        return interval.includes(current_date)


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


class HinduMapping(Mapping):
    __mapping__ = {
        (_I(a=(15, 3), b=(14, 5)),): TimeType.VASANTA,
        (_I(a=(15, 5), b=(14, 7)),): TimeType.GREESHMA,
        (_I(a=(15, 7), b=(14, 9)),): TimeType.VARSHA,
        (_I(a=(15, 9), b=(14, 11)),): TimeType.SHARAD,
        (_I(a=(15, 11), b=(31, 12)), _I(a=(1, 1), b=(14, 1))): TimeType.HEMANTA,
        (_I(a=(15, 1), b=(14, 3)),): TimeType.SHISHIRA,
    }

    @lazy_property
    def is_vasanta(self):
        """Return whether the given date is in Vasanta (Spring)"""

        return self._is_in_season(TimeType.VASANTA)

    @lazy_property
    def is_greeshma(self):
        """Return whether the given date is in Greeshma (Summer)"""

        return self._is_in_season(TimeType.GREESHMA)

    @lazy_property
    def is_varsha(self):
        """Return whether the given date is in Varsha (Monsoon)"""

        return self._is_in_season(TimeType.VARSHA)

    @lazy_property
    def is_sharad(self):
        """Return whether the given date is in Sharad (Autumn)"""

        return self._is_in_season(TimeType.SHARAD)

    @lazy_property
    def is_hemanta(self):
        """Return whether the given date is in Hemanta (Early Winter)"""

        return self._is_in_season(TimeType.HEMANTA)

    @lazy_property
    def is_shishira(self):
        """Return whether the given date is in Shishira (Prevernal or Late Winter)"""

        return self._is_in_season(TimeType.SHISHIRA)


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
