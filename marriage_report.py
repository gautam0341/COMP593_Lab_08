"""
Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""
import os
import pandas as panda
import sqlite3
from create_relationships import db_path


def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()

    # Save all married couples to CSV file
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)


def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """

    # Relationship type as required
    rel_type = 'spouse'

    # TODO: Function body

    # Making a connection to DB
    con = sqlite3.connect(db_path)

    # Creating a Cursor Object
    cur = con.cursor()

    # Fetching all the results
    cur.execute(""" SELECT person1.name, person2.name, start_date, type FROM relationships JOIN people person1 ON person_1_id = person1.id JOIN people person2 ON person_2_id = person2.id where type = '%s'""" % (
        rel_type))

    # Extracting data from cursor
    CouplesData = cur.fetchall()

    # Closing the connection
    con.close()

    # loop to print data
    for person1, person2, start_date, type in CouplesData:
        print(f'{person1} has been a {type} of {person2} since {start_date}.')

    # Returning the data list
    return CouplesData


def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    # TODO: Function body

    # Using Pandas module and dataframe instance
    df = panda.DataFrame(married_couples, columns=['Person 1', 'Person 2', 'Anniversary', 'Relation'])

    # Saving data to CSV file
    df.to_csv(csv_path, index=False)

    return


if __name__ == '__main__':
    main()
