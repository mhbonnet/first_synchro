# -*- coding: utf-8 -*-

import json
import requests
from functions import extract_keywords
from flask import Flask, render_template, jsonify, request

from flask import request
app = Flask(__name__)

# Avec Flask, les décorateurs sont utilisés pour 
# associer une URL à une fonction. Ici, on associe 
# donc la fonction  hello  à l’URL /.
@app.route("/")
def main_api():
    return "Welcome to the test api!"


@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')
    framework = request.args.get('framework')
    return '''<h1>The language value is: {}</h1>
    <p>frame = {}</p>'''.format(language, framework)

@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        titre = request.form.get('title_input')
        question = request.form.get('body_input')
        tags = ['html', 'css', 'flask', 'json', 'api']
        return '''
                  <h3>Titre = {}</h3>
                  <p>{}</p>
                  <h1>Tags proposés :</h1>
                  <p>{}</p>'''.format(titre, question, tags)

    # otherwise handle the GET request
    return '''
              <form method="POST">
                  <div>
                  <label>Titre: <input type="text" name="title_input" required
       minlength="2" maxlength="256" size="50"</label></div>
                  <div><label>Question:  <textarea name="body_input" rows="10" cols="100"></textarea></label></div>
                  <input type="submit" value="Soumettre">
              </form>'''

@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][0]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']
    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)
    
if __name__ == "__main__":
    app.run(debug=True)