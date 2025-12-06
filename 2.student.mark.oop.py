class Student:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__dob = ""

    def input(self):
        self.__id = input("student ID: ")
        self.__name = input("student Name: ")
        self.__dob = input("student Date of Birth: ")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def list(self):
        print(f"{self.__id} | {self.__name} | {self.__dob}")


class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""

    def input(self):
        self.__id = input("course ID: ")
        self.__name = input("course Name: ")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def list(self):
        print(f"{self.__id} | {self.__name}")


class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}  
    def input_students(self):
        n = int(input("number of students: "))
        for _ in range(n):
            s = Student()
            s.input()
            self.students.append(s)

    def input_courses(self):
        n = int(input("number of courses: "))
        for _ in range(n):
            c = Course()
            c.input()
            self.courses.append(c)

    def input_marks(self):
        cid = input("course ID to input marks for: ")

        if cid not in self.marks:
            self.marks[cid] = {}

        for s in self.students:
            mark = float(input(f"mark of {s.get_name()} ({s.get_id()}): "))
            self.marks[cid][s.get_id()] = mark
    def list_students(self):
        print("\nstudent list:")
        for s in self.students:
            s.list()

    def list_courses(self):
        print("\ncourse list:")
        for c in self.courses:
            c.list()

    def show_marks(self):
        cid = input("course ID to view marks for: ")

        if cid not in self.marks:
            print("no point yet.")
            return

        print("\ncourse marks:")
        for s in self.students:
            sid = s.get_id()
            if sid in self.marks[cid]:
                print(f"{s.get_name()} ({sid}): {self.marks[cid][sid]}")
            else:
                print(f"{s.get_name()} ({sid}): no mark")
    def menu(self):
        while True:
            print("\n--- MENU ---")
            print("1. student input")
            print("2. course input")
            print("3. course mark input")
            print("4. course list")
            print("5. student list")
            print("6. mark list")
            print("0. exit")

            choice = input("choose:")
            if choice == "1": self.input_students()
            elif choice == "2": self.input_courses()
            elif choice == "3": self.input_marks()
            elif choice == "4": self.list_courses()
            elif choice == "5": self.list_students()
            elif choice == "6": self.show_marks()
            elif choice == "0": break
            else: print("404 Not Found.")