'''
Created on Feb 9, 2016

@author: ncarlson
'''

class Student(object):
    '''
    classdocs
    '''


    def __init__(self, firstName = "",lastName="",studentID=-1):
        '''
        Constructor
        '''
        self.firstName = firstName
        self.lastName = lastName
        if studentID==-1:
            self.studentID=self.getStudentID()
        else:
            self.studentID=studentID

    def getStudentID(self):
        return self.studentID




class Course(object):
    '''
    classdocs
    '''
    def __init__(self,idNumber=-1,name='',students={}):
        self.idNumber=idNumber
        self.name = name
        self.students = students
        self.objectives=[]
        
    def addObjective(self,objective):
        self.objectives.append(objective.objectiveID)








