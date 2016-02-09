'''
Created on Feb 9, 2016

@author: ncarlson
'''

class Question(object):
    '''
    classdocs
    '''


    def __init__(self, question="",correctAnswers=[],incorrectAnswers=[],catagories=[]):
        '''
        Constructor
        '''
        self.question = question
        self.correctAnswers = correctAnswers
        self.incorrectAnswers = incorrectAnswers
        self.catagories = catagories
        
        
class Exam(object):
    '''
    classdocs
    '''
    
    def __init__(self,questions=[],catagories=[],numQuestions=0,students=[]):
        self.questions = questions
        self.catagories = catagories
        self.numQuestions = numQuestions
        self.students = students
        
        
class Catagory(object):
    '''
    classdocs
    '''
    
    def __init__(self,name=""):
        self.name = name
        self.idNum=self.getID()
        
    def getID(self):
        return 0