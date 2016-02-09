'''
Created on Feb 9, 2016

@author: ncarlson
'''

import Courses

class Game(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.students = []
        ################Student Test##################
        student = Courses.Student("Nick","Carlson",1)
        student2 = Courses.Student("Vila","Kongpachith",2)
        self.students.append(student) 
        self.students.append(student2)       
        ##############################################