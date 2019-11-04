#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
from datetime import datetime, timedelta
from typing import NamedTuple

import pytest


@pytest.fixture(scope='session')
def now() -> datetime:
    return datetime.utcnow()


@pytest.fixture
def today_noon(now: datetime) -> datetime:
    return now.replace(hour=12, minute=0, second=0, microsecond=0)


@pytest.fixture
def monday(today_noon: datetime) -> datetime:
    return today_noon - timedelta(days=today_noon.weekday())


@pytest.fixture
def southern_winter_monday(today_noon: datetime) -> datetime:
    return datetime(year=2020, month=8, day=3)


@pytest.fixture
def week(monday: datetime) -> NamedTuple:
    days = {date.strftime("%A").lower(): date for date in
            (monday + timedelta(days=n) for n in range(0, 7))}
    Week = namedtuple('Week', days.keys())

    return Week(**days)


@pytest.fixture
def months(now: datetime) -> NamedTuple:
    months = {date.strftime("%B").lower(): date for date in
              (now.replace(month=n) for n in range(1, 13))}
    Months = namedtuple('Months', months.keys())

    return Months(**months)
