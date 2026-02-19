import json

class Student:
    def __init__(self, name, reg_no, mark1, mark2, mark3):
        self.name = name
        self.reg_no = reg_no
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calculate_percentage(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3

    def check_eligibility(self):
        return "Eligible" if self.calculate_percentage() >= 60 else "Not Eligible"

    def to_dict(self):
        return {
            "name": self.name,
            "reg_no": self.reg_no,
            "mark1": self.mark1,
            "mark2": self.mark2,
            "mark3": self.mark3
        }


def save_data(students):
    with open("students.json", "w") as file:
        json.dump([student.to_dict() for student in students], file)


def load_data():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)
            return [Student(**student) for student in data]
    except FileNotFoundError:
        return []


def find_student(students, reg_no):
    for student in students:
        if student.reg_no == reg_no:
            return student
    return None


def main():
    students = load_data()

    while True:
        print("\n===== SUPER Student Placement System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            reg_no = input("Register Number: ")
            mark1 = int(input("Mark 1: "))
            mark2 = int(input("Mark 2: "))
            mark3 = int(input("Mark 3: "))

            student = Student(name, reg_no, mark1, mark2, mark3)
            students.append(student)
            save_data(students)
            print("Student Added & Saved Successfully!")

        elif choice == "2":
            if not students:
                print("No records found.")
            for s in students:
                print("\nName:", s.name)
                print("Register No:", s.reg_no)
                print("Percentage:", round(s.calculate_percentage(), 2))
                print("Status:", s.check_eligibility())

        elif choice == "3":
            reg_no = input("Enter Register Number to search: ")
            student = find_student(students, reg_no)
            if student:
                print("Found:", student.name)
                print("Percentage:", round(student.calculate_percentage(), 2))
                print("Status:", student.check_eligibility())
            else:
                print("Student not found.")

        elif choice == "4":
            reg_no = input("Enter Register Number to delete: ")
            student = find_student(students, reg_no)
            if student:
                students.remove(student)
                save_data(students)
                print("Student Deleted Successfully!")
            else:
                print("Student not found.")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
