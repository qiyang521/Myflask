# _*_coding:utf-8_*_
# author    :qqy
# time      :2020/12/14 11:24
# file      :test.py

from flask import Flask

app=Flask(__name__)
app.debug=True

@app.route('/index')
def hello_word():
    return 'hello word!'

if __name__ == '__main__':
    app.run()