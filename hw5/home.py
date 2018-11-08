from flask import render_template
from flask.views import MethodView

#This class simply render the home.html page
class Home(MethodView):
    def get(self):
        return render_template('home.html')
