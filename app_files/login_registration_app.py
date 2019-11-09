#login and registration

from flask import Flask, jsonify, request, abort
from pymongo import MongoClient
import requests
import re
from datetime import date
import datetime
import pickle
app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Origin','127.0.0.1')
  return response

# Login API - finds the record of the user in the table
# Input -> {"user_name": ,"password": }
# if user does not exist - 403
# if password is wrong - 401
@app.route('/login',methods=['POST'])
def check_login():
    usr = request.json["user_name"]
    password = request.json["password"]
    client = MongoClient()
    db = client['employee_management_db']
    ld = db.login_table
    res = list(ld.find({'user_name':usr}))
    d = dict()
    if(len(res)==0):
        #User not registered
        client.close()
        d["e_id"] = ""
        return jsonify(d),403
    elif(res[0]['user_name'] == usr and res[0]['password']!=password):
        #Password wrong
        d["e_id"] = ""
        return jsonify(d),401
    else:
        client.close()
        d["e_id"] = res[0]["e_id"]
        return jsonify(d),200

# if 400 returned redirect to /login page
@app.route('/register',methods=['POST'])
def register():
    usr = request.json["user_name"]
    password = request.json["password"]
    dept = request.json["dept_id"]
    client = MongoClient()
    db = client['employee_management_db']
    user_in_table = list(db.login_table.find({'user_name':usr}))
    if(len(user_in_table)==0):
        #generate e_id "id"
        department = dept[0:3]
        emps = list(db.employee_details_table.find({'dept_id':dept}))
        emp_lis = []
        for i in emps:
            emp_lis.append(i['e_id'])

        id_lis=[]
        for i in emp_lis:
            id_lis.append(int(i.split(department)[1]))
        m = max(id_lis)+1
        year = date.today().year
        id = str(year)+department+str(m).zfill(3)
        data = {'e_id':id,'user_name':usr,'password':password}
        db.login_table.insert_one(data)
        client.close()
        return jsonify({}),200
    client.close()
    return jsonify({}),400

if __name__ == '__main__':
    app.run("0.0.0.0",port=5000)
