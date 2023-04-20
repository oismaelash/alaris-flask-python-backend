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


class PlanController():

    def __init__(self):
        self.services = PlanServices()

    def create(self, payload):
        self.services.create(payload)
        return jsonify(payload)

    def readAll(self):
        items = self.services.readAll()
        print(items)
        mydict = CreateDict()

        for item in items:
            mydict.add(item[0], ({"id": item[0], "name": item[1],
                                  "benefits": item[2], "contents": item[3], "value": item[4], "terms": item[5], "featured": item[6]}))

        return mydict.toJson()

    def update(self, id, payload):
        try:
            self.services.update(id, payload)
            return jsonify(payload)
        except Exception as error:
            print(error)
            return error

    def delete(self, id):
        self.services.delete(id)
        return "ok"


class PlanServices():

    def create(self, payload):
        mycursor = mydb.cursor()
        sql = "INSERT INTO alaris.plan (name, benefits, contents, value, terms, featured) VALUES(%s, %s, %s, %s, %s, %s);"
        values = (payload['name'], payload['benefits'],
                  payload['contents'], payload['value'], payload['terms'], payload['featured'])
        mycursor.execute(sql, values)
        mydb.commit()

    def readAll(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM alaris.plan")
        return mycursor.fetchall()

    def update(self, id, payload):
        print(payload)

        mycursor = mydb.cursor()
        sql = "UPDATE alaris.plan SET name=%s, benefits=%s, contents=%s, value=%s, terms=%s, featured=%s WHERE id=%s;"
        values = (payload['name'], payload['benefits'],
                  payload['contents'], payload['value'], payload['terms'], payload['featured'], id)
        mycursor.execute(sql, values)
        mydb.commit()

    def delete(self, id):
        mycursor = mydb.cursor()
        sql = "DELETE FROM alaris.plan WHERE id = %s"
        values = (id,)
        mycursor.execute(sql, values)
        mydb.commit()
