#!/usr/bin/env python3

import json
import os
from recipe_scrapers import scrape_me
from flask_cors import CORS, cross_origin
os.environ["RECIPE_SCRAPERS_SETTINGS"] = "recipe_scrapers.settings.v12_settings"

from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
CORS(app, support_credentials=True)
api = Api(app)

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass


@app.route('/api/v1/scrape', methods=['GET'])
def api_url():
    if 'url' in request.args:
        url = request.args['url']
    else:
        url = "http://www.thedailymeal.com/recipes/spiced-grapefruit-juice-recipe"
    try:
        scraper = scrape_me(url)
        print("processing data");
        print(scraper.instructions());
        a_dictionary ={"url":url, "label": scraper.title(), "ingredients":scraper.ingredients(), "instructions":scraper.instructions(), "image":scraper.image(), "yield":scraper.yields(), "totalTime":scraper.total_time(), "digest":scraper.nutrients(), "source":scraper.host()};

        return jsonify(a_dictionary)
    except:
        return jsonify({"result":"error"})

		
app.run()
