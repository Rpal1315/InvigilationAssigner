import datetime
import sys
sys.path.append(".")
from assisting import list_dict_search , abbreviate
from helper import reset_teacher_duty
import json
import csv
import random
from alive_progress import alive_bar
from file_change import file_change



start_time = datetime.datetime.now()
# Reset teacher duty
file_change()
reset_teacher_duty()

with open(r"teachers.json") as fteachers, open(r"class.json") as fclass, open(
    r"exams.json"
) as fexams:
    teachers = json.load(fteachers)
    classes = json.load(fclass)
    days = json.load(fexams)

with alive_bar(len(days)) as bar:



    # Max experience calculation
    def max_exp():
        maxm = 0
        c_date = datetime.datetime.now().date()
        for i in teachers:
            doj = datetime.datetime.strptime(i["DOJ"], "%Y-%m-%d").date()
            exp = (c_date - doj).days // 365
            if exp > maxm:
                maxm = exp

        return maxm


    def exp_weight(teacher_id):
        teacher = list_dict_search(teachers, "id", teacher_id)
        exp = (
            datetime.datetime.now().date()
            - datetime.datetime.strptime(teacher["DOJ"], "%Y-%m-%d").date()
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
        """
        Checks if a teacher has sufficient availability to teach on a given day.

        This function checks if the teacher's schedule for two days prior to the given day
        does not conflict with their current workload and if they have at least 999 hours
        of remaining capacity available.

        Args:
            teacher_id (str): The ID of the teacher to check.
            day (int): The day to check availability for.

        Returns:
            bool: True if the teacher has sufficient availability, False otherwise.

        Notes:
            This function assumes that the teacher's schedule is stored in a JSON file
            named "teacher_duty.json" in the same directory as this script.
        """

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
        while True:
            teacher_id = random.choice(teachers)["id"]
            # teacher_id = teacher["id"]
            cls_min = teacher_eligibility(teacher_id)[0]
            cls_max = teacher_eligibility(teacher_id)[1]
            # if cls >= cls_min and cls <= cls_max and teacher_availability(teacher_id, day):
            if teacher_availability(teacher_id, day):
                with open("teacher_duty.json", "r") as f:
                    data = json.load(f)
                data[str(teacher_id)]["days"][int(day) - 1] = 3
                with open("teacher_duty.json", "w") as f:
                    json.dump(data, f)
                return teacher_id


    def main():
        """
        The main function of the Invigilation Assigner program.

        This function reads a list of days, assigns teachers to each day's rooms based on class sizes,
        and then writes out the assignments to CSV files for each day.

        :return: None
        """
        duties = {}
        for day in days:
            duty = {}
            rooms = days[day]
            for room in rooms:
                cls = max(rooms[room])
                teacher = assign_teacher(cls, day)
                
                if teacher is None:
                    continue
                else:
                    duty[room] = abbreviate(list_dict_search(teachers, "id", teacher)['name'])+f'({list_dict_search(teachers, "id", teacher)["id"]})'
            bar()

            duties[day] = duty

            with open(f"duty\{day}.csv", "w") as f:
                d_file=csv.writer(f,lineterminator="\n")
                d_file.writerow(["Day", "Room", "Teacher(ID)"])
                for room in duties[day]:
                    d_file.writerow([day, room, duties[day][room]])

    main()

