from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import rmodel
from google.cloud import translate

class Publish(MethodView):
    def get(self):
        return render_template('publish.html')

    def translate_text(self, target, text):
        translate_client = translate.Client()

        translation = translate_client.translate(text, target_language=target)['translatedText']
        return translation

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Translate to a different langauge 
        Insert translated data into datastore
        Redirect to recipelst when completed.
        """
        #translate_client = translate.Client()
        language = "ar"
        model = rmodel.get_model()
        model.insert(request.form['title'], request.form['author'], request.form['ingredlst'], request.form['preptime'], request.form['skilllv'], request.form['descrip'])
        # in theory I would like to call translate text on all the lines below and then add the transalted version to the other database
        #When I try and do this it tells me that the funcitons is undefined. even though I defined it above
        #title = translate_client.translate(request.form['title'], target_language=language)['translatedText']
        title = self.translate_text(language, request.form['title'])
        author = self.translate_text(language, request.form['author'] 
        ingredlst = self.translate_text(language, request.form['ingredlst'])
        preptime = self.translate_text(language, request.form['preptime'])
        skilllv = self.transalte_text(language, request.form['skilllv'])
        descrip = self.translate_text(language, request.form['descrip'])

        model.insert_translated(title, author, ingredlst, preptime, skilllv, descrip)
        return redirect(url_for('recipelst'))
