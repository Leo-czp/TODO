import requests


def add():
    # add new todo
    html = requests.post('http://127.0.0.1:5000/todos', data=todo)
    print(html.text)

def delete():
    # delete a todo
    html = requests.delete('http://127.0.0.1:5000/todos/4')
    print(html.text)

def update():
    # update a todo
    html = requests.put('http://127.0.0.1:5000/todos/3', data=todo)
    print(html.text)

def find():
    # show all todo
    html = requests.get('http://127.0.0.1:5000/todos')
    print(html.text)

if __name__ == '__main__':
    todo = {'message': 'this is todo 3'}
    # add()
    # delete()
    # update()
    find()
