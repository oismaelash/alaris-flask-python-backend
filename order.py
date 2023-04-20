from flask import jsonify
from dotenv import load_dotenv
from util import CreateDict
import mysql.connector
import os

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)


class OrderController():

    def __init__(self):
        self.services = OrderServices()

    def create(self, payload):
        self.services.create(payload)
        return jsonify(payload)

    def readAll(self):
        items = self.services.readAll()
        mydict = CreateDict()

        for item in items:
            mydict.add(item[0], ({"id": item[0], "name": item[1],
                                  "email": item[2], "phone": item[3], "status": item[4]}))

        return mydict.toJson()

    def update(self, id, payload):
        self.services.update(id, payload)
        return jsonify(payload)

    def delete(self, id):
        self.services.delete(id)
        return "ok"


class OrderServices():

    def create(self, payload):
        mycursor = mydb.cursor()
        sql = "INSERT INTO alaris.order (name, email, phone, status) VALUES(%s, %s, %s, 'IN PROGRESS');"
        values = (payload['name'], payload['email'], payload['phone'])
        mycursor.execute(sql, values)
        mydb.commit()

    def readAll(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM alaris.order")
        return mycursor.fetchall()

    def update(self, id, payload):
        print(payload)

        mycursor = mydb.cursor()
        sql = "UPDATE alaris.order SET name=%s, email=%s, phone=%s, status=%s WHERE id=%s;"
        val = (payload['name'], payload['email'],
               payload['phone'], payload['status'], id)
        mycursor.execute(sql, val)
        mydb.commit()

    def delete(self, id):
        mycursor = mydb.cursor()
        sql = "DELETE FROM alaris.order WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
