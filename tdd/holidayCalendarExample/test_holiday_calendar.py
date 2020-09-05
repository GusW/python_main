from unittest import TestCase
import holiday_calendar as hc
from datetime import date


class HolidayCalendarTest(TestCase):

    def test_checkDateIsNotWorkingDate(self):
        aSunday = date(2020, 8, 30)
        self.assertTrue(hc.HolidayCalendar.isNotWorkingDay(aSunday))

        aSartuday = date(2020, 8, 29)
        self.assertTrue(hc.HolidayCalendar.isNotWorkingDay(aSartuday))

        aMonday = date(2020, 8, 31)
        self.assertFalse(hc.HolidayCalendar.isNotWorkingDay(aMonday))

    def test_checkNewCustomWeekdayIsNotWorkingDate(self):
        aMonday = date(2020, 8, 31)
        hc.NotWorkingWeekday.makeNotWorkingDay(aMonday)
        self.assertTrue(hc.HolidayCalendar.isNotWorkingDay(aMonday))

    def test_checkHolidayIsNoWorkingDate(self):
        aXmas = date(2019, 12, 25)
        hc.NotWorkingMonthDay.makeNotWorkingDay(aXmas)
        self.assertTrue(hc.HolidayCalendar.isNotWorkingDay(aXmas))
        aNewYr = date(1901, 1, 1)
        hc.NotWorkingMonthDay.makeNotWorkingDay(aNewYr)
        self.assertTrue(hc.HolidayCalendar.isNotWorkingDay(aNewYr))

    def test_checkCustomDateIsNoWorkingDate(self):
        randomDate = date(2020, 12, 8)
        hc.NotWorkingCustomDate.makeNotWorkingDay(randomDate)
        self.assertTrue(hc.HolidayCalendar.isNotWorkingDay(randomDate))

    def test_checkCustomDateInRangeisNotWorkingDate(self):
        rangeInit = date(2020, 1, 1)
        rangeEnd = date(2020, 12, 31)
        hc.NotWorkingDateInsideRange.setRange(rangeInit, rangeEnd)

        randomDateInsideRange = date(2020, 9, 9)
        hc.NotWorkingDateInsideRange.makeNotWorkingMonthDay(
            randomDateInsideRange)
        self.assertTrue(hc.HolidayCalendar.isNotWorkingDay(randomDateInsideRange))

        randomDateOutsideRange = date(2021, 9, 9)
        self.assertFalse(hc.HolidayCalendar.isNotWorkingDay(
            randomDateOutsideRange))
