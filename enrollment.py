from course import LectureCourse, SeminarCourse, LabCourse
from student import Student

def create_courses():
    courses = [
        LectureCourse("HIST101", "Medieval and Renaissance History", "Prof. Smith", 30, "Falk College", "Mondays - Wednesdays, 10:00-12:00"),
        LectureCourse("CIS623", "Principals of Operating System", "Prof. Joseph W", 25, "Hall of Languages", "Wednesdays - Fridays, 14:00-16:00"),
        LectureCourse("CIS700", "Machine Learning with Graphs", "Prof. Reza Z", 30, "Hall A", "Monday - Wednesday, 09:00-11:00"),
        SeminarCourse("HIST420", "World History: 1900s", "Dr. Johnson", 20, "TBD", "Thursdays, 15:00-18:20"),
        LabCourse("BIO103", "Biology Lab", "Dr. Emily", 15, "Lab 204", "Tuesdays - Thursdays, 13:00-16:00", True),
        LabCourse("CEM649", "Chemistry Lab", "Dr. Walter White", 15, "Lab 101", "Mondays - Wednesdays, 08:00-11:00", True),
    ]
    courses[3].prerequisites.append("HIST101")
    return courses

def find_course(courses, course_code):
    return next((course for course in courses if course.course_code == course_code), None)

def main_cli():
    courses = create_courses()
    students = {}

    while True:
        print("\nWelcome to the Syracuse University Course Registration System")
        print("1. List all courses and schedules")
        print("2. Enroll in a course")
        print("3. List my enrolled courses and schedules")
        print("4. Mark a course as completed")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            for course in courses:
                prerequisites = ", ".join(course.prerequisites) if course.prerequisites else "None"
                lab_safety_msg = ", Lab Safety Certification Required: Yes" if isinstance(course, LabCourse) and course.safety_certification_required else ""
                print(f"{course.course_code}: {course.title} (Prerequisites: {prerequisites}{lab_safety_msg})")
                print(f"    Schedule: {course.schedule} - Available Seats: {course.max_capacity - len(course.enrolled_students)}")

        elif choice == "2":
            student_id = input("Enter your Student ID (SUID): ")
            if student_id not in students:
                student_name = input("Enter your name: ")
                student = Student(student_id, student_name)
                students[student_id] = student
            else:
                student = students[student_id]

            course_code = input("Enter the course code you want to enroll in: ")
            course = find_course(courses, course_code)

            # Check if lab safety certification is needed and ask accordingly
            if isinstance(course, LabCourse) and course.safety_certification_required:
                if student.lab_safety_certificate is None:
                    lab_safety_certified = input("Do you have a lab safety certification? (yes/no): ").strip().lower() == "yes"
                    student.certify_lab_safety() if lab_safety_certified else None

            if course:
                prerequisites = ", ".join(course.prerequisites) if course.prerequisites else "None"
                lab_safety_msg = "Lab Safety Certification Required: Yes" if isinstance(course, LabCourse) and course.safety_certification_required else "No"
                print(f"Enrolling in {course.title} (Prerequisites: {prerequisites}, {lab_safety_msg})")
                student.enroll_in_course(course)
            else:
                print("Course not found.")

        elif choice == "3":
            student_id = input("Enter your student ID: ")
            student = students.get(student_id)
            if student:
                student.list_enrolled_courses()
            else:
                print("Student not found or not enrolled in any courses.")

        elif choice == "4":
            student_id = input("Enter your student ID: ")
            student = students.get(student_id)
            if student:
                course_code = input("Enter the course code you have completed: ")
                student.add_completed_course(course_code)
            else:
                print("Student not found. Please register first.")

        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_cli()
