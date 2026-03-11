import mysql.connector
import random

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwordd="Deva1965",
    database="flight_game"
)

cursor = db.cursor(dictionary=True)