import sqlite3
import sys

class Database:

    def __init__(self):
        self.connection = sqlite3.connect('database.db')

        #Added this line to return fetchall() and fetchone() results ad dictionaries rather than lists.
        self.connection.row_factory = sqlite3.Row

        with open('database.sql') as f:
            self.connection.executescript(f.read())

            self.cur = self.connection.cursor()

    def test_populate_Restaurants(self):

        #Restaurant 1
        restName = 'McDonalds'
        query = '''
                INSERT INTO Restaurants (restName) VALUES ('{}');
                '''.format(restName)
        
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)

        #Restaurant 2
        restName = 'Burger King'
        query = '''
                INSERT INTO Restaurants (restName) VALUES ('{}');
                '''.format(restName)
        
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)

        #Restaurant 3
        restName = 'Pizza Hut'
        query = '''
                INSERT INTO Restaurants (restName) VALUES ('{}');
                '''.format(restName)
        
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)

        self.connection.commit()

    def list_Restaurants(self):

        query = '''
                SELECT *
                FROM Restaurants
                '''
        
        self.cur.execute(query)

        result = self.cur.fetchall()

        return result

    def __exit__(self):
        self.connection.close()