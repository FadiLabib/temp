from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import rmodel

class Publish(MethodView):
    def get(self):
        return render_template('publish.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to recipelst when completed.
        """
        model = rmodel.get_model()
        model.insert(request.form['title'], request.form['author'], request.form['ingredlst'], request.form['preptime'], request.form['skilllv'], request.form['descrip'])
        return redirect(url_for('recipelst'))
