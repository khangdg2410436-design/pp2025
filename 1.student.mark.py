students = []
courses = []
marks = {}     
def input_students():
    n = int(input("Number of students: "))
    for _ in range(n):
        sid = input("Student id: ")
        name = input("Student name: ")
        dob = input("Student DoB: ")
        students.append({"id": sid, "name": name, "dob": dob})
def input_courses():
    n = int(input("Number of courses: "))
    for _ in range(n):
        cid = input("Course id: ")
        name = input("Course name: ")
        courses.append({"id": cid, "name": name})
def input_marks():
    cid = input("Course id to enter marks: ")
    if cid not in [c["id"] for c in courses]:
        print("Course not found.")
        return
    marks[cid] = []
    for s in students:
        score = float(input(f"Mark for {s['id']} {s['name']}: "))
        marks[cid].append((s["id"], score))
def list_students():
    for s in students:
        print(s["id"], s["name"], s["dob"])
def list_courses():
    for c in courses:
        print(c["id"], c["name"])
def show_marks():
    cid = input("Course id: ")
    if cid not in marks:
        print("No marks for this course.")
        return

    for sid, score in marks[cid]:
        name = next(s["name"] for s in students if s["id"] == sid)
        print(sid, name, score)
def main():
    while True:
        print("\n1. Input students")
        print("2. Input courses")
        print("3. Input marks for course")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks for course")
        print("0. Exit")

        ch = input("Choice: ")

        if ch == "1": input_students()
        elif ch == "2": input_courses()
        elif ch == "3": input_marks()
        elif ch == "4": list_students()
        elif ch == "5": list_courses()
        elif ch == "6": show_marks()
        elif ch == "0": break
        else: print("Invalid")


main()
