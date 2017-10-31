from xmlrpc.client import ServerProxy

s = ServerProxy('http://localhost:10000')

a = 5
b = 6

print(s.add(a, b))

a = [1, 2, 3]
b = [4, 5, 6, 7]

print(s.add(a, b))
print(s.system.listMethods())
print(s.system.methodHelp('add'))
