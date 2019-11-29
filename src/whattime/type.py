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

    # Noongar seasons
    BIRAK = 'birak'
    BUNURU = 'bunuru'
    DJERAN = 'djeran'
    MAKURU = 'makuru'
    DJILBA = 'djilba'
    KAMBARANG = 'kambarang'

    # Cree
    PIPON = 'pipon'
    SEKWUN = 'sekwun'
    MITHOSKUMIN = 'mithoskumin'
    NEPIN = 'nepin'
    TUKWAKIN = 'tukwakin'
    MIKISKAW = 'mikiskaw'

    # Hindu
    VASANTA = 'vasanta'
    GREESHMA = 'greeshma'
    VARSHA = 'varsha'
    SHARAD = 'sharad'
    HEMANTA = 'hemanta'
    SHISHIRA = 'shishira'


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

