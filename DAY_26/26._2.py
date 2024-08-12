# ==================== DICTIONARY COMPREHENSION ==================== #
# new_dict={new_key:new_value for item in list}
# new_dict = {new_key:new_value for {key,value} in dict.item() if test}
import random
names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

students_socre={student:random.randint(1,100)for student in names}
# print(students_socre)

passed_student={student:score for (student,score) in students_socre.items() if score>=60}
# print(passed_student)

# How to itereate over pandas DataFrames

student_dict={
    "student":["Anglena","James","Lily"],
    "score":[56,76,98]
}

# for (key,value) in student_dict.items():
#     print(key,value)

import pandas
student_data_frames = pandas.DataFrame(student_dict)
# print(student_data_frames)

# Loop through row in a data frames

for (index,row) in student_data_frames.iterrows():
    # print(index,row)
    print(row.student)
    if row.student =="Anglena":
        print(row.score)



