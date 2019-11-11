#app.py
from flask import Flask, jsonify, request, abort
from pymongo import MongoClient
import requests
import re
from datetime import date
import datetime
import pickle

import random
from datetime import timedelta
time_coef = 250

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

@app.route('/update_calendar',methods=['POST'])
def update_calendar_info():
    deptId = request.json["dept_id"]
    eType = request.json["e_type"]
    client = MongoClient()
    db = client['employee_management_db']
    department_details = db.department_table
    res = list(department_details.find({'dept_id':deptId}))
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

@app.route('/login',methods=['GET'])
def check_login():
    usr = request.json["user_name"]
    password = request.json["password"]
    client = MongoClient()
    db = client['employee_management_db']
    ld = db.login_table
    res = ld.find({'user_name':usr})
    for i in res:
        if(i['user_name'] == usr and i['password'] == password):
            client.close()
            return jsonify({}),200
    client.close()
    return jsonify({}),400

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
@app.route('/display_etypes',methods=['GET'])
def display_etypes():
	client = MongoClient()
	db = client['employee_management_db']
	res = db["e_type"]
	client.close()
	return jsonify(res),200

#Part 2 of initiate-salary-process which takes in selected e-types and updates credited date for every employee in selected type
@app.route('/initiate-salary-process',methods=['POST'])
def initiate_salary_process(etypes):
    client = MongoClient()
    db = client['employee_management_db']
    today = date.today()
    employees = db.employee_collection_table
    for e in etypes:
        emps = employees.find({'e_type':e})
    for i in emps:
        record = db.salary_detail_table.find({'e_id':i})
        record['last_salary_credited'] = today.strftime("%d/%m/%Y")
    client.close()
    return jsonify({}),200


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

@app.route('/check_salary_status',methods=['GET'])
def check_salary_status():
    client = MongoClient()
    db = client['employee_management_db']
    sal = db['salary_detail_table']
    sal_month = sal['last_salary_credited'].split('/')[1]
    today = date.today().strftime("%d/%m/%Y")
    curr_month = today.split('/')[1]
    if(curr_month==sal_month):
        res="Credited"
    else:
        res="Pending"
    client.close()
    return jsonify(res),200

# cab APIs

@app.route('/schedule_login',methods=['POST'])
def login():
    client = MongoClient()
    db = client['employee_management_db']
    employee_cab_details = db.emp_cab_detail_table
    emp_cab_data = list(employee_cab_details.find())
    data = [[x['e_id'],x['location'],x['distance'],x['slope'],x['login'],x['logout'],x['login_cab'],x['logout_cab']] for x in emp_cab_data ]
    employee_cab_details.update_many({},{"$set": {'logout_cab':0}})
    data_5 = [i for i in data if(i[4] == 5)]
    data_8 = [i for i in data if(i[4] == 8)]
    data_11 = [i for i in data if(i[4] == 11)]
    
    cab_data = schedule_login(data_5)
    for x in data_5:
        employee_cab_details.update({'e_id':x[0]},{"$set": {'login_cab':x[6]}})

    cab_data = schedule_login(data_8)
    for x in data_8:
        employee_cab_details.update({'e_id':x[0]},{"$set": {'login_cab':x[6]}})

    cab_data = schedule_login(data_11)
    for x in data_11:
        employee_cab_details.update({'e_id':x[0]},{"$set": {'login_cab':x[6]}})

    return jsonify({'status':'scheduled successfully'}),200

