from enum import Enum


class TimeType(Enum):
    WEEKEND = 'weekend'
    WEEKDAY = 'weekday'

    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'

    MORNING = 'morning'
    MIDMORNING = 'midmorning'
    NOON = 'noon'
    AFTERNOON = 'afternoon'
    EVENING = 'evening'
    NIGHT = 'night'

    # Gregorian seasons
    SPRING = 'spring'
    SUMMER = 'summer'
    AUTUMN = 'autumn'
    WINTER = 'winter'

    # Tropical seasons
    WET_SEASON = 'wet season'
    DRY_SEASON = 'dry season'


class Hemisphere(Enum):
    NORTHERN = 'northern'
    SOUTHERN = 'southern'


class SeasonType(Enum):
    GREGORIAN = 'gregorian'
    TROPICAL = 'tropical'
    HINDU = 'hindu'
    BENGALI = 'bengali'
    TAMIL = 'tamil'
    THAI = 'thai'
    NOONGAR = 'noongar'
    CREE = 'cree'

