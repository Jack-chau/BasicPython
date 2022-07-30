import json
data = {}
data['name'] = 'paul'
data['age'] = 18

jsonText = json.dumps(data)
print(jsonText)

obj = json.loads(jsonText)
print(obj)