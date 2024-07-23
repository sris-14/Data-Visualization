# List of student data
student_list = [
    ["stdid", "stdname", "standard", "age", "hindi", "English", "Maths", "Science", "Computer", "Total"],
    ["std101", "Ashish Kumar", "10th", 15, 67, 89, 87, 89, 90, 422],
    ["std102", "Abhishek Kumar", "10th", 14, 85, 45, 48, 90, 45, 313],
    ["std103", "Aman", "10th", 15, 23, 56, 78, 78, 67, 302],
    ["std104", "Rahul", "10th", 14, 45, 67, 45, 45, 56, 258],
    ["std105", "Ruby", "10th", 13, 89, 67, 89, 93, 65, 403],
    ["std106", "Suman", "10th", 13, 90, 46, 67, 67, 67, 337],
    ["std107", "Saurabh", "10th", 15, 45, 23, 34, 45, 34, 181],
    ["std108", "Sumit", "10th", 14, 23, 45, 67, 78, 90, 303],
    ["std109", "Kamlesh", "10th", 15, 45, 56, 78, 99, 67, 345],
    ["std110", "Rohan", "10th", 15, 34, 12, 24, 45, 56, 171]
]

# Iterate through the list and print each student's details
for student in student_list:
    print(student)
    
print("--------------------------------------------------------")     
#Display the name of student whose marks in English is grater than 50
for x in range(1,len(student_list)):
    if(student_list[x][5]>50):
        print(student_list[x][1])

print("---------------------------------------------------")
#Display Student name and age of top four scorer of maths
#sort the Math score
sorted_Students =sorted(student_list[1:],key=lambda x: x[6], reverse=True)

#get the top four scorers
top_four_scorers = sorted_Students[:4]

#display the name and age of the top four scorers
for student in top_four_scorers:
    print(f"name: {student[1]}, Age: {student[3]}")
        

print("----------------------------------------------------")
#Display name , id ,age of student who are bottom 3 scorer  in computer
#sort the computer scores
sorted_Students =sorted(student_list[1:],key=lambda x: x[8], reverse=True)

#get the bottom three scorers
top_four_scorers = sorted_Students[7:]

#display the id ,name and age of the bottom three scorers
for student in top_four_scorers:
    print(f"id: {student[0]}, name: {student[1]}, Age: {student[3]}")