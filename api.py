from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

# A simple user database
users = {
    
}
conn=pyodbc.connect(driver="ODBC Driver 11 for SQL Server",host="192.168.1.43",user="sa",password="abc@123",database="LOT")
cursor=conn.cursor()
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    cursor.execute("select userid,idpassword from usermaster")
    res=cursor.fetchall()
    
    for row in res:
        
        
        users.update({row[0]:row[1]})
    
    
        #print(users)
        
    
    print(users)
    if username in users and users[username] == password:
        return jsonify({"message": "Login successful"}),200
    else:
        return jsonify({"message": "Invalid credentials"}),401
    #conn.close()


if __name__ == '__main__':
    app.run(debug=True,host='192.168.1.43',port=5000)