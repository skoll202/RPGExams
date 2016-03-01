'''
Created on Feb 9, 2016

@author: ncarlson
'''

class Question(object):
    '''
    classdocs
    '''
    def __init__(self, idNumber=-1,question="",correctAnswers=[],incorrectAnswers=[]):
        '''
        Constructor
        '''
        self.question = question
        self.correctAnswers = correctAnswers
        self.incorrectAnswers = incorrectAnswers
        
        
class Exam(object):
    '''
    classdocs
    '''
    def __init__(self,questions=[],catagories=[],numQuestions=0,students=[]):
        self.questions = questions
        self.catagories = catagories
        self.numQuestions = numQuestions
        self.students = students
        
        
    
class Objective(object):
    def __init__(self,objectiveID="",description="",questions=[]):
        self.objectiveID=objectiveID
        self.questions=questions
        self.description = description