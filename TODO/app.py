from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from config import SqlManager


app = Flask(__name__)
api = Api(app)
db = SqlManager()

parser = reqparse.RequestParser()
parser.add_argument('message', type=str)

todos = db.look('select * from todo.todos')


def check_todo_key(key):
    key_All = [message['key'] for message in todos]
    if int(key) not in key_All:
        abort(404, error = "The TODO with key {} does not exist".format(key))


class ToDos(Resource):

    def get(self):
        todos = db.look('select * from todo.todos')
        return todos, 200

    def post(self):
        args = parser.parse_args()
        key_Max = max([int(message['key']) for message in todos]) + 1
        db.CRU("insert into todo.todos (key,value ) values ({}, '{}')".format(key_Max, args['message']))
        return 'creation todo successful', 201


class ToDo(Resource):

    def delete(self, key):
        check_todo_key(key)
        db.CRU("delete from todo.todos where key = {}".format(key))
        return 'todo {} delete'.format(key), 201

    def put(self, key):
        args = parser.parse_args()
        print("update todo.todos set value ='{}' where key = {}".format(args['message'], key))
        db.CRU("update todo.todos set value ='{}' where key = {}".format(args['message'], key))
        return 'todo {} update'.format(key), 201


api.add_resource(ToDos, '/todos')
api.add_resource(ToDo, '/todos/<key>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9876, debug=True)

