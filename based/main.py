import based

s = '''abc = 123
d = 5
f = 0
ab = 60'''

print(based.parse(s))

d = {"hi": 123, "bag": "oh"}

print(based.stringfy(d))