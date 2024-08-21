
import csv
import json
out:list = []
with open(r"setup.json") as setup:
    data = json.load(setup)["teacher_file"]
with open(repr(data),"r") as fr:
    teachers = csv.DictReader(fr,fieldnames=["id","name","DOJ"])

    for teacher in teachers:
        if teacher["id"] != "Sno." and teacher["DOJ"] != " ":
            out.append(teacher)

with open(r"D:\Ritankar_work\PythonProjects\InvigilationAssigner\teachers.json","w") as fw:
    json.dump(out,fw)