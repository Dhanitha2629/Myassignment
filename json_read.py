f=open("D://assignmentdata.txt","r")
result = f.read()
import json
user= json.loads(result)

print(user)
