from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import rmodel
from google.cloud import translate
import six

class Publish(MethodView):
    def get(self):
        return render_template('publish.html')

    def translate_text(target, text):
        translate_client = translate.Client()

        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')

        result = translate_cleint.translate(text, target_langauge=target)
        return result

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Translate to a different langauge 
        Insert translated data into datastore
        Redirect to recipelst when completed.
        """
        model = rmodel.get_model()
        model.insert(request.form['title'], request.form['author'], request.form['ingredlst'], request.form['preptime'], request.form['skilllv'], request.form['descrip'])
        title = translate_text(ar,request.form['title']
        author = translate_text(ar, request.form['author'] 
        ingredlst = translate_text(ar, request.form['ingredlst']
        preptime = translate_text(ar, request.form['preptime']
        skilllv = translate_text(ar, request.form['skilllv']
        descrip = translate_text(ar, request.form['descrip']

        model.insert_translated(title, author, ingredlst, preptime, skilllv, descrip)
        return redirect(url_for('recipelst'))
