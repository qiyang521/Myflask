# _*_coding:utf-8_*_
# author    :qqy
# time      :2020/12/14 11:58
# file      :settings.py

from werkzeug.serving import run_simple
from werkzeug.wrappers import Request,Response

@Request.application
def hello(request):
    return Response('hello werkzeug!')


if __name__ == '__main__':
    run_simple('127.0.0.1',6000,hello)