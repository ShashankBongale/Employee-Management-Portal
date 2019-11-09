#salary and bonus 

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

if __name__ == '__main__':
    app.run("0.0.0.0",port=5000)
