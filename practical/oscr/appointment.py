from collections import defaultdict

def find_most_appointment_day(days):
    appointments = defaultdict(int)
    most_appointment = (0,0)
    for idx, day in enumerate(days):
        appointments[day] += 1
        if appointments[day] > most_appointment[1]:
            most_appointment = (day, appointments[day])
    return most_appointment[0]


days = [2,3,14,14]

res = find_most_appointment_day(days)
print(res)


def find_most_appointment_day_in_k_range(days, k):
    max_day = max(days)
    appointments = [0 for _ in range(max_day+k)]
    for idx, day in enumerate(days):
        appointments[day-1] += 1
    appointments_in_next_k_days = [0] * k
    for idx, appointment in enumerate(appointments):
        appointments_in_next_k_days.append(sum(appointments[idx:idx+k]))
    print(appointments_in_next_k_days)
    res = []
    for idx in range(max_day):
        res.append(max(appointments_in_next_k_days[idx: idx+2*k]))
    return res



days = [1, 2, 2, 3, 4, 5, 6, 14,14, 15, 20, 30]

res = find_most_appointment_day_in_k_range(days, 3)
print(res)