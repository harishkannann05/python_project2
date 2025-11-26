# Student Information Management
```
        id=input("Enter Student ID: ")
        if id in student_ids:
        print("Student ID already exists. Cannot add student.")
        return
        name=input("Enter Student Name: ")
        age=input("Enter Student Age: ")
        course=input(f"Enter Course {courses}: ")
        marks=float(input("Enter Marks: "))
        if course not in courses:
        print("Invalid course. Student not added.")
        return
        students[id]={"Name":name,"Age":age,"Course":course, "Marks":marks}
        student_ids.add(id)
        print("Student added successfully.")

```
### Output:
![Output 1](<Screenshot 2025-11-26 160639.png>)
![Output 2](<Screenshot 2025-11-26 160706.png>)
![Output 3](<Screenshot 2025-11-26 160724.png>)