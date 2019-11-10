from pymongo import MongoClient
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
data1 = {'e_id':'2019DEV001','user_name':'Rahul','e_contact':'8887712120','e_email':'rahul@gmail.com','e_type':'HOD','dept_id':'DEVBNG','leave_left':{'casual':'12','earned':'14','medical':'10'},'approver_id':'2019DEV001'}
data2 = {'e_id':'2019DEV002','user_name':'Raghav','e_contact':'8898513120','e_email':'raghav123@gmail.com','e_type':'MANAGER','dept_id':'DEVBNG','leave_left':{'casual':'10','earned':'12','medical':'8'},'approver_id':'2019DEV001'}
data3 = {'e_id':'2019DEV003','user_name':'Sagar','e_contact':'9992212120','e_email':'sagar@gmail.com','e_type':'DEV','dept_id':'DEVBNG','leave_left':{'casual':'8','earned':'10','medical':'6'},'approver_id':'2019DEV002'}
data4 = {'e_id':'2019FIN001','user_name':'Ashu','e_contact':'8892267120','e_email':'ashu12@gmail.com','e_type':'HOD','dept_id':'FINDEP','leave_left':{'casual':'12','earned':'14','medical':'10'},'approver_id':'2019FIN001'}
data5 = {'e_id':'2019FIN002','user_name':'Ashish','e_contact':'8792212039','e_email':'ashish67@gmail.com','e_type':'MANAGER','dept_id':'FINDEP','leave_left':{'casual':'10','earned':'12','medical':'8'},'approver_id':'2019FIN001'}
data6 = {'e_id':'2019FIN003','user_name':'Alisha','e_contact':'8555755287','e_email':'alisha26@gmail.com','e_type':'ACCOUNTANT','dept_id':'FINDEP','leave_left':{'casual':'8','earned':'10','medical':'6'},'approver_id':'2019FIN002'}
data7 = {'e_id':'2019HRD001','user_name':'Ayushi','e_contact':'9430712120','e_email':'ayushi@gmail.com','e_type':'HOD','dept_id':'HRDEPT','leave_left':{'casual':'12','earned':'14','medical':'10'},'approver_id':'2019HRD001'}
data8 = {'e_id':'2019HRD002','user_name':'Deepika','e_contact':'9835513120','e_email':'deepika007@gmail.com','e_type':'HR MANAGER','dept_id':'HRDEPT','leave_left':{'casual':'10','earned':'12','medical':'8'},'approver_id':'2019HRD001'}
data9 = {'e_id':'2019HRD003','user_name':'Purva','e_contact':'9939212120','e_email':'purva001@gmail.com','e_type':'HR','dept_id':'HRDEPT','leave_left':{'casual':'8','earned':'10','medical':'6'},'approver_id':'2019HRD002'}

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
data1={'e_type':'DEV','Salary':'60,000','Bonus':'1,08,000'}
data2={'e_type':'MANAGER','Salary':'90,000','Bonus':'1,62,000'}
data3={'e_type':'HOD','Salary':'1,20,0000','Bonus':'2,16,000'}
data4={'e_type':'ACCOUNTANT','Salary':'65,000','Bonus':'1,17,000'}
data5={'e_type':'MANAGER','Salary':'90,000','Bonus':'1,62,000'}
data6={'e_type':'HOD','Salary':'1,20,000','Bonus':'2,16,000'}
data7={'e_type':'HR','Salary':'70,000','Bonus':'1,26,000'}
data8={'e_type':'HR MANAGER','Salary':'90,000','Bonus':'1,62,000'}
data9={'e_type':'HOD','Salary':'1,20,000','Bonus':'2,16,000'}
account_det.insert_many([data1,data2,data3,data4,data5,data6,data7,data8,data9])

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

