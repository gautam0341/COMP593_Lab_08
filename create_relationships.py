"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3
from random import randint, choice
from faker import Faker

# Determine the path of the database
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'social_network.db')


def main():
    create_relationships_table()
    populate_relationships_table()


def create_relationships_table():
    """Creates the relationships table in the DB"""

    CreateQuery = ''

    # Creating a connection to DB
    connection = sqlite3.connect('social_network.db')

    # SQL table Creation Query
    CreateQuery = """ CREATE TABLE IF NOT EXISTS relationships ( id INTEGER PRIMARY KEY, person_1_id INTEGER NOT NULL, person_2_id INTEGER NOT NULL, type TEXT NOT NULL, start_date DATE NOT NULL, FOREIGN KEY (person_1_id) REFERENCES people (id), FOREIGN KEY (person_2_id) REFERENCES people (id) ); """

    # creating a cursor for corresponding Connection
    cursor1 = connection.cursor()

    # Query Execution
    cursor1.execute(CreateQuery)

    # Committing the changes to DB
    connection.commit()

    # Closing the Connection
    connection.close()


def populate_relationships_table():
    """Adds 100 random relationships to the DB"""

    # Creating Faker Object
    faker = Faker()

    # Creating a connection to DB
    connection = sqlite3.connect('social_network.db')

    # creating a cursor for corresponding Connection
    cursor1 = connection.cursor()

    # taking an iterator
    iterator = 0

    person_1_obj = 0
    person_2_obj = 0

    while iterator < 100:
        # SQL query that inserts a row of data in the relationships table.
        add_relation = """ INSERT INTO relationships ( person_1_id, person_2_id, type, start_date ) VALUES (?, ?, ?, ?); """

        # Randomly select first person in relationship
        person_1_obj = randint(1, 200)

        # Randomly select second person in relationship

        person_2_obj = randint(1, 200)

        # Loop ensures person will not be in a relationship with themself
        while person_2_obj == person_1_obj:
            person_2_obj = randint(1, 200)

        # Randomly select a relationship type
        relation = choice(('friend', 'spouse', 'partner', 'relative'))

        # Randomly select a relationship start date between now and 50 years ago
        start_date = faker.date_between(start_date='-50y', end_date='today')

        # Create tuple of data for the new relationship
        obj_relation = (person_1_obj, person_2_obj, relation, start_date)

        # Add the new relationship to the DB
        cursor1.execute(add_relation, obj_relation)

        # incrementing the iterator for loop
        iterator = iterator + 1

    # Committing the Changes
    connection.commit()

    # Closing the Connection
    connection.close()


if __name__ == '__main__':
    main()
