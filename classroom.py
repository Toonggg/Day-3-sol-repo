class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def full_name(self):
        print("Name is: %s %s" % (self.firstname, self.lastname))
    

class Student(Person):
    def __init__(self, firstname, lastname, subjectname):
        Person.__init__(self, firstname, lastname)
        self.subjectname = subjectname
    def full_name_subject_name(self):
        print("Name is: %s %s" % (self.firstname, self.lastname))
        print("%s %s is taking: %s" % (self.firstname, self.lastname, self.subjectname))

class Teacher(Person):
    def __init__(self, firstname, lastname, coursename):
        Person.__init__(self, firstname, lastname)
        self.coursename = coursename
    def teacher_name_course_name(self):
        print("Teacher is: %s %s" % (self.firstname, self.lastname))
        print("%s %s is teaching: %s" % (self.firstname, self.lastname, self.coursename))

