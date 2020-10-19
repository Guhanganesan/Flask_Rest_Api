from flask_restful import Api
from .service import Service
from app import app 
#import app instance from app.py

restServer=Api(app)
restServer.add_resource(Service,"/api/v1.0/task")
