class Student:
    def __init__(self, name, reg_no, mark1, mark2, mark3):
        self.name = name
        self.reg_no = reg_no
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calculate_percentage(self):
        total = self.mark1 + self.mark2 + self.mark3
        return total / 3

    def check_eligibility(self):
        percentage = self.calculate_percentage()
        if percentage >= 60:
            return "Eligible for Placement"
        else:
            return "Not Eligible for Placement"

    def display_details(self):
        print("\n----- Student Details -----")
        print("Name:", self.name)
        print("Register Number:", self.reg_no)
        print("Percentage:", round(self.calculate_percentage(),2)1)
        print("Placement Status:", self.check_eligibility())


def main():
    print("===== Student Placement Management System =====")

    students = []

    while True:
        print("\n1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Student Name: ")
            reg_no = input("Enter Register Number: ")
            mark1 = int(input("Enter Mark 1: "))
            mark2 = int(input("Enter Mark 2: "))
            mark3 = int(input("Enter Mark 3: "))

            student = Student(name, reg_no, mark1, mark2, mark3)
            students.append(student)

            print("Student Added Successfully!")

        elif choice == "2":
            if not students:
                print("No student records found.")
            else:
                for student in students:
                    student.display_details()

        elif choice == "3":
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice! Try Again.")


if __name__ == "__main__":
    main()
