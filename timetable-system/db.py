import sqlite3
import mysql.connector
from .settings import host, user, password, database
import json
import datetime

import click
from flask import current_app, g
from flask.cli import with_appcontext

# @staticmethod


def get_db(term_value, courses, class_codes):
    db = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database
    )
    mycursor = db.cursor()
    if term_value == "1":
        term = "2019-20 Sem 1"
    else:
        term = "2019-20 Sem 2"
    query = "SELECT DISTINCT term, course_code, class_section, start_time, end_time, course_title, duration, day FROM `19/20 COMP Course Timetable` where term=%s and course_code=%s and class_section=%s"
    for i in range(len(courses)):
        mycursor.execute(query, (term, courses[i], class_codes[i]))
        # print(term, courses[i], class_codes[i])
        myresult = mycursor.fetchall()
        # print(myresult[0][0])
        # myresult:  obj
        formatted_result = []
        for j in range(len(myresult)):
            result = {'term': myresult[j][0], 'course_code': myresult[j][1], 'class_code': myresult[j][2], 'start_time': str(myresult[j][3]), 'end_time': str(myresult[j][4]), 'course_title': myresult[j][5], 'duration': str(myresult[j][6]), 'day': myresult[j][7]}
            load_result = json.dumps(result)
            json_result = json.loads(load_result)
            formatted_result.append(json_result)
        # result = json.dumps(myresult, default=myconverter)
        print(formatted_result)
        return formatted_result