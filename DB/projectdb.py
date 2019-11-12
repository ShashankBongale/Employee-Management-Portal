from pymongo import MongoClient
import json
client = MongoClient()
db = client['employee_management_db']

#2.Login Collection
login_details = db.login_table
data1 = {'e_id':'2019DEV001','user_name':'Rahul','password':'E5857B335AFDF35CA81A110BC81F38682F8A89892CC597F5398DFEF82D42B513'}
data2 = {'e_id':'2019DEV002','user_name':'Raghav','password':'9425C3AE8CF81E1475108C7CA9ACF70B5DF3FEAB935C1910DD0E618FB431DDA0'}
data3 = {'e_id':'2019DEV003','user_name':'Sagar','password':'CFC2BB2D953B68C45D2711E542076A8F47C1A37778CF8A9CC117F087A5FDDE9F'}
data4 = {'e_id':'2019FIN001','user_name':'Ashu','password':'5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'}
data5 = {'e_id':'2019FIN002','user_name':'Ashish','password':'1282c71af676e24d8ab3202ad4e4264655f2238e0e1e82d138041f5721108653'}
data6 = {'e_id':'2019FIN003','user_name':'Alisha','password':'fb2471d9606c6e3c2ab1eb5316f47b39c5d56262c3dafa7c991e8310150cc513'}
data7 = {'e_id':'2019HRD001','user_name':'Ayushi','password':'4f278cdddf52263fe21c64c94932f2b2ec316acecd39a7adcc01eb2e6592a678'}
data8 = {'e_id':'2019HRD002','user_name':'Deepika','password':'27223c7bdb7362a30b4d84254bc6e555f9bf0467b9796f6e9d62e47633dc29b3'}
data9 = {'e_id':'2019HRD002','user_name':'Purva','password':'a0e58d8fb7d8dd44330b1a55ba190043e931617546d6c06c4bef4c2e77331642'}
login_details.insert_many([data1,data2,data3,data4,data5,data6,data7,data8,data9])

#4.Deapartment
dept_details = db.department_table
data1 = {'dept_id':'DEVBNG','hod_id':'2019DEV001','dept_name':'Development','total_employees':'30','min_employees':'17'}
data2 = {'dept_id':'FINDEP','hod_id':'2019FIN001','dept_name':'Finance','total_employees':'25','min_employees':'14'}
data3 = {'dept_id':'HRDEPT','hod_id':'2019HRD001','dept_name':'Human Resource','total_employees':'10','min_employees':'7'}
dept_details.insert_many([data1,data2,data3])

#5.Calendar
calendar_details = db.calendar_table
data1 = {'dept_id':'DEVBNG','e_type':'DEV','casual':'8','earned':'10','medical':'6'}
data2 = {'dept_id':'DEVBNG','e_type':'MANAGER','casual':'10','earned':'12','medical':'8'}
data3 = {'dept_id':'DEVBNG','e_type':'HOD','casual':'12','earned':'14','medical':'10'}
data4 = {'dept_id':'FINDEP','e_type':'ACCOUNTANT','casual':'8','earned':'10','medical':'6'}
data5 = {'dept_id':'FINDEP','e_type':'MANAGER','casual':'10','earned':'12','medical':'8'}
data6 = {'dept_id':'FINDEP','e_type':'HOD','casual':'12','earned':'14','medical':'10'}
data7 = {'dept_id':'HRDEPT','e_type':'HR','casual':'8','earned':'10','medical':'6'}
data8 = {'dept_id':'HRDEPT','e_type':'HR MANAGER','casual':'10','earned':'12','medical':'8'}
data9 = {'dept_id':'HRDEPT','e_type':'HOD','casual':'12','earned':'14','medical':'10'}
calendar_details.insert_many([data1,data2,data3,data4,data5,data6,data7,data8,data9])

