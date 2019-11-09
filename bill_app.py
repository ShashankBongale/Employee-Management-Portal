#Bill apps

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
