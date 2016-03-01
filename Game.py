'''
Created on Feb 9, 2016

@author: ncarlson
'''

import Courses
import sys
import Exams

class Game(object):
    '''
    classdocs
    '''
    students={}
    courses={}
    objectives={}
    exams={}
    questions={}

    def __init__(self):
        '''
        Constructor
        '''
        self.load()

    def addCourse(self,courseName):
        availableID = 0
        unique=False
        #Check for available course id number
        while not unique:
            test = True
            for c in self.courses.keys():
                if int(c)==availableID:
                    test=False
                    break
            if test==False:
                availableID+=1
            else:
                unique=True
        course = Courses.Course(availableID,courseName)
        course.students={}
        course.objectives={}
        self.courses[availableID]=course
        self.save()
        
    def addObjective(self,objectiveID="",objectiveDescription="",courseID=[]):
        #check to make sure objective ID is unique
        if objectiveID not in self.objectives.keys():
            objective = Exams.Objective(objectiveID,[])
            self.objectives[objectiveID] = objective
            self.objectives[objectiveID].questions=[]
            for c in courseID:
                self.courses[c].addObjective(objective)
        else:
            raise ValueError('ObjectiveID was given that already exists on the database.')
        
    def removeObjective(self,objectiveID):
        for c in self.courses.keys():
            if objectiveID in self.courses[c].objectives:
                self.courses[c].remove(objectiveID)
        if objectiveID in self.objectives.keys():
            self.objectives.pop(objectiveID,None)
            
    def addQuestionToObjective(self,questionID,objectiveID):
        self.objectives[objectiveID].questions.append(questionID)
        
    def addQuestion(self,questionText="",correctAnswers=[],incorrectAnswer=[],objectiveIDs=[]):
        availableID = 0
        unique=False
        #Check for available course id number
        while not unique:
            test = True
            for q in self.questions.keys():
                if int(q)==availableID:
                    test=False
                    break
            if test==False:
                availableID+=1
            else:
                unique=True
        question = Exams.Question(availableID,questionText,correctAnswers,incorrectAnswer)
        
        #add the question ID to the question list of any objective it should be associated with
        for o in objectiveIDs:
            self.objectives[o].questions.append(availableID)
        self.questions[availableID] = question
    
    def removeQuestion(self,questionID):
        self.questions.pop(questionID,None)
        
        #Remove the question ID from any objectives it is associated with
        for o in self.objectives.keys():
            if questionID in self.objectives[o].questions:
                self.objectives[o].questions.remove(questionID)
        
    def removeCourse(self,idNumber):
        for c in self.courses.keys():
            if str(c)==str(idNumber):
                self.courses.pop(c, None)
                break
        self.save()

    def addStudent(self,firstName,lastName):
        availableID = 0
        unique=False
        #Check for available course id number
        while not unique:
            test = True
            for c in self.students.keys():
                if int(c)==availableID:
                    test=False
                    break
            if test==False:
                availableID+=1
            else:
                unique=True
        student = Courses.Student(firstName,lastName,availableID)
        self.students[availableID] = student
        self.save()

    def removeStudent(self,idNumber):
        for s in self.students.keys():
            if str(s)==str(idNumber):
                self.students.pop(s,None)
                break
        for c in self.courses.keys():
            if s in self.courses[c].students.keys():
                self.courses[c].students.pop(s,None)
        self.save()

    def getStudent(self,studentID):
        student = None
        for s in self.students.keys():
            print >> sys.stderr, "*****************Comparing %s with %s" % (str(s),str(studentID))
            if str(s)==str(studentID):
                print >> sys.stderr, "*****************Match.  Student name is %s" % self.students[s].firstName
                student=self.students[s]

        print >> sys.stderr, "*****************Returning student."
        return student

    def getCourse(self,courseID):
        course = None
        for c in self.courses.keys():
            if str(c)==str(courseID):
                course=c
                break
        return course

    def getStudentsFromCourse(self,courseID):
        students = []
        try:
            for s in self.courses[int(courseID)].students.keys():
                students.append(self.students[s])
            return students
        except:
            return []

    def addStudentToCourse(self,studentID,courseID):
        try:
            student = self.students[int(studentID)]
        except:
            pass
        try:
            course = self.courses[int(courseID)]
        except:
            pass
        try:
            course.students[int(studentID)] = student
        except:
            pass
        self.save()

    def removeStudentFromCourse(self,studentID,courseID):
        course = self.courses[int(courseID)]
        course.students.pop(int(studentID),None)
        self.save()

    def save(self):
        #Save student file
        studentFile = open("/home/nc20213/students.txt","w")
        for s in self.students.keys():
            studentFile.write("%s;%s;%s\r\n" % (str(s),self.students[s].lastName,self.students[s].firstName))
        studentFile.close()

        #Save course file
        courseFile = open("/home/nc20213/courses.txt","w")
        for c in self.courses.keys():
            courseFile.write("%s;%s\r\n" % (str(c),self.courses[c].name))
            for s in self.courses[c].students.keys():
                courseFile.write("STUDENT:%s\r\n" % str(s))
        courseFile.close()

    def load(self):
        #Load students
        try:
            studentFile = open("/home/nc20213/students.txt")
            lines = studentFile.readlines()
            for l in lines:
                (studentID,lastName,firstName) = l.split(";")
                firstName = firstName.rstrip()
                self.students[int(studentID)]=Courses.Student(firstName,lastName,int(studentID))
            studentFile.close()
        except:
            pass

        #Load courses
        #try:
        courseFile = open("/home/nc20213/courses.txt")
        lines = courseFile.readlines()
        course = None
        for l in lines:
            if "STUDENT" in l:
                print >> sys.stderr, "*****************Student found"
                (t,studentID) = l.split(":")
                studentID = studentID.rstrip()
                print >> sys.stderr, "*****************Student ID is %s" % studentID
                student = self.getStudent(studentID)
                print >> sys.stderr, "*****************Student data located.  Name is %s" % student.firstName
                if student != None:
                    print >> sys.stderr, "*****************trying to add %s to course %s" % (self.getStudent(studentID).lastName,course.name)
                    course.students[int(studentID)]=student
                    print >> sys.stderr, "*****************adding %s to course %s" % (self.getStudent(studentID).lastName,course.name)
            else:
                (idNumber,name) = l.split(";")
                idNumber=int(idNumber)
                name=name.rstrip()
                course = Courses.Course(idNumber,name)
                course.students={}
                course.objectives={}
                self.courses[idNumber] = course
                print >> sys.stderr, "*****************Changing course to %s" % (name)
        courseFile.close()
        #except:
            #pass