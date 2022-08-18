import json
x = '''{ "name":"John", "age":30, "city":"New York"}''' #single codes are possible also
y = json.loads(x)
z=json.dumps(x)
print(z)
print(y["age"])