#Employee_cab_details
emp_cab_det=db.emp_cab_detail_table
data =[{'e_id': '2019DEV001', 'location': (12.7502, 77.2129), 'distance': 0.44126279018289843, 'slope': 1.7240289069557067, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV002', 'location': (12.8724, 77.908), 'distance': 0.32872511312645536, 'slope': -3.15927419354841, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV003', 'location': (13.1456, 77.5775), 'distance': 0.17483823952442382, 'slope': -0.09827586206896137, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV004', 'location': (12.7456, 77.7833), 'distance': 0.29442094015201997, 'slope': -0.8349557522123738, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV005', 'location': (13.2504, 78.1281), 'distance': 0.6019565515882389, 'slope': 1.9135581061693074, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV006', 'location': (13.3579, 77.6057), 'distance': 0.3864594415976924, 'slope': 0.028734144447318123, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV007', 'location': (12.5684, 78.0089), 'distance': 0.5781130771743515, 'slope': -1.027529761904755, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV008', 'location': (12.7789, 78.0312), 'distance': 0.4772345859218492, 'slope': -2.265697976128686, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019DEV009', 'location': (12.5703, 78.0871), 'distance': 0.6352935856751644, 'slope': -1.2272614004485565, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV010', 'location': (12.8903, 77.9267), 'distance': 0.34190656618438625, 'slope': -4.0848708487084195, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV011', 'location': (13.0176, 77.1744), 'distance': 0.42271035000339774, 'slope': -9.134782608695648, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV012', 'location': (12.3236, 77.4969), 'distance': 0.6553238054580348, 'slope': 0.15077160493827665, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV013', 'location': (13.346, 77.5538), 'distance': 0.3766165158354053, 'slope': -0.1089743589743708, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV014', 'location': (13.378, 77.3184), 'distance': 0.49137297442981265, 'slope': -0.6796259842519762, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV015', 'location': (13.3886, 77.6205), 'distance': 0.417803554317098, 'slope': 0.06211031175061667, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV016', 'location': (12.7761, 77.6291), 'distance': 0.19852077976876867, 'slope': -0.17647058823526365, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV017', 'location': (13.3441, 77.7652), 'distance': 0.40970795696446605, 'slope': 0.4579865771811914, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV018', 'location': (12.5944, 77.214), 'distance': 0.5358509121014922, 'slope': 1.0090137857900343, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV019', 'location': (13.1572, 77.5132), 'distance': 0.20266553727755493, 'slope': -0.4385775862069102, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV020', 'location': (12.4301, 77.9105), 'distance': 0.6269091321714819, 'slope': -0.583379501385039, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019DEV021', 'location': (13.0698, 77.8593), 'distance': 0.2823284080640887, 'slope': 2.6955193482688804, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019DEV022', 'location': (12.4315, 77.8683), 'distance': 0.6054912881289074, 'slope': -0.5067580077763466, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV023', 'location': (12.6623, 77.8427), 'distance': 0.3965098989937037, 'slope': -0.8021338506304349, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV024', 'location': (12.3347, 77.2363), 'distance': 0.730767062749821, 'slope': 0.56256869210237, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019DEV025', 'location': (13.2644, 77.886), 'distance': 0.4130929677445471, 'slope': 0.9952185792349596, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV026', 'location': (12.3353, 78.1737), 'distance': 0.8603688162642791, 'slope': -0.9101052962439047, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV027', 'location': (12.4561, 77.2325), 'distance': 0.6299656022355505, 'slope': 0.7024248302618764, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV028', 'location': (12.4078, 77.9883), 'distance': 0.6876555314981455, 'slope': -0.6982972685349328, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV029', 'location': (12.5493, 77.8515), 'distance': 0.49430243778480476, 'slope': -0.6083353066540416, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019DEV030', 'location': (12.929, 77.5867), 'distance': 0.04332631994527251, 'slope': 0.18544600938982211, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN001', 'location': (12.5156, 77.9694), 'distance': 0.5902635343640976, 'slope': -0.8219298245613866, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN002', 'location': (12.5854, 77.3569), 'distance': 0.4534884011747183, 'slope': 0.6154842050750996, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN003', 'location': (12.8525, 78.0653), 'distance': 0.485534035882135, 'slope': -3.952141057934412, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN004', 'location': (12.7189, 77.3031), 'distance': 0.3857843179809153, 'slope': 1.1535417491096094, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN005', 'location': (12.7477, 77.222), 'distance': 0.4346975615298576, 'slope': 1.6641357748995305, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN006', 'location': (12.6241, 77.4342), 'distance': 0.3827328180336757, 'slope': 0.46158273381293696, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN007', 'location': (12.9047, 77.2025), 'distance': 0.39776628816429305, 'slope': 5.8609865470851545, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN008', 'location': (12.3164, 78.1176), 'distance': 0.8383412431701048, 'slope': -0.7982295482295415, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN009', 'location': (13.1876, 77.2964), 'distance': 0.36821086350078847, 'slope': -1.3805555555555333, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN010', 'location': (12.6358, 77.3972), 'distance': 0.38952329840460276, 'slope': 0.5878499106611118, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN011', 'location': (13.0584, 78.1376), 'distance': 0.549893844300886, 'slope': 6.255760368663653, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN012', 'location': (12.9639, 77.755), 'distance': 0.16058471284651787, 'slope': -20.83116883116876, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019FIN013', 'location': (13.1541, 77.569), 'distance': 0.1842867602406629, 'slope': -0.14027397260272487, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN014', 'location': (12.7115, 77.4472), 'distance': 0.29896282377580335, 'slope': 0.5667051134179312, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019FIN015', 'location': (13.1292, 77.5455), 'distance': 0.1650714087902557, 'slope': -0.31154822335022575, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN016', 'location': (13.1716, 77.4251), 'distance': 0.2621645475650731, 'slope': -0.8474999999999996, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019FIN017', 'location': (12.4793, 78.0611), 'distance': 0.678219389283436, 'slope': -0.9475929311395414, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN018', 'location': (12.4325, 77.3952), 'distance': 0.5747948938534512, 'slope': 0.36987571879057074, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019FIN019', 'location': (12.465, 77.1126), 'distance': 0.6992621539880447, 'slope': 0.9514409790761917, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019FIN020', 'location': (12.4325, 77.4583), 'distance': 0.5560633956663601, 'slope': 0.25282878872195386, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019FIN021', 'location': (12.6765, 78.1789), 'distance': 0.6545918575723338, 'slope': -1.980006777363604, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN022', 'location': (12.7567, 77.3446), 'distance': 0.32966954666756837, 'slope': 1.16333178222429, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN023', 'location': (12.6804, 78.1419), 'distance': 0.6199473606686358, 'slope': -1.8794642857143105, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN024', 'location': (12.4456, 78.0059), 'distance': 0.6677152761469498, 'slope': -0.7819391634980937, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019FIN025', 'location': (12.4352, 77.8592), 'distance': 0.5981121299555805, 'slope': -0.49328859060402924, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN026', 'location': (13.2595, 78.0638), 'distance': 0.55048619419564, 'slope': 1.6297325460229344, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN027', 'location': (12.4157, 78.1419), 'distance': 0.7801039033359652, 'slope': -0.9845295916531855, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN028', 'location': (13.3043, 77.8771), 'distance': 0.43645794757341605, 'slope': 0.8491133152990671, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN029', 'location': (13.179, 77.8), 'distance': 0.29189710515864803, 'slope': 0.9903567984570759, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019FIN030', 'location': (12.3765, 78.0478), 'distance': 0.74802022031493, 'slope': -0.7615526802218032, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD001', 'location': (13.0004, 77.9519), 'distance': 0.3584588260874553, 'slope': 12.406249999999664, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD002', 'location': (13.1651, 77.8977), 'distance': 0.3595995828696141, 'slope': 1.5664082687338514, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD003', 'location': (12.7417, 77.7127), 'distance': 0.2584600936314926, 'slope': -0.5137016093953805, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD004', 'location': (13.3043, 77.4649), 'distance': 0.3570873562589403, 'slope': -0.3898406973249175, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD005', 'location': (13.1836, 77.6603), 'distance': 0.22194704323329198, 'slope': 0.3099056603773907, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD006', 'location': (12.6597, 78.1509), 'distance': 0.6377705700328231, 'slope': -1.7835844822058153, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD007', 'location': (12.9334, 77.5179), 'distance': 0.08568622993223798, 'slope': 2.007853403141436, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019HRD008', 'location': (12.7377, 77.4305), 'distance': 0.2857236777027793, 'slope': 0.7015818725951459, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019HRD009', 'location': (12.8921, 77.9406), 'distance': 0.3550158447168277, 'slope': -4.352201257861613, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019HRD010', 'location': (12.3803, 77.3845), 'distance': 0.6275170914007038, 'slope': 0.35531878910873826, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019HRD011', 'location': (13.2808, 77.5209), 'distance': 0.31786212419852666, 'slope': -0.2383570504527898, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD012', 'location': (12.6338, 77.6839), 'distance': 0.3494042501172514, 'slope': -0.26435760805208547, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019HRD013', 'location': (12.608, 77.3769), 'distance': 0.42379033731315435, 'slope': 0.5987348734873311, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD014', 'location': (12.3605, 77.6477), 'distance': 0.6134026573141012, 'slope': -0.08689248895434554, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD015', 'location': (13.2236, 77.1964), 'distance': 0.47124010864950966, 'slope': -1.580158730158748, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019HRD016', 'location': (13.3934, 78.1873), 'distance': 0.727467202009817, 'slope': 1.405168326220945, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD017', 'location': (12.368, 77.991), 'distance': 0.7221259723898594, 'slope': -0.6567263088137836, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD018', 'location': (12.9359, 77.7285), 'distance': 0.13857741518732128, 'slope': -3.750700280111931, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD019', 'location': (13.1875, 77.605), 'distance': 0.2161503411979724, 'slope': 0.04817044928209452, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD020', 'location': (13.1464, 77.753), 'distance': 0.23589319617148752, 'slope': 0.9061784897025221, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019HRD021', 'location': (13.2344, 77.4717), 'distance': 0.2901176485496884, 'slope': -0.46765601217656455, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD022', 'location': (12.5627, 77.1537), 'distance': 0.6013252198270085, 'slope': 1.0782587429689365, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD023', 'location': (12.4659, 77.408), 'distance': 0.5390288025699558, 'slope': 0.3689934743919284, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD024', 'location': (12.3426, 77.5455), 'distance': 0.6309134726727599, 'slope': 0.078060413354524, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD025', 'location': (13.3533, 77.9606), 'distance': 0.5288202813811135, 'slope': 0.9588682211160579, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD026', 'location': (13.391, 77.8947), 'distance': 0.5157095791237544, 'slope': 0.7155460181211273, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}, 
 {'e_id': '2019HRD027', 'location': (13.27, 77.6241), 'distance': 0.2998546481213846, 'slope': 0.09886058981232855, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD028', 'location': (12.3887, 77.4188), 'distance': 0.6088333515831724, 'slope': 0.3015954709212475, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD029', 'location': (12.5857, 77.2849), 'distance': 0.4948059215490504, 'slope': 0.8025395180098615, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''},
 {'e_id': '2019HRD030', 'location': (13.0283, 77.5101), 'distance': 0.10176020833312431, 'slope': -1.4902998236332734, 'login': 8, 'logout': 5, 'login_cab': '', 'logout_cab': ''}];
emp_cab_det.insert(data)

#Cab_Management
cab_detail=db.cab_detail_table
data=[{'cab_id': 'cab_0', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_1', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_2', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_3', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_4', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_5', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_6', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_7', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_8', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_9', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_10', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_11', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_12', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_13', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_14', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_15', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_16', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_17', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_18', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_19', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_20', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_21', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_22', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_23', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_24', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_25', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_26', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_27', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_28', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_29', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_30', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_31', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_32', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_33', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''},
      {'cab_id': 'cab_34', 'pickup_order': '', 'passenger1': '', 'passenger2': '', 'passenger3': '', 'start_time': '', 'end_time': ''}];
cab_detail.insert(data)

#Cab Information Detail
cab_info_detail=db.cab_info_detail_table
data=[{ 'cab_id' : 'cab_0' , 'driver_name' : 'RUPESH KUMAR' , 'cab_no' : 'KA 03 AA 0128' , 'driver_number' : '8021047360' },
{ 'cab_id' : 'cab_1' , 'driver_name' : 'JAYANT YADAV' , 'cab_no' : 'KA 11 JD 2975' , 'driver_number' : '9372859283' },
{ 'cab_id' : 'cab_2' , 'driver_name' : 'DUSHYANT GOWDA' , 'cab_no' : 'KA 04 MJ 690' , 'driver_number' : '7028472940' },
{ 'cab_id' : 'cab_3' , 'driver_name' : 'MOHAMMED SUHAIL' , 'cab_no' : 'KA17 CA 7780' , 'driver_number' : '9593953810' },
{ 'cab_id' : 'cab_4' , 'driver_name' : 'ARVIND KUMAR' , 'cab_no' : 'KA 11 J 2259' , 'driver_number' : '6028449201' },
{ 'cab_id' : 'cab_5' , 'driver_name' : 'SUJITH VERMA' , 'cab_no' : 'KA 42 Z 6240' , 'driver_number' : '8937375910' },
{ 'cab_id' : 'cab_6' , 'driver_name' : 'AMIT SINGH' , 'cab_no' : 'KA 05 DB 1184 ' , 'driver_number' : '7392059204' },
{ 'cab_id' : 'cab_7' , 'driver_name' : 'SANTHOSH KUMAR' , 'cab_no' : 'KA 18 IL 0032' , 'driver_number' : '8333819581' },
{ 'cab_id' : 'cab_8' , 'driver_name' : 'PRAJWAL GOWDA' , 'cab_no' : 'KA 36 JM 3358' , 'driver_number' : '9285988184' },
{ 'cab_id' : 'cab_9' , 'driver_name' : 'ABRAR ULLA KHAN' , 'cab_no' : 'KA 42 AL 786' , 'driver_number' : '7295917591' },
{ 'cab_id' : 'cab_10' , 'driver_name' : 'ARJUN S' , 'cab_no' : 'KA 04 PR 007' , 'driver_number' : '9844466897' },
{ 'cab_id' : 'cab_11' , 'driver_name' : 'DINESH YADAV' , 'cab_no' : 'KA 12 YZ 8385' , 'driver_number' : '8904550430' },
{ 'cab_id' : 'cab_12' , 'driver_name' : 'RAKSHITH J' , 'cab_no' : 'KA 05 QW 3729' , 'driver_number' : '9986512357' },
{ 'cab_id' : 'cab_13' , 'driver_name' : 'SHIVKUMAR' , 'cab_no' : 'KA 56 LO 7382' , 'driver_number' : '9986409361' },
{ 'cab_id' : 'cab_14 ', 'driver_name' : 'MANISH T' , 'cab_no' : 'KA 64 FU 5372' , 'driver_number' : '7019658239' },
{ 'cab_id' : 'cab_15' , 'driver_name' : 'JUNAID KHASIM' , 'cab_no' : 'KA 47 PQ 737' , 'driver_number' : '9900026128' },
{ 'cab_id' : 'cab_16' , 'driver_name' : 'DURGESH' , 'cab_no' : 'KA 29 FU 2937' , 'driver_number' : '7295164017' },
{ 'cab_id' : 'cab_17' , 'driver_name' : 'ARVIND KUMAR' , 'cab_no' : 'KA 18 CW 4729' , 'driver_number' : '9948203641' },
{ 'cab_id' : 'cab_18' , 'driver_name' : 'CHETHAN SINGH' , 'cab_no' : 'KA 48 SH 391' , 'driver_number' : '8292075919' },
{ 'cab_id' : 'cab_19' , 'driver_name' : 'RAJEEV' , 'cab_no' : 'KA 58 DU 8492' , 'driver_number' : '9175910484' },
{ 'cab_id' : 'cab_20' , 'driver_name' : 'PANKAJ' , 'cab_no' : 'KA 08 D 8391' , 'driver_number' : '8293918492' },
{ 'cab_id' : 'cab_21' , 'driver_name' : 'DINESH SINGH' , 'cab_no' : 'KA 26 HA 3838' , 'driver_number' : '7290455184' },
{ 'cab_id' : 'cab_22' , 'driver_name' : 'SYED RIZVI' , 'cab_no' : 'KA 16 DU 2846' , 'driver_number' : '7200464819' },
{ 'cab_id' : 'cab_23' , 'driver_name' : 'SANJAY' , 'cab_no' : 'KA 01 MT 4829' , 'driver_number' : '9957294185' },
{ 'cab_id' : 'cab_24' , 'driver_name' : 'AMIT VERMA' , 'cab_no' : 'KA 46 HE 483' , 'driver_number' : '6185900174' },
{ 'cab_id' : 'cab_25' , 'driver_name' : 'SUSHANT SINGH' , 'cab_no' : 'KA 18 DU 2758' , 'driver_number' : '9938316939' },
{ 'cab-id' : 'cab_26' , 'driver_name' : 'RAJEEV' , 'cab_no' : 'KA 48 SJ 3729' , 'driver_number' : '8838366184' },
{ 'cab_id' : 'cab_27' , 'driver_name' : 'YUSUF KHAN' , 'cab_no' : 'KA 10 HD 0278' , 'driver_number' : '9937255111' },
{ 'cab_id' : 'cab_28' , 'driver_name' : 'ANTHONY JOSEFH' , 'cab_no' : 'KA 21 WJ 5920' , 'driver_number' : '8393066183' },
{ 'cab_id' : 'cab_29' , 'driver_name' : 'AYAN MUKHERJEE' , 'cab_no' : 'KA 38 RI 2859' , 'driver_number' : '8492472949' },
{ 'cab_id' : 'cab_30' , 'driver_name' : 'ROHIT GOWDA' , 'cab_no' : 'KA 48 DO 2402' , 'driver_number' : '9937364991' },
{ 'cab_id' : 'cab_31' , 'driver_name' : 'CHANDAN SHETTY' , 'cab_no' : 'KA 19 OS 5820' , 'driver_number' : '8284001839' },
{ 'cab_id' : 'cab_32' , 'driver_name' : 'MONISH V' , 'cab_no' : 'KA 39 SI 3829' , 'driver_number' : '8293520057' },
{ 'cab_id' : 'cab_33' , 'driver_name' : 'DILBAGH SINGH' , 'cab_no' : 'KA 42 J 2250' , 'driver_number' : '7202663821' },
{ 'cab_id' : 'cab_34' , 'driver_name' : 'SYED AKBAR' , 'cab_no' : 'KA 11 M 7247' , 'driver_number' : '9937174828' }];
cab_info_detail.insert(data)



