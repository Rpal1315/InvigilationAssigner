import json
def reset_teacher_duty():  
    # Read the data from teachers.json
    with open('teachers.json') as f:
        teachers = json.load(f)

    # Create a dictionary to store the data for teacher_duty.json
    teacher_duty = {}

    # Iterate over the teachers and create the data for teacher_duty.json
    for teacher in teachers:
        teacher_id = teacher['id']
        teacher_duty[teacher_id] = {'days': [0, 0, 0, 0, 0, 0, 0, 0]}

    # Write the data to teacher_duty.json
    with open('teacher_duty.json', 'w') as f:
        json.dump(teacher_duty, f, indent=4)