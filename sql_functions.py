#!usr/bin/env python3

import sqlite3
from sqlite3 import Error

def sql_connection():
	try:
		conn = sqlite3.connect('my_data.db')
		return conn
	except Error:
		print(Error)

def make_sql_table(conn):
    print("Creating db")
    cursor_object = conn.cursor()

    result = cursor_object.execute("CREATE TABLE Temperatures(location_temperatures, values)")
    #result = cursor_object.execute("SELECT * FROM Temperatures")

    printable_output = result.fetchall()
    print(printable_output)

def insert_temperatures(conn, list_of_temps):
    print(list_of_temps)
    cursor_object = conn.cursor()
    result = cursor_object.execute("INSERT INTO Temperatures(list_of_temps)", (list_of_temps))
    printable_output = result.fetchall()
    print(printable_output)

def save_content(list_of_temps):
#sql_connection()
    print("Save content running")
    conn = sql_connection()
    make_sql_table(conn)
    insert_temperatures(conn, list_of_temps)

    return 0