#1.Employee Collection
employee_details = db.employee_details_table
data1 = {'e_id':'2019DEV001','user_name':'Rahul','e_contact':'8887712120','e_email':'rahul@gmail.com','e_type':'HOD','dept_id':'DEVBNG','leave_left':{'casual':'12','earned':'14','medical':'10'},'approver_id':'2019DEV001','reamt':'8000'}
data2 = {'e_id':'2019DEV002','user_name':'Raghav','e_contact':'8898513120','e_email':'raghav123@gmail.com','e_type':'MANAGER','dept_id':'DEVBNG','leave_left':{'casual':'10','earned':'12','medical':'8'},'approver_id':'2019DEV001','reamt':'6000'}
data3 = {'e_id':'2019DEV003','user_name':'Sagar','e_contact':'9992212120','e_email':'sagar@gmail.com','e_type':'DEV','dept_id':'DEVBNG','leave_left':{'casual':'8','earned':'10','medical':'6'},'approver_id':'2019DEV002','reamt':'4000'}
data4 = {'e_id':'2019FIN001','user_name':'Ashu','e_contact':'8892267120','e_email':'ashu12@gmail.com','e_type':'HOD','dept_id':'FINDEP','leave_left':{'casual':'12','earned':'14','medical':'10'},'approver_id':'2019FIN001','reamt':'8000'}
data5 = {'e_id':'2019FIN002','user_name':'Ashish','e_contact':'8792212039','e_email':'ashish67@gmail.com','e_type':'MANAGER','dept_id':'FINDEP','leave_left':{'casual':'10','earned':'12','medical':'8'},'approver_id':'2019FIN001','reamt':'6000'}
data6 = {'e_id':'2019FIN003','user_name':'Alisha','e_contact':'8555755287','e_email':'alisha26@gmail.com','e_type':'ACCOUNTANT','dept_id':'FINDEP','leave_left':{'casual':'8','earned':'10','medical':'6'},'approver_id':'2019FIN002','reamt':'4000'}
data7 = {'e_id':'2019HRD001','user_name':'Ayushi','e_contact':'9430712120','e_email':'ayushi@gmail.com','e_type':'HOD','dept_id':'HRDEPT','leave_left':{'casual':'12','earned':'14','medical':'10'},'approver_id':'2019HRD001','reamt':'8000'}
data8 = {'e_id':'2019HRD002','user_name':'Deepika','e_contact':'9835513120','e_email':'deepika007@gmail.com','e_type':'MANAGER','dept_id':'HRDEPT','leave_left':{'casual':'10','earned':'12','medical':'8'},'approver_id':'2019HRD001','reamt':'6000'}
data9 = {'e_id':'2019HRD003','user_name':'Purva','e_contact':'9939212120','e_email':'purva001@gmail.com','e_type':'HR','dept_id':'HRDEPT','leave_left':{'casual':'8','earned':'10','medical':'6'},'approver_id':'2019HRD002','reamt':'4000'}

employee_details.insert_many([data1,data2,data3,data4,data5,data6,data7,data8,data9])

#3.Leave Collection
leave_col = db.leave_collection_table
data1 = {'e_id':'2019DEV003','type':'medical','list_of_dates':['29/10/2019','30/10/2019'],'reason':'medical leave','status':'pending'}
data2 = {'e_id':'2019DEV001','type':'casual','list_of_dates':['26/10/2019','28/10/2019','29/10/2019'],'reason':'casual leave','status':'pending'}
data3 = {'e_id':'2019FIN002','type':'casual','list_of_dates':['2/11/2019'],'reason':'casual leave','status':'pending'}
data4 = {'e_id':'2019HRD002','type':'medical','list_of_dates':['22/10/2019','23/10/2019','24/10/2019','25/10/2019'],'reason':'medical leave','status':'pending'}
leave_col.insert_many([data1,data2,data3,data4])

#6.Account Department
account_det=db.account_department_table
data1={'e_type':'DEV','Salary':'60,000','Bonus':'1,08,000','reamt':'4000'}
data2={'e_type':'MANAGER','Salary':'90,000','Bonus':'1,62,000','reamt':'6000'}
data3={'e_type':'HOD','Salary':'1,20,0000','Bonus':'2,16,000','reamt':'8000'}
data4={'e_type':'ACCOUNTANT','Salary':'65,000','Bonus':'1,17,000','reamt':'4000'}
data5={'e_type':'HR','Salary':'70,000','Bonus':'1,26,000','reamt':'4000'}
account_det.insert_many([data1,data2,data3,data4,data5])

#7.Salary
salary_det=db.salary_detail_table
data1={'e_id':'2019DEV001','last_salary_credited':'2/09/2019','reimbursed_amt':'6,000','last_bonus_credited':""}
data2={'e_id':'2019DEV002','last_salary_credited':'2/09/2019','reimbursed_amt':'6,000','last_bonus_credited':""}
data3={'e_id':'2019DEV003','last_salary_credited':'2/09/2019','reimbursed_amt':'2,500','last_bonus_credited':""}
data4={'e_id':'2019FIN001','last_salary_credited':'2/09/2019','reimbursed_amt':'6,000','last_bonus_credited':""}
data5={'e_id':'2019FIN002','last_salary_credited':'2/09/2019','reimbursed_amt':'6,000','last_bonus_credited':""}
data6={'e_id':'2019FIN003','last_salary_credited':'2/09/2019','reimbursed_amt':'6,000','last_bonus_credited':""}
data7={'e_id':'2019HRD001','last_salary_credited':'2/09/2019','reimbursed_amt':'4,500','last_bonus_credited':""}
data8={'e_id':'2019HRD002','last_salary_credited':'2/09/2019','reimbursed_amt':'8,000','last_bonus_credited':""}
data9={'e_id':'2019HRD003','last_salary_credited':'2/09/2019','reimbursed_amt':'6,000','last_bonus_credited':""}
salary_det.insert_many([data1,data2,data3,data4,data5,data6,data7,data8,data9])

#8.Bills 
bills_info = db.bills_table
data1 = {'e_id':'2019DEV001','bill_id':'1','bill_image':'','bill_amount':'0','status':'pending'}
bills_info.insert_one(data1)

#9.Data for ML
with open('final_data.json') as json_file:
    data = json.load(json_file)
ml_data = db.ml_data_table
ml_data.insert_one(data)

