# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello Taehoon'

@app.route('/coder')
def coder():
    return 'I am AutoCoder.'

# .py가 실행되는 경로 안에 'templates' 폴더 생성 후 그 안에 test.html 파일 넣어 두기
@app.route('/autocoder')
def autocoder():
    return render_template("test.html")

@app.route('/test2')
def test2():
    return render_template("test2.html")

def main():
    app.run(host='127.0.0.1', debug=False, port=80)


if __name__ == '__main__':
    main()