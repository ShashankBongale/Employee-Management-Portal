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

@app.route('/get_emp_details/<string:empId>',methods=['GET'])
def get_emloyee_details(empId):
    client = MongoClient()
    db = client['employee_management_db']
    employee_details = db.employee_details_table
    empInfo = employee_details.find_one({'e_id':empId})
    if(empInfo != None):
        client.close()
        del empInfo["_id"]
        # print(empInfo)
        return jsonify(empInfo),200
    else:
        client.close()
        return jsonify({'status':'Invalid employee id'}),400

#Part 1 of initiate-salary-process which returns the json of e-types to the frontend
#Input nothing
#Output -> ["DEV","HR",...]
@app.route('/display_etypes',methods=['GET']) 
def display_etypes():
    client = MongoClient()
    db = client['employee_management_db']
    contents = db.account_department_table
    res = list(contents.find())
    etype_list = []
    for i in res:
        etype_list.append(i['e_type'])
    client.close()
    return jsonify(etype_list),200

# This api return department id given an employee id
# Input -> http://127.0.0.1:5000/employee_id
# output -> Department ID
@app.route('/get_dept_id/<string:e_id>', methods=['GET'])   
def get_dept_id(e_id):
    client = MongoClient()
    db = client['employee_management_db']
    emp = db.employee_details_table
    res = list(emp.find({'e_id':e_id}))
    if(len(res)==0):
        client.close()
        return jsonify({}),400
    client.close()
    return jsonify(res[0]['dept_id']),200

# This api returns the employee type given an employee id
# Input -> http://127.0.0.1:5000/employee_id
# output -> DEV/MANAGER/HOD
@app.route('/get_e_type/<string:e_id>', methods=['GET'])   
def get_e_type(e_id):
    client = MongoClient()
    db = client['employee_management_db']
    emp = db.employee_details_table
    res = list(emp.find({'e_id':e_id}))
    if(len(res)==0):
        client.close()
        return jsonify({}),400
    client.close()
    return jsonify(res[0]['e_type']),200

if __name__ == '__main__':
    app.run("0.0.0.0",port=5000)
