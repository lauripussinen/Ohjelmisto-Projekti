import random
import story
from geopy import distance

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='some_database_name', #ei vielä tiedossa
    user='some_user_name', #ei cielä tiedossa
    password='some_password', #ei vielä tiedossa
    autocommit=True
)