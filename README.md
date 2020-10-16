# 1. 创建新的 todo和测试
  def post(self):
      args = parser.parse_args()
      key_Max = max([int(message['key']) for message in todos]) + 1
      db.CRU("insert into todo.todos (key,value ) values ({}, '{}')".format(key_Max, args['message']))
      return 'creation todo successful', 201
  
  def add():
    # add new todo
    html = requests.post('http://127.0.0.1:5000/todos', data=todo)
    print(html.text)
    
# 2. 删除某条 todo和测试
  def delete(self, key):
      check_todo_key(key)
      db.CRU("delete from todo.todos where key = {}".format(key))
      return 'todo {} delete'.format(key), 201

  def delete():
    # delete a todo
    html = requests.delete('http://127.0.0.1:5000/todos/4')
    print(html.text)

# 3. 更新某条 todo和测试
  def put(self, key):
      args = parser.parse_args()
      print("update todo.todos set value ='{}' where key = {}".format(args['message'], key))
      db.CRU("update todo.todos set value ='{}' where key = {}".format(args['message'], key))
      return 'todo {} update'.format(key), 201

  def update():
    # update a todo
    html = requests.put('http://127.0.0.1:5000/todos/3', data=todo)
    print(html.text)
    
# 4. 列出所有的 todo
  def get(self):
      todos = db.look('select * from todo.todos')
      return todos, 200
        
  def find():
    # show all todo
    html = requests.get('http://127.0.0.1:5000/todos')
    print(html.text)
