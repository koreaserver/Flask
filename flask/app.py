from flask import Flask, render_template, request, abort, redirect, url_for
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
app = Flask(__name__)

@app.route('/1')
def page1():
	url1 = requests.get('https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States')
	soup1 = bs(url1.text,'html.parser')
	data1 = soup1.select('tr>td>b>a')
	return render_template("/1.html", data1=data1)

@app.route('/2')
def page2():
	url2 = requests.get('https://finance.naver.com/sise/')
	soup2 = bs(url2.text,'html.parser')
	data2 = soup2.select_one('body>div>div>div>div>div>ul>li')
	return render_template("/2.html", data2=data2)

@app.route('/3', methods=['GET', 'POST'])
def page3():
	a = request.form.get('name')
	if a == 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States':
		return redirect(url_for('page1'))
	elif a == 'https://finance.naver.com/sise/':
		return redirect(url_for('page2'))
	return f'입력한 URL : {a} 입니다. 다시 입력해주세요.'

@app.route('/input')
def urlinput():
	return render_template("/input.html")
if __name__ == '__main__':
	app.run(port=80, debug=True)