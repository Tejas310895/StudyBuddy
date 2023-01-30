import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         port=3308,
                                         database='study_bussy',
                                         user='root',
                                         password='')
    cursor = connection.cursor()
except Error as e:
    print("Error while connecting to MySQL", e)
