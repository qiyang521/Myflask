# _*_coding:utf-8_*_
# author    :qqy
# time      :2020/12/14 14:33
# file      :app.py
from flask import Flask,render_template,request,session,redirect
app=Flask(__name__)
app.secret_key='ausdfndasldgfdna234'
app.debug=True

USER_DICT={
    '1':{'name':'胡军','age':14},
    '2':{'name':'林志颖','age':34},
    '3':{'name':'高虎','age':77}
}


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    user=request.form.get('user')
    pwd=request.form.get('pwd')
    if user=='alex' and pwd=='123':
        # 用户信息放入session
        session['user_info']=user
        return redirect('/index')
    else:
        return render_template('login.html',msg='用户名密码错误')


@app.route('/index')
def index():
    user_info=session.get("user_info")
    if not user_info:
        return redirect('/login')
    return render_template('index.html',user_dict=USER_DICT)


@app.route('/detail')
def detail():
    user_info=session.get("user_info")
    if not user_info:
        return redirect('/login')
    uid=request.args.get('uid')
    info=USER_DICT.get(uid)
    return render_template('detail.html',info=info)


@app.route('/logout')
def logout():
    del session['user_info']
    # return redirect('/login')
    return '404'

if __name__ == '__main__':
    app.run()