def schedule_login(data):
    if(len(data) == 0):
        print("empty")
        cab_data = []
    else:
        data.sort(key=lambda x:x[3])
        cab_id = 1
        cab_data = []
        ind = 0
        login = data[0][4]
        while(ind<len(data)):
            temp = data[ind:ind+3]
            cab = {}
            cab["cabId"] = cab_id
            distances = [temp[i][2] for i in range(len(temp))]
            if(len(temp) == 3):
                first = distances.index(max(distances))
                last = distances.index(min(distances))
                second = (3-(first+last))
                order = "passenger" + str(first+1) + " -> passenger" + str(second+1) + " -> passenger" + str(last+1)
            elif(len(temp) == 2):
                first = distances.index(max(distances))
                last = distances.index(min(distances))
                order = "passenger" + str(first+1) + " -> passenger" + str(last+1)
            else:
                order = "passenger1"

            cab["pickupOrder"] = order
            for i in range(len(temp)):
                passenger = {}
                passenger["e_id"] = temp[i][0]
                passenger["location"] = temp[i][1]
                passenger["distance"] = temp[i][2]
                cab["passenger" + str(i+1) + "Details"] = passenger
            time = str(timedelta(minutes=((login*60) - (max(distances)*time_coef))))[:4]
            cab["startTime"] = time
            cab["endTime"] = str(timedelta(minutes=(login*60)))[:4]
            cab_data.append(cab)
            for y in range(ind,len(data))[0:3]:
                data[y][6] =  cab_id 
            cab_id += 1
            ind+=3
    return cab_data        
        

@app.route('/schedule_logout',methods=['POST'])
def logout():
    client = MongoClient()
    db = client['employee_management_db']
    employee_cab_details = db.emp_cab_detail_table
    emp_cab_data = list(employee_cab_details.find())
    data = [[x['e_id'],x['location'],x['distance'],x['slope'],x['login'],x['logout'],x['login_cab'],x['logout_cab']] for x in emp_cab_data ]
    employee_cab_details.update_many({},{"$set": {'login_cab':0}})
    data_15 = [i for i in data if(i[5] == 5)]
    data_18 = [i for i in data if(i[5] == 18)]
    data_21 = [i for i in data if(i[5] == 21)]
    
    cab_data = schedule_logout(data_15)
    for x in data_15:
        employee_cab_details.update({'e_id':x[0]},{"$set": {'logout_cab':x[7]}})

    cab_data = schedule_logout(data_18)
    for x in data_18:
        employee_cab_details.update({'e_id':x[0]},{"$set": {'logout_cab':x[7]}})
        
    cab_data = schedule_logout(data_21)
    for x in data_21:
        employee_cab_details.update({'e_id':x[0]},{"$set": {'logout_cab':x[7]}})

    return jsonify({'status':'scheduled successfully'}),200

def schedule_logout(data):
    if(len(data) == 0):
        print("empty")
        cab_data = []
    else:
        data.sort(key=lambda x:x[3],reverse=True)
        cab_id = 1
        cab_data = []
        ind = 0
        logout = data[0][5]
        while(ind<len(data)):
            temp = data[ind:ind+3]
            cab = {}
            cab["cabId"] = cab_id
            distances = [temp[i][2] for i in range(len(temp))]
            if(len(temp) == 3):
                first = distances.index(min(distances))
                last = distances.index(max(distances))
                second = (3-(first+last))
                order = "passenger" + str(first+1) + " -> passenger" + str(second+1) + " -> passenger" + str(last+1)
            elif(len(temp) == 2):
                first = distances.index(min(distances))
                last = distances.index(max(distances))
                order = "passenger" + str(first+1) + " -> passenger" + str(last+1)
            else:
                order = "passenger1"

            cab["pickupOrder"] = order
            for i in range(len(temp)):
                passenger = {}
                passenger["e_id"] = temp[i][0]
                passenger["location"] = temp[i][1]
                passenger["distance"] = temp[i][2]
                cab["passenger" + str(i+1) + "Details"] = passenger
            cab["startTime"] = str(timedelta(minutes=(logout*60)))[:5]
            time = str(timedelta(minutes=((logout*60) + (max(distances)*time_coef))))[:5]
            cab["endTime"] = time
            cab_data.append(cab)
            for y in range(ind,len(data))[0:3]:
                data[y][7] =  cab_id 
            cab_id += 1
            ind+=3
    return cab_data

