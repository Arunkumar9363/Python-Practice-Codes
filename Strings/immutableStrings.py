'''1. Once we declared the String we cannot modify it,
 if we try to modify the String it will create new String.

2.If new String does not have any reference variable then it will be removed.

3.Python Internally users String Internally.

4.String Internaly is the Process of Checking String Intern Pool befor creating any new object.

Whenever we want to create new object, Python first will check String
intern pool, weather that object already exist or not.

When Object already exist in the String intern Records then address of existing object will be reused.
'''

# s1 = 'Kodnest'
# s1 = s1.upper()
# print(s1)

# s1 = 'K'
# print(s1, id(s1))

s1 = 'Hello'
s2 = 'World'
print(s1, id(s1))
print(s2, id(s2))

print('s1 ID of H:', id(s1[0]))
print('s1 ID of O:', id(s1[-1]))

print('s2 Id of W:', id(s2[0]))
print('s2 ID of O:', id(s2[1]))

print('s1 ID of l:', id(s1[2]))
print('s1 ID of l:', id(s1[3]))
print('s2 ID of l:', id(s2[3]))