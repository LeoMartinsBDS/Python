import MySQLdb

host = "localhost"
user = "root"
password = #your password here
db = "escola_curso"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor(MySQLdb.cursors.DictCursor)

def select(fields, tables, where=None):

    global c

    query = "SELECT " + fields + " FROM " + tables
    if (where) :
        query = query + " WHERE " + where

    c.execute(query)
    return c.fetchall()

def insert(values, table, fields=None):

    global c, con

    query = " INSERT INTO " + table 
    if(fields):
        query = query + " (" +fields+ ") "

    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

    c.execute(query)
    con.commit()

def update(sets, table, where=None):

    global c, con

    query = "UPDATE " + table 
    query = query + " SET " +  ",".join([field + " = '" + value + "'"  for field, value in sets.items()])
    
    if(where):
        query = query + " WHERE " + where

    c.execute(query)
    con.commit()

def delete(table, where):

    global c, con
    
    query = "DELETE FROM " + table
    query = query + " WHERE " + where

    c.execute(query)
    con.commit()


values= [
    "DEFAULT, 'JOAO PEDRO', '123456789', '2000-01-01', 'AV DAS PEDRAS, 123', 'SÃO PAULO', 'SP'",
    "DEFAULT, 'MARIA PEDRO','123456780', '2000-01-01', 'AV DAS PEDRAS, 123', 'SÃO PAULO', 'SP'"]

#insert(values, "alunos")
#result = select("NOME, CPF", "ALUNOS", "ID_ALUNO = 1")

#update({"nome":"Joao Paulo","cidade":"Macapá"}, "alunos", "id_aluno = 2")
#delete("alunos", "id_aluno = 1")

#print(result)
print(select("*", "alunos"))
#print(result[0]["NOME"])