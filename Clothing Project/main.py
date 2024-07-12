import requests
import json
import sqlite3
from Men_hoodies import data_Mens_Hoodies
from Men_pants import data_Mens_Pants
from Men_shoes import data_Mens_Shoes
from Women_hoodies import data_Women_Hoodies
from Women_pants import data_Women_Pants
from Women_shoes import data_Womens_Shoes

def insert_shoes(name, brand, category, gender, price, Website):
    conn = sqlite3.connect('Clothes_Project.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO Shoes (name, brand, category, gender, price, Website)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, brand, category, gender, price, Website))
    conn.commit()
    conn.close()

def insert_hoodies(name, brand, category, gender, price, Website):
    conn = sqlite3.connect('Clothes_Project.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO Hoodies (name, brand, category, gender, price, Website)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, brand, category, gender, price, Website))
    conn.commit()
    conn.close()

def insert_pants(name, brand, category, gender, price, Website):
    conn = sqlite3.connect('Clothes_Project.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO Pants (name, brand, category, gender, price, Website)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, brand, category, gender, price, Website))
    conn.commit()
    conn.close()

conn = sqlite3.connect('Clothes_Project.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS Hoodies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        brand TEXT NOT NULL,
        category TEXT NOT NULL,
        gender TEXT NOT NULL,
        price REAL NOT NULL,
        Website TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

conn = sqlite3.connect('Clothes_Project.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS Pants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        brand TEXT NOT NULL,
        category TEXT NOT NULL,
        gender TEXT NOT NULL,
        price REAL NOT NULL,
        Website TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

conn = sqlite3.connect('Clothes_Project.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS Shoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        brand TEXT NOT NULL,
        category TEXT NOT NULL,
        gender TEXT NOT NULL,
        price REAL NOT NULL,
        Website TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

def Htables():
    conn = sqlite3.connect('Clothes_Project.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM Hoodies')
    r = c.fetchall()
    for row in r:
        print(row)
        conn.close()

def Ptables():
    conn = sqlite3.connect('Clothes_Project.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM Pants')
    r = c.fetchall()
    for row in r:
        print(row)
        conn.close()

def Stables():
    conn = sqlite3.connect('Clothes_Project.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM Shoes')
    r = c.fetchall()
    for row in r:
        print(row)
        conn.close()

Mens_hoodies = data_Mens_Hoodies()
Mens_pants = data_Mens_Pants()
Mens_shoes = data_Mens_Shoes()
Womens_hoodies = data_Women_Hoodies()
Womens_pants = data_Women_Pants()
Womens_shoes = data_Womens_Shoes()

for product in Mens_hoodies:
    insert_hoodies(**product)
for product in Mens_pants:
    insert_pants(**product)
for product in Mens_shoes:
    insert_shoes(**product)
for product in Womens_hoodies:
    insert_hoodies(**product)
for product in Womens_pants:
    insert_pants(**product)
for product in Womens_shoes:
    insert_shoes(**product)
print("Data successful")

print ("\nShoes: ")
Stables ()
print ("\nPants: ")
Ptables ()
print ("\nHoodies: ")
Htables ()




