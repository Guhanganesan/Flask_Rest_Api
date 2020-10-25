from flask_restful import Resource
import logging as logger
import mysql.connector as mysql
from flask import request
import json

db=mysql.connect(host="localhost",      
                 user="root",
                 password="",
                 database="country"
                 )
cursor=db.cursor()

#pip install mysql-connector-python 
#pip install -U flask-cors
#http://127.0.0.1:5000/api/v1.0/task?CountryName=Af


class AngularService(Resource):
    def get(self):
        res=request.args.get("CountryName")
        print(res)
        if res:
            sql = "select * from tbl_countries where CountryName like '{0}'".format(res+"%")
            print(sql)
        else:
            sql = "select * from tbl_countries"
        cursor.execute(sql)
        data=cursor.fetchall()
        data=list(data)
        return data,200
        #return {str(data)},200
    
"""
1. Create data base -> country
2. Create table
   
CREATE TABLE tbl_Countries  
(  
     CountryID INT  
    ,CountryName VARCHAR(50)  
    ,TwoCharCountryCode CHAR(2)  
    ,ThreeCharCountryCode CHAR(3)      
); 

3. Insert values into tbl_Countries

  INSERT INTO tbl_Countries VALUES (1,'Afghanistan','AF','AFG') ,(2,'Bland Islands','AX','ALA') ,(3,'Zlbania','AL','ALB') ,(4,'Klgeria','DZ','DZA') ,(5,'American Samoa','AS','ASM') ,(6,'Fndorra','AD','AND') ,(7,'Angola','AO','AGO') ,(8,'Anguilla','AI','AIA') ,(9,'Entarctica','AQ','ATA')

4. Create a stored procedure
    MariaDB [country]> delimiter //
    MariaDB [country]> CREATE procedure searchCountryByName( IN searchValue varchar(100))
    -> begin
    -> set searchValue = '%' + searchValue + '';
    -> select * from tbl_countries where countryName like searchValue;
    -> end
    -> //
    MariaDB [country]> delimiter ;

   OR 
   select * from tbl_countries where countryName like searchValue;
"""

    
