class Course:
    #A base class to represent a general course.
    def __init__(self, course_code, title, instructor, max_capacity, schedule="TBD"):
        self.course_code = course_code
        self.title = title
        self.instructor = instructor
        self.max_capacity = max_capacity
        self.enrolled_students = []
        self.prerequisites = []
        self.schedule = schedule  # Provides specific scheduling details

    def enroll_student(self, student):
        #Enroll a student if prerequisites are met and capacity allows.
        if not self.check_available_seats():
            print(f"{self.title} is full.")
            return False
        if not self.check_prerequisites(student):
            print(f"{student.name} does not meet prerequisites for {self.title}.")
            return False
        self.enrolled_students.append(student)
        print(f"{student.name} has been enrolled in {self.title}.")
        return True

    def check_available_seats(self):
        #Check if the course still has seats available.
        return len(self.enrolled_students) < self.max_capacity

    def check_prerequisites(self, student):
        #Verify if the student has completed all necessary prerequisites.
        return all(prereq in student.completed_courses for prereq in self.prerequisites)

    def generate_schedule(self):
        #Generate a detailed schedule for the course.
        return f"Schedule for {self.title}: {self.schedule}. Taught by {self.instructor}. Capacity: {self.max_capacity}."

class LectureCourse(Course):
    #Represents a lecture course, subclass of Course.
    def __init__(self, course_code, title, instructor, max_capacity, lecture_hall, schedule):
        super().__init__(course_code, title, instructor, max_capacity, schedule)
        self.lecture_hall = lecture_hall

    def generate_schedule(self):
        #Generate a lecture-specific schedule.
        return f"{super().generate_schedule()} Lectures will be held in {self.lecture_hall}."

class SeminarCourse(Course):
    #Represents a seminar course, subclass of Course.
    def __init__(self, course_code, title, instructor, max_capacity, seminar_topic, schedule):
        super().__init__(course_code, title, instructor, max_capacity, schedule)
        self.seminar_topic = seminar_topic

    def generate_schedule(self):
        #Generate a seminar-specific schedule.
        return f"{super().generate_schedule()}. Topic: '{self.seminar_topic}'."

class LabCourse(Course):
    #Represents a lab course, subclass of Course.
    def __init__(self, course_code, title, instructor, max_capacity, lab_requirements, schedule, safety_certification_required=True):
        super().__init__(course_code, title, instructor, max_capacity, schedule)
        self.lab_requirements = lab_requirements
        self.safety_certification_required = safety_certification_required

    def enroll_student(self, student):
        #Enroll a student with additional checks for lab safety certification.
        if self.safety_certification_required and not student.is_lab_safety_certified():
            print(f"{student.name} does not have the required lab safety certification for {self.title}.")
            return False
        return super().enroll_student(student)

    def generate_schedule(self):
        #Generate a lab-specific schedule.
        lab_requirements_text = ', '.join(self.lab_requirements) if isinstance(self.lab_requirements, list) else self.lab_requirements
        return f"{super().generate_schedule()} Lab number and requirements: {lab_requirements_text}. Safety certification required: {'Yes' if self.safety_certification_required else 'No'}."
