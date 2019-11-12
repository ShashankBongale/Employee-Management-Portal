#app.py

"""
1. @app.route('/update_calendar',methods=['POST'])
2. @app.route('/login',methods=['POST'])
3. @app.route('/register',methods=['POST'])
4. @app.route('/get_leave_data/<string:empId>',methods=['GET'])
5. @app.route('/get_emp_details/<string:empId>',methods=['GET'])
6. @app.route('/get_leaves/<string:deptId>',methods=['GET'])
7. @app.route('/apply_leave',methods=['POST'])
8. @app.route('/approve_leave',methods=['POST'])
9. @app.route('/display_etypes',methods=['GET'])
10. @app.route('/initiate-salary-process',methods=['POST'])
11. @app.route('/get_leave_applications/<string:approver_id>',methods=['GET'])
12. @app.route('/get_bonus_status/<string:approver_id>',methods=['GET'])
13. @app.route('/approve_bonus',methods=['POST'])
14. @app.route('/check_salary_status',methods=['GET'])
15. @app.route('/update_salary_bonus',methods=['POST'])
16. @app.route('/get_dept_id/<string:e_id>', methods=['GET']) 
17. @app.route('/get_e_type/<string:e_id>', methods=['GET']) 
18. @app.route('/display_salary/<string:empID>',methods=['GET'])
19. @app.route('/apply_bill',methods=['POST'])
20. @app.route('/view_bill_status/<string:empid>',methods=['GET'])
21. @app.route('/view_all_bills',methods=['GET'])
22. @app.route('/process_bill',methods=['POST'])
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


# Manager enters New Employees Name, default password, dept_id of employee, e_type of employee,
# contact number and email id and approver_id
@app.route('/register',methods=['POST'])
def register():
    usr = request.json["user_name"]
    password = request.json["password"]
    dept = request.json["dept_id"]
    number = request.json["e_contact"]
    email = request.json["e_email"]
    etype = request.json["e_type"]
    approver = request.json["approver_id"]

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
        #insert into login table
        data = {'e_id':id,'user_name':usr,'password':password}
        db.login_table.insert_one(data)
        #insert into employee_details_table
        leavelist = list(db.calendar_table.find({'dept_id':dept,'e_type':etype}))
        leaves = dict()
        leaves['casual'] = leavelist[0]['casual']
        leaves['earned'] = leavelist[0]['earned']
        leaves['medical'] = leavelist[0]['medical']
        data = {'e_id':id,'user_name':usr,'e_contact':number,'e_email':email,'e_type':etype,'dept_id':dept,'leave_left':leaves,'approver_id':approver}
        db.employee_details_table.insert_one(data)
        #insert into salary_detail_table
        data = {'e_id':id,'last_salary_credited':"",'reimbursed_amt':0,'last_bonus_credited':""}
        db.salary_detail_table.insert_one(data)
        client.close()
        return jsonify({}),200
    client.close()
    return jsonify({}),400

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

# This api gives salary status for this month,bonus status of this month
# Input -> given through url http://127.0.0.1:5000/empID
#Output -> {"Salary": "1,20,0000", "bonus_amount": "2,16,000", "bonus_status": "false", "salary_status": "true"}
@app.route('/display_salary/<string:empID>',methods=['GET'])
def displaySalary(empID):
    client = MongoClient()
    db = client['employee_management_db']
    account_det = db.salary_detail_table
    res = list(account_det.find({'e_id':empID}))
    bonus_credited_date = res[0]['last_bonus_credited']
    if(bonus_credited_date != ""):
        bonus_year = bonus_credited_date.split('/')[2]
    else:
        bonus_year = "1970"
    salary_credited_date = res[0]['last_salary_credited']
    now = datetime.datetime.now()
    month = str(now.month)
    year = str(now.year)
    d = dict()
    last_salary_list = salary_credited_date.split('/')
    if(month == last_salary_list[1] and year == last_salary_list[2]):
        d["salary_status"] = "true"
    else:
        d["salary_status"] = "false"
    emp_det = db.employee_details_table
    res = list(emp_det.find({'e_id':empID}))
    emp_type = res[0]['e_type']
    account_det = db.account_department_table
    res = list(account_det.find({'e_type':emp_type}))
    salary_amount = res[0]['Salary']
    d["Salary"] = salary_amount
    bonus_amount = res[0]['Bonus']
    if(bonus_year == year):
        d["bonus_status"] = "true"
    else:
        d["bonus_status"] = "false"
    d["bonus_amount"] = bonus_amount
    return jsonify(d),200

###Bill APIs ###

@app.route('/apply_bill',methods=['POST'])
def applybill():
    eid = request.json['e_id']
    image = request.json['bill_image']
    amount = int(request.json['bill_amount'])
    bill_id = -1
    client = MongoClient()
    db = client['employee_management_db']
    det = db.bills_table
    all_rows = list(det.find())
    for i in all_rows:
        if(int(i['bill_id']) > bill_id):
            bill_id = int(i['bill_id'])
    bill_id = bill_id + 1
    data = dict()
    data['bill_image'] = image
    data['bill_amount'] = str(amount)
    data['e_id'] = eid
    data['bill_id'] = str(bill_id)
    emp_det = db.employee_details_table
    res = list(emp_det.find({'e_id':eid}))
    rem_amt = int(res[0]['reamt'])
    if(rem_amt >= amount):
        data['status'] = "pending"
        #emp_det.update({'e_id':eid},{"$set":{'reamt':str(rem_amt - amount)}})
        return_response = 200
    else:
        data['status'] = "rejected"
        return_response = 400
    det.insert_one(data)
    client.close()
    return jsonify({}),return_response

@app.route('/view_bill_status/<string:empid>',methods=['GET'])
def view_bill_status(empid):
    bills = []
    client = MongoClient()
    db = client['employee_management_db']
    bill_info = db.bills_table
    res = list(bill_info.find({'e_id':empid}))
    for i in res:
        temp = dict()
        temp['bill_image'] = i['bill_image']
        temp['bill_amount'] = i['bill_amount']
        temp['status'] = i['status']
        bills.append(temp)
    client.close()
    return jsonify(bills),200

@app.route('/view_all_bills',methods=['GET'])
def view_all_bills():
    client = MongoClient()
    bills = []
    db = client['employee_management_db']
    bill_info = db.bills_table
    res = list(bill_info.find({'status':'pending'}))
    for i in res:
        temp = dict()
        for j in i:
            if(j != '_id'):
                temp[j] = i[j]
        bills.append(temp)
    client.close()
    return jsonify(bills),200

@app.route('/process_bill',methods=['POST'])
def process_bill():
    bill_id = request.json['bill_id']
    bill_status = request.json['bill_status']
    client = MongoClient()
    db = client['employee_management_db']
    bill_info = db.bills_table
    bill_info.update({'bill_id':bill_id},{'$set':{'status':bill_status}})
    client.close()
    return jsonify({}),200

if __name__ == '__main__':
    app.run("0.0.0.0",port=5000)
