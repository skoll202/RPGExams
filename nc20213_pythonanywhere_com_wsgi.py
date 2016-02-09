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

class Root(object):
    
    game = Game.Game()
    
    
    def index(self):
        return 'Hello World!'
    index.exposed = True
    
    def students(self):
        return open('students.html')
    students.exposed = True
    
    def getStudents(self):
        return json.dumps(self.game.students)
    getStudents.exposed = True

application = cherrypy.Application(Root(), script_name='', config=None)