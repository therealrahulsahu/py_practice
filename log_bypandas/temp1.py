import validation as V
import pymongo

data = []
for x in range(V.posinteger('Enter count :')):
    temp = dict()
    temp['email'] = V.validEmail('Enter Email :')
    temp['phone'] = V.validPhone('Enter Phone :')
    temp['name'] = V.validName('Enter Name :')
    data.append(temp)
print(*data, sep="\n")
# mycol = pymongo.MongoClient('mongodb://localhost:27017/')['formdetails1']["std1"]
myclient = pymongo.MongoClient('mongodb+srv://therealrahulsahu:rahulsahu1_@democluster-2u6fb.gcp.mongodb.net/test?retryWrites=true')
mycol = myclient['formdetails1']["std1"]
mycol.insert_many(data)
