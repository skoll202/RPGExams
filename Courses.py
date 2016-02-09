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
        return 0
    
    
    
    
class Course(object):
    '''
    classdocs
    '''
    
    def __init__(self,name='',students=[]):
        self.name = name
        self.students = students