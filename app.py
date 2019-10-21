#app.py

"""
1. @app.route('/update_calendar',methods=['POST'])
2. @app.route('/login',methods=['POST'])
3. @app.route('/register',methods=['POST'])
4. @app.route('/get_leaves/<string:deptId>',methods=['GET'])
5. @app.route('/apply_leave',methods=['POST'])
6. @app.route('/approve_leave',methods=['POST'])
7. @app.route('/display_etypes',methods=['GET'])
8. @app.route('/initiate-salary-process',methods=['POST'])
9. @app.route('/get_leave_applications/<string:approver_id>',methods=['GET'])
10. @app.route('/get_bonus_status/<string:approver_id>',methods=['GET'])
11. @app.route('/approve_bonus',methods=['POST'])
12. @app.route('/check_salary_status',methods=['GET'])

"""

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
 
@app.route('/check',methods=['GET'])
def trial_connection():
    trial_list = dict()
    trial_list["trial"] = "allOk";
    return jsonify(trial_list),200


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

#Part 2 of initiate-salary-process which takes in selected e-types and updates credited date for every employee in selected type
#Input is given through url:http://127.0.0.1:5000/initiate-salary-process/employee_type
#Output is nothing,just a empty json with status 200
@app.route('/initiate-salary-process/<string:etype>',methods=['POST'])
def initiate_salary_process(etype):
    client = MongoClient()
    db = client['employee_management_db']
    today = date.today()
    employees = db.employee_details_table
    salary_info = db.salary_detail_table
    emps = list(employees.find({'e_type':etype}))
    for i in emps:
        salary_info.update({'e_id':i['e_id']},{"$set":{'last_salary_credited':today.strftime("%d/%m/%Y")}})
    client.close()
    return jsonify({}),200

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

# This api returns all the employee under an approver who have not yet got bonus this year
# Input to the api is given through url
# Output will be [{"e_id": ,"user_name": ,"e_email": ,"e_contact": },...]
@app.route('/get_bonus_status/<string:approver_id>',methods=['GET'])
def get_bonus(approver_id):
    client = MongoClient()
    db = client['employee_management_db']
    emp_details = db.employee_details_table
    bonus_credited_det = db.salary_detail_table
    res = list(emp_details.find())
    now = datetime.datetime.now()
    year = str(now.year)
    applications = list()
    for i in res:
        res_bonus = bonus_credited_det.find({'e_id':i['e_id']})
        if(i['approver_id'] == approver_id and (res_bonus[0]['last_bonus_credited'] == "" or res_bonus[0]['last_bonus_credited'].split('/')[2] != year)):
            emp_det = dict()
            emp_det['e_id'] = i['e_id']
            emp_det['user_name'] = i['user_name']
            emp_det['e_email'] = i['e_email']
            emp_det['e_contact'] = i['e_contact']
            applications.append(emp_det)
    client.close()
    return jsonify(applications),200

# This is api is for approving the bonus
# Input -> {"e_id": }
# Output -> Updates the db and returns an empty json
@app.route('/approve_bonus',methods=['POST'])
def approvebonus():
    e_id = request.json["e_id"]
    client = MongoClient()
    db = client['employee_management_db']
    sal_details = db.salary_detail_table
    now = datetime.datetime.now()
    day = str(now.day)
    month = str(now.month)
    year = str(now.year)
    today_date = day + "/" + month + "/" + year
    sal_details.update({'e_id':e_id},{"$set":{'last_bonus_credited':today_date}})
    return jsonify({}),200

# This returns the current months salary status
# Input is given through the url
# Api checks the db and returns "credired"/"pending"
@app.route('/check_salary_status/<string:eid>',methods=['GET'])
def check_salary_status(eid): 
    client = MongoClient()
    db = client['employee_management_db']
    sal = db.salary_detail_table
    res = list(sal.find({'e_id':eid}))
    sal_month = res[0]['last_salary_credited'].split('/')[1]
    today = date.today().strftime("%d/%m/%Y")
    curr_month = today.split('/')[1]
    if(curr_month==sal_month):
        res=["Credited"]
    else:
        res=["Pending"]
    client.close()
    return jsonify(res),200

# This api is used by account department to update the salary and bonus of a particular employee type
# Input -> {"e_type": ,"Salary": ,"Bonus": } //make sure all the values are string
# Output -> empty json string with return status 200
@app.route('/update_salary_bonus',methods=['POST'])
def update_sb():
    etype = request.json['e_type']
    salary = request.json['Salary']
    bonus = request.json['Bonus']
    client = MongoClient()
    db = client['employee_management_db']
    det = db.account_department_table
    res = list(det.find({'e_type':etype}))
    if(len(res) == 0):
        data = {'e_type':etype,'Salary':salary,'Bonus':bonus}
        det.insert_one(data)
        client.close()
        return jsonify({}),200
    det.update({'e_type':etype},{"$set":{'Salary':salary,'Bonus':bonus}})
    client.close()
    return jsonify({}),200


@app.route('/get_dept_id<string:e_id>', methods=['GET'])   
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

@app.route('/get_e_type<string:e_id>', methods=['GET'])   
def get_dept_id(e_id):
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
