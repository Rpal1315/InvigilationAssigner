
import csv
import json
def file_change():
    out:list = []
    with open(r"setup.json") as setup:
        data = json.load(setup)["teacher_file"]
    with open(data,"r") as fr:
        teachers = csv.DictReader(fr,fieldnames=["id","name","DOJ"])

        for teacher in teachers:
            if teacher["id"] != "Sno." and teacher["DOJ"] != " ":
                out.append(teacher)

    with open(r"teachers.json","w") as fw:
        json.dump(out,fw)
        
if __name__ == "__main__": 
       file_change()
       
       