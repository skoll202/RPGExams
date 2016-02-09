'''
Created on Feb 9, 2016

@author: ncarlson
'''

import sys
sys.stdout = sys.stderr

import atexit
import cherrypy

class WebServer(object):
    '''
    classdocs
    '''
    
    
    cherrypy.config.update({'environment': 'embedded'})
    
    if cherrypy.__version__.startswith('3.0') and cherrypy.engine.state == 0:
        cherrypy.engine.start(blocking=False)
        atexit.register(cherrypy.engine.stop)    
    
    def start(self):
        
        class Root(object):
            def index(self):
                return 'Hello World!'
            index.exposed = True
        
        application = cherrypy.Application(Root(), script_name='', config=None)

    def __init__(self, params):
        '''
        Constructor
        '''
        