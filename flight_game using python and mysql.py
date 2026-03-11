import mysql.connector
import random

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Deva1965",
    database="flight_game"
)

cursor = db.cursor(dictionary=True)

def start_game():
    print("Welcome to flight game")
    screen_name = input("Enter your username: ")
    print(f"Hello captain {screen_name}! Welcome to the flight game! ")
    print(f"{screen_name}, we need to make an eco-friendly machine and we need to visit 10 new airports.")
    print("Captain, the fuel will be limited. So, think wisely before giving a step and there is no undo button!")

    co2_budget = 10000
    current_location = 'EFHK'
    visited_airports = set()

    required_parts = ["Electric Motor", "Battery", "Air Filter", "Propeller", "Solar Panel"]
    collected_parts = []

start_game()