@app.route('/book_login',methods=['POST'])
def book_login():
	emp_id=request.json["e_id"]
	login_time=request.json["login"]
	client=MongoClient()
	db=client['employee_management_db']
	emp_cab_det=db.emp_cab_detail_table
	emp_cab_det.update({'e_id':emp_id},{"$set": {'login':login_time}})

	return jsonify({'status':'booked successfully'}),200

@app.route('/book_logout',methods=['POST'])
def book_logout():
	emp_id=request.json["e_id"]
	logout_time=request.json["logout"]
	client=MongoClient()
	db=client['employee_management_db']
	emp_cab_det=db.emp_cab_detail_table
	emp_cab_det.update({'e_id':emp_id},{"$set": {'logout':logout_time}})

	return jsonify({'status':'booked successfully'}),200

@app.route('/cancel_login',methods=['POST'])
def cancel_login():
	emp_id=request.json['e_id']
	client=MongoClient()
	db=client['employee_management_db']
	emp_cab_det=db.emp_cab_detail_table
	emp_cab_det.update({'e_id':emp_id},{"$set": {'login':0}})
	emp_cab_det.update({'e_id':emp_id},{"$set": {'login_cab':0}})
	return jsonify({'status':'cancelled'}),200

@app.route('/cancel_logout',methods=['POST'])
def cancel_logout():
	emp_id=request.json['e_id']
	client=MongoClient()
	db=client['employee_management_db']
	emp_cab_det=db.emp_cab_detail_table
	emp_cab_det.update({'e_id':emp_id},{"$set": {'logout':0}})
	emp_cab_det.update({'e_id':emp_id},{"$set": {'logout_cab':0}})
	return jsonify({'status':'cancelled'}),200

@app.route('/show_cab_details_login',methods=['POST'])
def show_cab_details_login():
	emp_id=request.json['e_id']
	client=MongoClient()
	db=client['employee_management_db']
	emp_cab_det=db.emp_cab_detail_table
	cab_driver_info_detail=db.cab_driver_info_detail_table
	emp_cab_info=list(emp_cab_det.find({'e_id':emp_id}))
	login_cab_id=emp_cab_info[0]['login_cab']
	# print("cab_id ================",login_cab_id)
	if(emp_cab_info[0]['login'] != 0 and login_cab_id != 0):
		cab_info=list(cab_driver_info_detail.find({'cab_id':login_cab_id}))
		driver_name=cab_info[0]['driver_name']
		driver_number=cab_info[0]['driver_number']
		cab_number=cab_info[0]['cab_no']
		return jsonify({'driver_name':driver_name,'driver_number':driver_number,'cab_number':cab_number}),200
	else:
		return jsonify({'status':'cab not allocated'}),400	

@app.route('/show_cab_details_logout',methods=['POST'])
def show_cab_details_logout():
	emp_id=request.json['e_id']
	client=MongoClient()
	db=client['employee_management_db']
	emp_cab_det=db.emp_cab_detail_table
	cab_driver_info_detail=db.cab_driver_info_detail_table
	emp_cab_info=list(emp_cab_det.find({'e_id':emp_id}))
	logout_cab_id=emp_cab_info[0]['logout_cab']
	# print("cab_id ================",logout_cab_id)
	if(emp_cab_info[0]['logout'] != 0 and logout_cab_id != 0):
		cab_info=list(cab_driver_info_detail.find({'cab_id':logout_cab_id}))
		driver_name=cab_info[0]['driver_name']
		driver_number=cab_info[0]['driver_number']
		cab_number=cab_info[0]['cab_no']
		return jsonify({'driver_name':driver_name,'driver_number':driver_number,'cab_number':cab_number}),200
	else:
		return jsonify({'status':'cab not allocated'}),400	


  
if __name__ == '__main__':
    app.run("0.0.0.0",port=5000,debug=True)
