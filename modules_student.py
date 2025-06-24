name=input("Enter Student Name:")
marks=input("Enter marks :")

import student_info
grade=(student_info.get_grade(marks))
pass_fail=(student_info.is_pass(marks))



print("Result")
print("Student Name :",name)
print("Marks:",marks)
print("Grade:",grade)
print("pass" if pass_fail else "fail")
