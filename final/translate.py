from flask import render_template
from flask.views import MethodView
import rmodel

#This class uses the data from the datastore model
#Then it fed this data as an input to the translate.hml web page
#translate.html processes the recipes_raw data and displays it to the end user
class Translate(MethodView):
    def get(self):
         model = rmodel.get_model()
         recipes_translated = [dict(title=row[0], author=row[1], ingred_list=row[2], prep_time=row[3], skill_lv=row[4], descrip=row[5]) for row in model.select_translated()]

        #Pass recipes_translated to Jinja2 template to render
        return render_template('translate.html',some_recipes=recipes_translated) 
