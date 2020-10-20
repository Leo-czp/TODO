from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# The database that needs to be built
#
#CREATE KEYSPACE TODO WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
#CREATE TABLE todos (key int PRIMARY KEY, value text);
#INSERT INTO todos(key,value) values(1,'this is todo1');
#INSERT INTO todos(key,value) values(2,'this is todo2');
#INSERT INTO todos(key,value) values(3,'this is todo3');

class CqlManager:
    def __init__(self):
        self.contact_point = ['182.92.164.236'] * 10
        self.auth_provider = PlainTextAuthProvider(username='wei',password='mypassword')
        self.cluster = Cluster(contact_points=self.contact_point, auth_provider=self.auth_provider)
        self.session = self.cluster.connect()

    def look(self, cql):
        execute_result = self.session.execute('{};'.format(cql), timeout=None)
        result = execute_result._current_rows
        return [{'key':line[0], 'value':line[1]} for line in result]

    def CRU(self, cql):
        self.session.execute('{};'.format(cql), timeout=None)
        print(cql)
