"""
Python list model
"""
from .Model import Model

class model(Model):
    def __init__(self):
        self.recipes = []
        
    def select(self):
        """
        Returns recipes list of lists
        Each list in recipes contains: title, author, ingredient list, prep time, skill level, description
        :return: List of lists
        """
        return self.recipes

    def insert(self, title, author, ingred_list, prep_time, skill_lv, descrip):
        """
        Appends a new list of values representing new recipe into recipes
        :param title: String
        :param author: String
        :param ingred_list: String
        :param prep_time: String
        :param skill_lv: String
        :param descrip: String
        :return: True
        """
        params = [title, author, ingred_list, prep_time, skill_lv, descrip]
        self.recipes.append(params)
        return True
