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

# dept_Id,eType,cas,ear,med sent as json object from frontend
# Find the corresponding record and update the row
# if record doesn't exist then create a new record and insert it
# Body of the request: {"dept_id": ,"e_type": ,"casual": ,"earned": ,"medical": }
# Return: 
@app.route('/update_calendar',methods=['POST'])
def update_calendar_info():
    deptId = request.json["dept_id"]
    eType = request.json["e_type"]
    client = MongoClient()
    db = client['employee_management_db']
    department_details = db.department_table
    res = list(department_details.find({'dept_id':deptId}))
    # if department id not in the department details table then it is an invalid request
    if(len(res) == 0):
        client.close()
        return jsonify({}),400
    calendar_details = db.calendar_table
    res = list(calendar_details.find({'dept_id':deptId,'e_type':eType}))
    cas = request.json['casual']
    ear = request.json['earned']
    med = request.json['medical']
    if(len(res) != 0):
        calendar_details.update_one({'dept_id':deptId,'e_type':eType},{"$set": {'casual':cas,'earned':ear,'medical':med}})
        client.close()
        return jsonify({}),200
    data = {'dept_id':deptId,'e_type':eType,'casual':cas,'earned':ear,'medical':med}
    calendar_details.insert_one(data)
    client.close()
    return jsonify({}),200

# Api returns the number of leave left in each category for a given employee
# Input -> http://127.0.0.1:5000/employee_id
#Output -> {"casual": ,"medical": ,"earned": }
@app.route('/get_leave_data/<string:empId>',methods=['GET'])
def get_leave_data(empId):
    client = MongoClient()
    db = client['employee_management_db']
    employee_details = db.employee_details_table
    empInfo = employee_details.find_one({'e_id':empId})
    if(empInfo != None):
        data = empInfo["leave_left"]
        client.close()
        # print(data)
        return jsonify(data),200
    else:
        client.close()
        return jsonify({'status':'Invalid employee id'}),400

# Takes deptID from frontend which is given in the url
# Input -> http:/127.0.0.1/get_leaves/Department_ID
# Output -> {"27/10/2019":"10","30/10/2019":"5"}
# Output is dictionary containing key value pairs where key is date and value is number of employees on leave
@app.route('/get_leaves/<string:deptId>',methods=['GET'])
def get_leaves_date(deptId):
    client = MongoClient()
    db = client['employee_management_db']
    contents_leave = db.leave_collection_table
    res_leaves = list(contents_leave.find())
    contents_emp = db.employee_details_table
    leave_dict = dict()
    today = date.today()
    today_date = today.strftime("%d/%m/%Y")
    for i in res_leaves:
        if(i['status'] == "approved"):
            emp_id = i['e_id']
            emp_det = list(contents_emp.find({'e_id':emp_id}))
            if(emp_det[0]['dept_id'] == deptId):
                dates = i['list_of_dates']
                for j in dates:
                    if(j > today_date):
                        if(j in leave_dict.keys()):
                            leave_dict[j] = leave_dict[j] + 1
                        else:
                            leave_dict[j] = 1
    client.close()
    return jsonify(leave_dict),200

# Input -> {"e_id": ,"type": ,"list_of_dates": ,"reason": }
# Output -> if number of leaves are exceeding the number of leaves left
#           api will return {'status':'rejected'} with status code 400
#           otherwise it will return {'status':'pending'} with status code 200
@app.route('/apply_leave',methods=['POST'])
def apply_leave():
    empId = request.json["e_id"]
    lType = request.json["type"]
    dates = request.json["list_of_dates"]
    numberOfLeaves = len(dates)
    reason = request.json["reason"]
    client = MongoClient()
    db = client['employee_management_db']
    employee_details = db.employee_details_table
    leave_col = db.leave_collection_table
    empInfo = list(employee_details.find({'e_id':empId}))
    if(int(empInfo[0]['leave_left'][lType]) < numberOfLeaves):
        data = {'e_id':empId,'type':lType,'list_of_dates':dates,'reason':reason,'status':'rejected'}
        leave_col.insert_one(data)
        client.close()
        return jsonify({'status':'rejected'}),400
    else:
        data = {'e_id':empId,'type':lType,'list_of_dates':dates,'reason':reason,'status':'pending'}
        leave_col.insert_one(data)
        client.close()
        return jsonify({'status':'pending'}),200

# Input -> {"e_id": ,"type": ,"list_of_dates": ,"status":"REJECT"/"APPROVE"}
@app.route('/approve_leave',methods=['POST'])
def approve_leave():
    empId = request.json["e_id"]
    lType = request.json["type"]
    dates = request.json["list_of_dates"]
    numberOfLeaves = len(dates)
    status=request.json["status"]
    client = MongoClient()
    db = client['employee_management_db']
    employee_details = db.employee_details_table
    leave_col = db.leave_collection_table
    empInfo = list(employee_details.find({'e_id':empId}))
    if(status=="REJECT"):
        leave_col.update({'e_id':empId},{"$set": {'status':'rejected'}})
        client.close()
        return jsonify({'status':'rejected'}),200
    else:
        updated = str(int(empInfo[0]['leave_left'][lType]) - numberOfLeaves)
        data = empInfo[0]['leave_left']
        data[lType] = updated
        employee_details.update({'e_id':empId},{"$set": {'leave_left':data}})
        leave_col.update({'e_id':empId},{"$set": {'status':'approved'}})
        client.close()
        return jsonify({'status':'approved'}),200

# Input is given through url -> http://127.0.0.1:5000/get_leave_applications/approver_id
# Output -> [{'e_id': ,'type': ,'list_of_dates': ,'reason': ,'status':"pending"/"rejected"/"approved"},...]
# Its a list of dictionary,where each dictionary is a leave application
@app.route('/get_leave_applications/<string:approver_id>',methods=['GET'])
def get_applications(approver_id):
    client = MongoClient()
    db = client['employee_management_db']
    salary_apps = db.leave_collection_table
    res = list(salary_apps.find())
    leave_applications = list()
    for i in res:
        e_id = i['e_id']
        emp_db = db.employee_details_table
        res = list(emp_db.find({'e_id':e_id}))
        if(res[0]['approver_id'] == approver_id):
            data = dict()
            data['e_id'] = i['e_id']
            data['type'] = i['type']
            data['list_of_dates'] = i['list_of_dates']
            data['reason'] = i['reason']
            data['status'] = i['status']
            leave_applications.append(data)
    return jsonify(leave_applications),200

if __name__ == '__main__':
    app.run("0.0.0.0",port=5000)
