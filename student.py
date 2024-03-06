from course import LabCourse

class Student:
    #Represents a student with their course enrollments and completions.
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []  # Tracks courses the student is currently enrolled in.
        self.completed_courses = []  # Tracks courses the student has completed.
        self.lab_safety_certificate = None  # None indicates unknown certification status.

    def is_lab_safety_certified(self):
        #Checks if the student has lab safety certification.
        return self.lab_safety_certificate

    def certify_lab_safety(self, status=True):
        #Certifies the student for lab safety based on the status provided."""
        self.lab_safety_certificate = status
        if status:
            print(f"{self.name} is now certified for lab safety.")

    def enroll_in_course(self, course):
        #Attempts to enroll the student in a course, checking for capacity, prerequisites, and lab safety certification.
        if course in self.enrolled_courses:
            print(f"{self.name} is already enrolled in {course.title}.")
            return

        if len(course.enrolled_students) >= course.max_capacity:
            print(f"{course.title} is full. Cannot enroll {self.name}.")
            return

        if any(prereq not in self.completed_courses for prereq in course.prerequisites):
            print(f"{self.name} does not meet the prerequisites for {course.title}.")
            return

        if isinstance(course, LabCourse) and course.safety_certification_required and (self.lab_safety_certificate is None or not self.lab_safety_certificate):
            print(f"{self.name} cannot be enrolled in {course.title} without lab safety certification.")
            return

        course.enrolled_students.append(self)
        self.enrolled_courses.append(course)
        print(f"{self.name} successfully enrolled in {course.title}.")

    def list_enrolled_courses(self):
        #Lists all courses the student is currently enrolled in, including detailed schedules.
        if not self.enrolled_courses:
            print(f"{self.name} is not enrolled in any courses.")
        else:
            for course in self.enrolled_courses:
                # Use the correct attribute for location based on the course type
                location = getattr(course, 'lecture_hall', 'TBD') if hasattr(course, 'lecture_hall') else 'TBD'
                location = location if location != 'TBD' else getattr(course, 'lab_requirements', 'TBD') if hasattr(course, 'lab_requirements') else 'TBD'
                print(f"{course.course_code}: {course.title}. Taught by: {course.instructor}. Location: {location}. Schedule: {course.schedule}")

    def add_completed_course(self, course_code):
        #Marks a course as completed, removing it from the enrolled list and adding to the completed list.
        course_to_complete = next((course for course in self.enrolled_courses if course.course_code == course_code), None)

        if course_to_complete:
            self.enrolled_courses.remove(course_to_complete)
            self.completed_courses.append(course_code)
            print(f"{course_code} marked as completed for {self.name}.")
        else:
            print(f"{self.name} has not enrolled in {course_code}, cannot mark as completed.")
