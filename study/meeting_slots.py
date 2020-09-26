from collections import deque

# GIVEN THE INPUTS
cal1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
ava1 = ['9:00', '20:00']
cal2 = [['10:00', '11:30'], ['12:30', '14:30'],
        ['14:30', '15:00'], ['16:00', '17:00']]
ava2 = ['10:00', '18:30']
min_meeting_timespan = 30

# EXPECTED ANSWER = [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]


def _calculate_minutes_as_hour_rate(minutes_int) -> int:
    return int(100 / (60/int(minutes_int)))


def _parse_time_string_to_int(time: str) -> int:
    hours, minutes = time.split(':', 1)
    if minutes != '00':
        minutes = _calculate_minutes_as_hour_rate(minutes)

    return int(hours + str(minutes))


def _parse_int_2_time_string(time: int) -> str:
    minutes_digits = time % 100
    hour_rate = int(60 / (100 / minutes_digits)) if minutes_digits else '00'
    return str(time)[:-2] + ':' + str(hour_rate)


def _parse_meeting_str_2_int_tuple(meeting: str) -> map:
    return map(_parse_time_string_to_int, meeting)


def _extract_common_time_constrains(time_contrains: list) -> tuple:
    min_constrain = max_constrain = None
    for availability in time_contrains:
        min_individual_constrain, max_individual_constrain = _parse_meeting_str_2_int_tuple(availability)
        if not min_constrain or min_individual_constrain > min_constrain:
            min_constrain = min_individual_constrain

        if not max_constrain or max_individual_constrain < max_constrain:
            max_constrain = max_individual_constrain

    return min_constrain, max_constrain


def _generate_common_calendar(time_contrains: tuple,
                              slot_in_min: int) -> dict:
    min_constrain, max_constrain = _extract_common_time_constrains(time_contrains)
    slot_hour_rate = _calculate_minutes_as_hour_rate(slot_in_min)
    return {time_slot: True for time_slot in range(min_constrain,
                                                   max_constrain,
                                                   slot_hour_rate)}


def _get_meeting_busy_slots(meeting: list,
                            slot_in_min: int) -> list:
    init_time, end_time = _parse_meeting_str_2_int_tuple(meeting)
    return [slot_init for slot_init in range(init_time,
                                             end_time,
                                             _calculate_minutes_as_hour_rate(slot_in_min))]


def _get_user_calendar_busy_slots(meetings: list,
                                  slot_in_min: int) -> deque:
    busy_slots = deque()
    for m in meetings:
        busy_slots.extend(_get_meeting_busy_slots(m, slot_in_min))

    return busy_slots


def _merge_available_time_slots(common_calendar: dict,
                                slot_in_min: int) -> list:
    available_slots = [slot for slot, availability in common_calendar.items() if availability]
    slot_timespan = _calculate_minutes_as_hour_rate(slot_in_min)

    available_ranges = deque()
    idx = 0
    while idx < len(available_slots):
        slot = available_slots[idx]
        next_slot = slot + slot_timespan
        if next_slot not in available_slots:
            available_ranges.append(list(map(_parse_int_2_time_string, [slot, next_slot])))
        else:
            last_adjacent_slot = next_slot
            while last_adjacent_slot in available_slots:
                last_adjacent_slot += slot_timespan
                idx += 1

            available_ranges.append(list(map(_parse_int_2_time_string, [slot, last_adjacent_slot])))

        idx += 1

    return list(available_ranges)


def _find_available_time_for_calendars(users_calendar: list,
                                       time_contrains: tuple,
                                       slot_in_min: int) -> list:
    common_calendar = _generate_common_calendar(time_contrains, slot_in_min)
    for user_cal in users_calendar:
        busy_slots = _get_user_calendar_busy_slots(user_cal, slot_in_min)
        for slot in busy_slots:
            common_calendar[slot] = False

    return _merge_available_time_slots(common_calendar, slot_in_min)


def main():
    print(_find_available_time_for_calendars([cal1, cal2],
                                             [ava1, ava2],
                                             min_meeting_timespan))


if __name__ == '__main__':
    main()
