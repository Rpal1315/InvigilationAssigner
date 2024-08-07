import datetime
from assisting import list_dict_search

import json

with open("teachers.json") as fteachers, open("class.json") as fclass, open(
    "exams.json"
) as fexams:
    teachers = json.load(fteachers)
    classes = json.load(fclass)
    days = json.load(fexams)


# Create a program that assigns duty to each teacher in a class during the exam.
# Conditions:
# 1. A teacher must not have two consecutive days of duty.
# 2. A teacher of lesser experience will have lower class(like 6 or 7) with more hours.
# 3. A teacher of higher experience will have higher class(like 11 or 12) with less hours.
# Use teacher.json , class.json and exams.json as input.

# Start with the first day of the exam

# Determine class to be assigned to the teacher


# Max experience calculation
def max_exp():
    maxm = 0
    c_date = datetime.datetime.now().date()
    for i in teachers:
        doj = datetime.datetime.strptime(i["DOJ"], "%d-%m-%Y").date()
        exp = (c_date - doj).days // 365
        if exp > maxm:
            maxm = exp

    return maxm


def exp_weight(teacher_id):
    teacher = list_dict_search(teachers, "id", teacher_id)
    exp = (
        datetime.datetime.now().date()
        - datetime.datetime.strptime(teacher["DOJ"], "%d-%m-%Y").date()
    ).days // 365
    return (exp / max_exp(), exp)


def teacher_eligibility(teacher_id):
    if exp_weight(teacher_id)[0] <= 0.33:
        eligib = (6, 8)
    elif exp_weight(teacher_id)[0] <= 0.66:
        eligib = (9, 10)
    elif exp_weight(teacher_id)[0] <= 1:
        eligib = (11, 12)

    return eligib


def teacher_availability(teacher_id, day):
    with open("teacher_duty.json") as fteacher_duty:
        teacher_duty = json.load(fteacher_duty)
    if len(teacher_duty[str(teacher_id)]["days"]) > 1:
        if (
            teacher_duty[str(teacher_id)]["days"][(int(day) - 2)] == 0 and
            teacher_duty[str(teacher_id)]["days"][(int(day) - 1)] < 3
            and sum(teacher_duty[str(teacher_id)]["days"]) < 1000
        ):
            return True
        else:
            return False
    else:
        return True


def assign_teacher(cls, day):
    for teacher in teachers:
        teacher_id = teacher["id"]
        cls_min = teacher_eligibility(teacher_id)[0]
        cls_max = teacher_eligibility(teacher_id)[1]
        if cls >= cls_min and cls <= cls_max:
            if teacher_availability(teacher_id, day):
                with open("teacher_duty.json", "r") as f:
                    data = json.load(f)
                data[str(teacher_id)]["days"][int(day) - 1] = 3
                with open("teacher_duty.json", "w") as f:
                    json.dump(data, f)
                return teacher_id


def main():
    duties = {}
    for day in days:
        duty = {}
        rooms = days[day]
        for room in rooms:
            cls = max(rooms[room])
            teacher = assign_teacher(cls, day)
            print(teacher)
            if teacher is None:
                continue
            else:
                duty[room] = list_dict_search(teachers, "id", teacher)['name']

        duties[day] = duty

    with open("duty.json", "w") as f:
        json.dump(duties, f, indent=4)

main()