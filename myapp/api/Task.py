from flask_restful import Resource
import logging as logger

import mysql.connector as mysql
from flask import request
import json

db=mysql.connect(host="localhost",
                 user="root",
                 password="1234",
                 database="mydb"
                 )
cursor=db.cursor()

#pip install mysql-connector-python 

class Task(Resource):
    def get(self):
        res=request.args.get("id")
        if res:
            sql = "select * from student where id='{0}'".format(res)
        else:
            sql = "select * from student"
        cursor.execute(sql)
        data=cursor.fetchall()
        data=list(data)
        return data,200
        #return {str(data)},200
    
    def post(self):
        logger.debug("Inside get method")
        res=request.json
        sql = "insert into student(name,email, pass) values('{0}','{1}','{2}')".format(res["name"],res["email"],res["pass"])
        cursor.execute(sql)
        db.commit()
        return {"message":"Successfully Registered"},200
        
    def put(self):
        logger.debug("Inside put method")
        res=request.json
        sql = "update student set name='{1}', email='{2}', pass='{3}' where id='{0}'".format(res["id"],res["name"],res["email"],res["pass"])
        cursor.execute(sql)
        db.commit()        
        return {"message":"Successfully Updated"},200
        
        
    def delete(self):
        logger.debug("Inside delete method")
        res=request.args.get("id") 
        sql = "delete from student where id='{0}'".format(res)
        cursor.execute(sql)
        db.commit()
        return {"message":"Successfully deleted"},200
        
        
