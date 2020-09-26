# [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]

cal1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
ava1 = ['9:00', '20:00']
cal2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
ava2 = ['10:00', '18:30']
min_meeting_timespan = 30


def _parse_time_string_to_int(time: str):
    hours, minutes = time.split(':', 1)
    if minutes != '00':
        minutes = 100 / (60/int(minutes))

    return int(hours + str(minutes))


def _extract_common_time_constrains(time_contrains: list):
    min_constrain = max_constrain = None
    for time in time_contrains:
        min_individual_constrain, max_individual_constrain = map(_parse_time_string_to_int, time)
        if not min_constrain or min_individual_constrain > min_constrain:
            min_constrain = min_individual_constrain

        if not max_constrain or max_individual_constrain < max_constrain:
            max_constrain = max_individual_constrain

    return min_constrain, max_constrain


def _parse_int_to_minutes(time: int):
    pass


def _generate_common_calendar(time_contrains: tuple,
                              slot_in_min: int):

    min_constrain, max_constrain = time_contrains
    slot_hour_rate = 100 / (60 / slot_in_min)
    return {time_slot: False for time_slot in range(min_constrain,
                                                    max_constrain,
                                                    slot_hour_rate)}


# def _find_available_time_for_calendar(users_calendar: list(list(str)),
#                                       time_contrains: tuple(int),
#                                       slot_in_min: int):

#     common_calendar = _generate_common_calendar(time_contrains, slot_in_min)
#     for meeting in users_calendar:



# def _match_available_time_within_constrains(time_contrains: list(list),
#                                             schedule: )
