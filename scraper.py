from bs4 import BeautifulSoup
import requests
import flask
from flask import request
from flask import jsonify
import json
from Github import Github

URL = 'https://github.com/trending'
app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/github/trend', methods=['GET'])
def scrap() :
    #user = request.args.get('user')
    list = []
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    info = soup.find_all(class_='Box-row')
    for item in info :
        title = (item.find(class_='h3 lh-condensed').find('a').get_text()).replace('\n','').replace(' ', '')
        link = "https://github.com/" + item.find(class_='h3 lh-condensed').find('a')['href']
        text = item.find(class_='col-9 text-gray my-1 pr-4').get_text().strip()
        glo_language = item.find(class_='f6 text-gray mt-2').find_all(class_='d-inline-block ml-0 mr-3')
        for lan in glo_language :
            language = lan.find('span',itemprop='programmingLanguage').get_text()
        star= item.find(class_='f6 text-gray mt-2').select('a')[0].get_text().strip()
        folk= item.find(class_='f6 text-gray mt-2').select('a')[1].get_text().strip()
        github = Github(title,link,text,language,star,folk)
        list.append(github)
        #print(github.reponseJson())

    return jsonify(trending=[e.reponseJson() for e in list])

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>URI is not correct, please check out the documentation.</p>", 404




app.run()
