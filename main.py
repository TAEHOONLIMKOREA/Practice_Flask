# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template
from flask import request, redirect
import random

app = Flask(__name__)

next_id = 4
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

def template(contents, content, id=None):
    contextUI=''
    if id is not None:
        contextUI = f'''
            <li><a href="/create/">create</a></li>
            <li><a href="/update/{id}/">update</a></li>
            <li>
            <form action="/delete/{id}" method="POST">
                <p><input type="submit" name="delete_button" value="delete"></p>
            </form>
            </li>        
        '''
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a><h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>                
                {contextUI}
            </ul>
        </body>
    </html>
    '''

def getContents():
    list_tags = ''
    for topic in topics:
        list_tags = list_tags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'

    return list_tags

@app.route('/')
def index():

    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    for topic in topics:
        if id == topic["id"]:
            topics.remove(topic)
            break
    return redirect('/')

@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}', id)

@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>            
            </form>      
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global next_id
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id': next_id, 'title': title, 'body': body}
        topics.append(newTopic)
        next_id = next_id + 1
        url = '/read/' + str(next_id)
        return redirect(url)


@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    if request.method == 'GET':
        content = f'''
            <form action="/update/{id}" method="POST">
                <p><input type="text" name="title" placeholder="title" value="{title}"></p>
                <p><textarea name="body" placeholder="body">{body}</textarea></p>
                <p><input type="submit" value="update"></p>            
            </form>      
        '''
        return template(getContents(), content, id)
    elif request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        for topic in topics:
            if id == topic['id']:
                topic['title'] = title
                topic['body'] = body
                break
        url = '/read/' + str(id)
        return redirect(url)


# .py가 실행되는 경로 안에 'templates' 폴더 생성 후 그 안에 test.html 파일 넣어 두기
@app.route('/autocoder')
def autocoder():
    return render_template("test.html")

@app.route('/test2')
def test2():
    return render_template("test2.html")

def main():
    app.run(host='127.0.0.1', debug=True, port=80)


if __name__ == '__main__':
    main()