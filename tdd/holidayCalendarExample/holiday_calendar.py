from collections import deque


class NotWorkingDayRule(object):

    def isNotWorkingDay(self):
        raise NotImplementedError('Must be defined in the subclasses')

    def makeNotWorkingDay(self):
        raise NotImplementedError('Must be defined in the subclasses')


class NotWorkingWeekday(NotWorkingDayRule):
    NOT_WORKING_WEEK_DAYS = [6, 7]
    CUSTOM_NOT_WORKING_WEEK_DAYS = deque()

    @classmethod
    def isNotWorkingDay(cls, dateObj):
        return (dateObj.isoweekday() in cls.NOT_WORKING_WEEK_DAYS
                or dateObj.isoweekday() in cls.CUSTOM_NOT_WORKING_WEEK_DAYS)

    @classmethod
    def makeNotWorkingDay(cls, dateObj):
        isoWeekday = dateObj.isoweekday()
        if (isoWeekday not in cls.CUSTOM_NOT_WORKING_WEEK_DAYS
           and isoWeekday not in cls.NOT_WORKING_WEEK_DAYS):
            cls.CUSTOM_NOT_WORKING_WEEK_DAYS.append(isoWeekday)


class NotWorkingMonthDay(NotWorkingDayRule):
    NOT_WORKING_MONTH_DAYS = deque()

    @classmethod
    def isNotWorkingDay(cls, dateObj):
        return (dateObj.month, dateObj.day) in cls.NOT_WORKING_MONTH_DAYS

    @classmethod
    def makeNotWorkingDay(cls, dateObj):
        monthDayTuple = dateObj.month, dateObj.day
        if monthDayTuple not in cls.NOT_WORKING_MONTH_DAYS:
            cls.NOT_WORKING_MONTH_DAYS.append(monthDayTuple)


class NotWorkingCustomDate(NotWorkingDayRule):
    NOT_WORKING_CUSTOM_DATES = deque()

    @classmethod
    def isNotWorkingDay(cls, dateObj):
        return dateObj in cls.NOT_WORKING_CUSTOM_DATES

    @classmethod
    def makeNotWorkingDay(cls, dateObj):
        if dateObj not in cls.NOT_WORKING_CUSTOM_DATES:
            cls.NOT_WORKING_CUSTOM_DATES.append(dateObj)


class NotWorkingDateInsideRange(NotWorkingDayRule):

    DATE_RANGE = tuple()
    NOT_WORKING_MONTH_DAYS = deque()

    @classmethod
    def isNotWorkingDay(cls, dateObj):
        return (cls.DATE_RANGE[0] <= dateObj <= cls.DATE_RANGE[1]
                and (dateObj.month, dateObj.day) in cls.NOT_WORKING_MONTH_DAYS)

    @classmethod
    def setRange(cls, initDateObj, endDateObj):
        cls.DATE_RANGE = (initDateObj, endDateObj)

    @classmethod
    def makeNotWorkingMonthDay(cls, dateObj):
        monthDayTuple = dateObj.month, dateObj.day
        if monthDayTuple not in cls.NOT_WORKING_MONTH_DAYS:
            cls.NOT_WORKING_MONTH_DAYS.append(monthDayTuple)


class HolidayCalendar(object):

    _NOT_WORKING_DAY_RULES = [
        NotWorkingWeekday,
        NotWorkingMonthDay,
        NotWorkingCustomDate,
        NotWorkingDateInsideRange,
    ]

    @classmethod
    def isNotWorkingDay(cls, dateObj):
        return any(rule.isNotWorkingDay(dateObj) for rule in cls._NOT_WORKING_DAY_RULES)
