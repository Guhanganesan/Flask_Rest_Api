from flask_restful import Api
#from .Service import Service
from .AngularService import AngularService
from app import app 
#import app instance from app.py

restServer=Api(app)
restServer.add_resource(AngularService,"/api/v1.0/task")