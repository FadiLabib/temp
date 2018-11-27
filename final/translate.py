from flask import render_template
from flask.views import MethodView
import rmodel

#This class uses the data from the datastore model
#Then it fed this data as an input to the translate.hml web page
#translate.html processes the recipes_raw data and displays it to the end user
class Translate(MethodView):
    def get(self):
        model=rmodel.get_model()

        #Use the model to fetch information
        # from Datastore about each recipe
        query = model.query(kind='ArRecipes')
        recipes_translated = list(query.fetch())

        #Pass recipes_translated to Jinja2 template to render
         return render_template('translate.html',some_recipes=recipes_translated) 
