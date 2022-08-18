import re

a = "in KLU at KLU from KLu"
b = re.findall("KL", a)
c = re.search("at",a)
d = re.split("KLu",a)
e = re.sub("in","Thanmai",a)
print(a)
print(b)
print(c)
print(d)
print(e)