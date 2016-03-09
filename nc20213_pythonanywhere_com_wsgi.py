import sys
sys.stdout = sys.stderr

import atexit
import cherrypy
import json
import Game

cherrypy.config.update({'environment': 'embedded'})

if cherrypy.__version__.startswith('3.0') and cherrypy.engine.state == 0:
    cherrypy.engine.start(blocking=False)
    atexit.register(cherrypy.engine.stop)

class Root:
    exposed=True
    game = Game.Game()
    def obj_dict(self,obj):
        return obj.__dict__

    def index(self):
        return 'Hello World!'
    index.exposed = True

    def courses(self):
        return open('/var/www/public/courses.html')
    courses.exposed = True

    def objectives(self):
        return open('/var/www/public/objectives.html')
    objectives.exposed = True

    def getObjectives(self):
        return json.dumps(self.game.objectives,default=self.obj_dict)
    getObjectives.exposed = True

    def getQuestions(self):
        return json.dumps(self.game.questions,default=self.obj_dict)
    getQuestions.exposed = True

    def getExams(self):
        return json.dumps(self.game.exams,default=self.obj_dict)
    getExams.exposed = True

    def getStudentsFromCourse(self,courseID):
        students = self.game.getStudentsFromCourse(courseID)
        for s in students:
            print >> sys.stderr, "%s------------------->%s" % (str(courseID),s.lastName)
        return json.dumps(students,default=self.obj_dict)
    getStudentsFromCourse.exposed = True

    def getCourses(self):
        return json.dumps(self.game.courses,default=self.obj_dict)
    getCourses.exposed = True

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def postCourse(self):
        input_json = cherrypy.request.json
        self.game.addCourse(input_json['courseName'])



    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def postObjective(self):
        input_json = cherrypy.request.json
        self.game.addObjective(input_json['objectiveID'],input_json['objectiveDescription'],{})

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def removeObjective(self):
        input_json = cherrypy.request.json
        self.game.removeObjective(input_json['objectiveID'])

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def postQuestionToObjective(self):
        input_json = cherrypy.request.json
        self.game.removeObjective(input_json['questionID'],input_json['objectiveID'])

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def postQuestion(self):
        inputJson = cherrypy.request.json
        self.game.addQuestion(inputJson['questionText'],inputJson['correctAnswers'],inputJson['incorrectAnswers'])

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def removeQuestion(self):
        input_json = cherrypy.request.json
        self.game.removeQuestion(input_json['questionID'])

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def postStudentToCourse(self):
        input_json = cherrypy.request.json
        courseID=input_json['courseID']
        studentID=input_json['studentID']
        self.game.addStudentToCourse(studentID,courseID)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def removeStudentFromCourse(self):
        input_json = cherrypy.request.json
        courseID=input_json['courseID']
        studentID=input_json['studentID']
        self.game.removeStudentFromCourse(studentID,courseID)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def removeCourse(self):
        input_json = cherrypy.request.json
        self.game.removeCourse(input_json['id'])

    @cherrypy.expose
    def GET(self):
        return "Hello"
    def POST(self):
        return "Hello"

class UI(object):
    exposed = True
    def __init__(self,game):
        self.game = game
    def GET(self):
        return open('/var/www/public/students.html')

class Student(object):
    exposed=True
    def obj_dict(self,obj):
        return obj.__dict__

    def __init__(self,game):
        self.game = game

    @cherrypy.tools.json_out()
    def GET(self,id=''):
        returnData = None
        if id=='':
            returnData= json.dumps(self.game.students,default=self.obj_dict)
        else:
            student = self.game.getStudent(id)
            returnData= student.__dict__
        return returnData

    @cherrypy.tools.json_in()
    def POST(self):
        input_json = cherrypy.request.json
        self.game.addStudent(input_json['firstName'],input_json['lastName'])
        return "1"

    def REMOVE(self,id=''):
        if id!='':
            self.game.removeStudent(id)
            return "1"

    def PUT(self):
        pass


class Course(object):
    exposed=True
    def obj_dict(self,obj):
        return obj.__dict__
    def __init__(self,game):
        self.game = game

    @cherrypy.tools.json_out()
    def GET(self,id=""):
        returnData = None
        if id=="":
            returnData= json.dumps(self.game.courses,default=self.obj_dict)
        else:
            returnData=self.obj_dict(self.game.getCourse(id))
        return returnData

    @cherrypy.tools.json_in()
    def POST(self):
        input_json = cherrypy.request.json
        self.game.addCourse(input_json['courseName'])
        return "1"

    def PUT(self):
        pass

    def REMOVE(self,id=''):
        if id!='':
            self.game.removeCourse(id)
            return "1"

class Objective(object):
    exposed=True
    def __init__(self,game):
        self.game = game
    def GET(self,id):
        pass
    def POST(self):
        pass
    def PUT(self):
        pass
    def REMOVE(self):
        pass


class Question(object):
    exposed=True
    def __init__(self,game):
        self.game = game
    def GET(self,id):
        pass
    def POST(self):
        pass
    def PUT(self):
        pass
    def REMOVE(self):
        pass

class Exam(object):
    exposed=True
    def __init__(self,game):
        self.game = game
    def GET(self,id):
        pass
    def POST(self):
        pass
    def PUT(self):
        pass
    def REMOVE(self):
        pass



root=Root()
root.student = Student(root.game)
root.question = Question(root.game)
root.exam = Exam(root.game)
root.objective = Objective(root.game)
root.course = Course(root.game)
root.ui=UI(root.game)



conf = {
     '/': {
         'tools.sessions.on': True,
         'tools.staticdir.root': '/var/www',
         'request.dispatch': cherrypy.dispatch.MethodDispatcher()
     },
     '/static': {
         'tools.staticdir.on': True,
         'tools.staticdir.dir': './public'
     }
 }
application = cherrypy.Application(root, script_name='', config=conf)