"""
A simple reciepe flask app.
"""
import flask
from flask.views import MethodView
from home import Home
from recipelst import Recipelst
from publish import Publish
from translate import Translate

app = flask.Flask(__name__)       # our Flask app

#URL for the landing page, in this case home
app.add_url_rule('/',
                 view_func=Home.as_view('home'),
                 methods=["GET"])

#URL for the page containing the recipes
app.add_url_rule('/recipelst/',
                 view_func=Recipelst.as_view('recipelst'),
                 methods=["GET"])

#URL for the page containing the form to add recipes
#This page accepts both 'GET' and 'POST' requests
app.add_url_rule('/publish/',
                 view_func=Publish.as_view('publish'),
                 methods=['GET', 'POST'])

#URL for the page containg the recipies translated to Arabic
app.add_url_rule('/translate', 
                view_func=Translate.as_view('translate'),
                methods=['GET'])

# Running the app on debug mode using ip address 0.0.0.0 & port 8000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
