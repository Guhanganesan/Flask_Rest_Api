from flask_restful import Api
from .Task import Task
from app import app 
#import app instance from app.py

restServer=Api(app)
restServer.add_resource(Task,"/api/v1.0/task")




