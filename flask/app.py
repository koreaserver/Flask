from flask import Flask, render_template
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
app = Flask(__name__)

@app.route('/1')
def page1():
	url1 = requests.get('https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States')
	soup1 = bs(url1.text,'html.parser')
	data1 = soup1.select('tr > td > b > a')
	return render_template("/1.html", data1=data1)

@app.route('/2')
def page2():
	url2 = requests.get('https://finance.naver.com/sise/')
	soup2 = bs(url2.text,'html.parser')
	data2 = soup2.select_one('body > div > div > div > div > div > ul')
	return render_template("/2.html", data2=data2)
if __name__ == '__main__':
	app.run(port=80, debug=True)