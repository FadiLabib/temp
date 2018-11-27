"""
A simple recipes catalog flask app.
Data is stored in a SQLite database that looks something like the following:

+--------------------+------------------+-------------------------------+----------------+--------------+-----------------------------+
| Title              | Author           | ingred_list                   | prep time      | Skill Level  | Description                 |
+====================+==================+===============================+----------------+--------------+-----------------------------+
| Recipies Title     | First Last       | Ingred1, Ingred2, ... Ingredx | XXX Minutes    | Medium       | How to cook the meal        |
+--------------------+------------------+-------------------------------+----------------+--------------+-----------------------------+

This can be created with the following SQL (see bottom of this file):

    create table recipes (title text, author text, ingred_list, prep_time text, skill_lv text, descrip);

"""
from .Model import Model
import sqlite3
DB_FILE = 'recipies.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from recipes")
        except sqlite3.OperationalError:
            cursor.execute("create table recipes (title text, author text, ingred_list, prep_time text, skill_lv text, descrip)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: title, author, ingredients list, prep time, skill level, and descrip
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM recipes")
        return cursor.fetchall()

    def insert(self, arg_title, arg_author, arg_ingred_list, arg_prep_time, arg_skill_lv, arg_descrip):
        """
        Inserts entry into database
        :param arg_title: String
        :param arg_author: String
        :param arg_ingred_list: String
        :param arg_prep_time: String
        :param arg_skill_lv: String
        :param arg_descrip: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'title':arg_title, 'author':arg_author, 'ingred_list':arg_ingred_list, 'prep_time':arg_prep_time, 'skill_lv':arg_skill_lv, 'descrip':arg_descrip}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into recipes (title, author, ingred_list, prep_time, skill_lv, descrip) VALUES (:title, :author, :ingred_list, :prep_time, :skill_lv, :descrip)", params)

        connection.commit()
        cursor.close()
        return True

