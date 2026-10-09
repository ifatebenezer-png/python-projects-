students = []
def add_student():

    print("\n========== ADD STUDENT ==========")

    name = input("Enter Student Name : ").strip()
    roll = input("Enter Roll Number  : ").strip()

    # Check duplicate roll number
    for student in students:
        if student["roll"] == roll:
            print("❌ Roll Number Already Exists")
            return

    try:
        marks = float(input("Enter Student Marks : "))
    except ValueError:
        print("❌ Invalid Marks")
        return

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)

    print("✅ Student Added Successfully")
def view_students():

    print("\n========== STUDENT RECORDS ==========")

    if len(students) == 0:
        print("❌ No Student Records Found")
        return

    print(
        f"{'Roll No':<15}"
        f"{'Name':<25}"
        f"{'Marks':<10}"
    )

    print("-" * 50)

    for student in students:

        print(
            f"{student['roll']:<15}"
            f"{student['name']:<25}"
            f"{student['marks']:<10}"
        )


# =========================================
# SEARCH STUDENT
# =========================================
def search_student():

    print("\n========== SEARCH STUDENT ==========")

    roll = input("Enter Roll Number : ").strip()

    found = False

    for student in students:

        if student["roll"] == roll:

            print("\n✅ Student Found")
            print("-----------------------------")
            print("Name  :", student["name"])
            print("Roll  :", student["roll"])
            print("Marks :", student["marks"])

            found = True
            break

    if not found:
        print("❌ Student Not Found")



def delete_student():

    print("\n========== DELETE STUDENT ==========")

    roll = input("Enter Roll Number : ").strip()

    found = False

    for student in students:

        if student["roll"] == roll:

            students.remove(student)

            print("✅ Student Deleted Successfully")

            found = True
            break

    if not found:
        print("❌ Student Not Found")



def update_student():

    print("\n========== UPDATE STUDENT ==========")

    roll = input("Enter Roll Number : ").strip()

    found = False

    for student in students:

        if student["roll"] == roll:

            print("\nStudent Found")

            new_name = input("Enter New Name : ").strip()

            try:
                new_marks = float(input("Enter New Marks : "))
            except ValueError:
                print("❌ Invalid Marks")
                return

            student["name"] = new_name
            student["marks"] = new_marks

            print("✅ Student Updated Successfully")

            found = True
            break

    if not found:
        print("❌ Student Not Found")



while True:

    print("\n")
    print("===================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("===================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("\nEnter Your Choice : ").strip()

 

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        update_student()

    elif choice == "6":
        print("\n✅ Program Closed")
        break

    else:
        print("\n❌ Invalid Choice")
