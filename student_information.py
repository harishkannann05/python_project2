students={}
student_ids=set()
courses=("CSE","CSD","ML","AI","EE","ECE")

def add_student():
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
  
def view_students():
    if not students:
        print("No student records found.")
        return
    print("\n- - - - - Student Records: - - - - - \n")
    for id, info in students.items():
        print(f"ID: {id} -> Name: {info['Name']}, Age: {info['Age']}, Course: {info['Course']}, Marks: {info['Marks']}")

def search_student():
    id=input("Enter Student ID to search: ")
    if id in students:
        info=students[id]
        print(f"Student Found:\n ID: {id} -> Name: {info['Name']}, Age: {info['Age']}, Course: {info['Course']}, Marks: {info['Marks']}")
    else:
        print("Student not found.")
        
def delete_student():
    id=input("Enter Student ID to delete: ")
    if id in students:
        del students[id]
        student_ids.remove(id)
        print("Student deleted successfully.")
    else:
        print("Student not found.")

while True:
    print("\n====== Student Record Management System ======")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Students")
    print("4. Delete Student")
    print("5. Exit")

    choice=input("Enter your choice (1-5): ")

    if choice=='1':
      add_student()
    elif choice=='2':
      view_students()
    elif choice=='3':
      search_student()
    elif choice=='4':
      delete_student()
    elif choice=='5':
      print("Exiting the program. Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")
    
