import sys
sys.stdout = sys.stderr

import atexit
import os
import cherrypy
import json
import Game

cherrypy.config.update({'environment': 'embedded'})

if cherrypy.__version__.startswith('3.0') and cherrypy.engine.state == 0:
    cherrypy.engine.start(blocking=False)
    atexit.register(cherrypy.engine.stop)

class Root(object):

    game = Game.Game()
    def obj_dict(self,obj):
        return obj.__dict__

    def index(self):
        return 'Hello World!'
    index.exposed = True

    def students(self):
        return open('/var/www/public/students.html')
    students.exposed = True

    def getStudents(self):
        return json.dumps(self.game.students,default=self.obj_dict)
    getStudents.exposed = True

conf = {
     '/': {
         'tools.sessions.on': True,
         'tools.staticdir.root': '/var/www'
     },
     '/static': {
         'tools.staticdir.on': True,
         'tools.staticdir.dir': './public'
     }
 }
application = cherrypy.Application(Root(), script_name='', config=conf)