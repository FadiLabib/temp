from flask import render_template
from flask.views import MethodView
import rmodel

#This class uses the data from the database model 
#Then it feeds this data as an input to the recipelst.html web page
#recipelst.html process the recipes_raw data and displays it to the end user
class Recipelst(MethodView):
    def get(self):
         model = rmodel.get_model()
         recipes_raw = [dict(title=row[0], author=row[1], ingred_list=row[2], prep_time=row[3], skill_lv=row[4], descrip=row[5]) for row in model.select()]
         return render_template('recipelst.html',some_recipes=recipes_raw)
