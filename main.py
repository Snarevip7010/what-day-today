import datetime
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def whatday():

    # Datetimeを利用して今日の日付を取得する
    date = datetime.date.today().strftime("%m/%d")

    # WebサイトのURLを指定
    url = "https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8"

    # Requestsを利用してWebページを取得する
    r = requests.get(url)

    # BeautifulSoupを利用してWebページを解析する
    soup = BeautifulSoup(r.text, 'html.parser')

    # soup.find_allを利用して今日は何の日を取得する
    elems = soup.find_all(id="mf-itn")

    # for loopを利用してリスト部分を取得する
    for row in elems:
        csvRow = []
        for cell in row.findAll('li'):
            csvRow.append(cell.get_text())

    #htmlに渡す
    return render_template('index.html', title='What Day Today', date=date, elems=csvRow)
 
if __name__ == '__main__':
<<<<<<< HEAD
    app.run()
======
>>>>>>> origin/master
