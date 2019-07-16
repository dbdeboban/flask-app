from flask_restful import Resource
import logging as logger
import sqlite3
from flask import request,render_template
import bcrypt


class User(Resource):

    def get(self):
        

        return {"message": "you used get" },200
    
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        connection = sqlite3.connect('samplelog.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO user(username,password) values(?,?)',(username,hashed))
        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "you used post"},200

    def put(self):
        logger.debug("Inside put method")
        return {"message": "you used put"},200

    def delete(self):
        logger.debug("Inside delete method")
        return {"message": "you used delete"},200