import copy

name = ['#!jackchen', '4jasonpan',['alex', 'wayne'], 'Johnsonlu', 'susancheng']

name2 = copy.deepcopy(name)
#name2 = copy.copy(name)

print(name)
print(name2)
name[3] = "陳柏勳"
name[2][0] = "gaod"
print("------")
print(name)
print(name2)
