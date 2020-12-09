#!/usr/bin/env python3




import jk_simpleobjpersistency

from MyUserObj import MyUserObj



ppdm = jk_simpleobjpersistency.PersistencyManager("testdata")
ppdm.registerClass(MyUserObj, {
	"eMail": "example@example.com"
}, "testdata/users")



ppdm.destroyAllObjects(MyUserObj)



obj = ppdm.createObject(MyUserObj, "myUser")
print(obj._x_identifier)
assert obj._x_identifier == "myUser"
print(obj.isPersistent())
assert obj.isPersistent() == False
obj.store()
print(obj.isPersistent())
assert obj.isPersistent() == True
print()

obj = ppdm.createObject(MyUserObj)
print(obj._x_identifier)
assert obj._x_identifier == "id1"
print(obj.isPersistent())
assert obj.isPersistent() == False
obj.store()
print(obj.isPersistent())
assert obj.isPersistent() == True
print()

obj = ppdm.createObject(MyUserObj)
objID2 = obj
print(obj._x_identifier)
assert obj._x_identifier == "id2"
print(obj.isPersistent())
assert obj.isPersistent() == False
obj.store()
print(obj.isPersistent())
assert obj.isPersistent() == True
print()

obj = ppdm.createObject(MyUserObj)
print(obj._x_identifier)
assert obj._x_identifier == "id3"
print(obj.isPersistent())
assert obj.isPersistent() == False
obj.store()
print(obj.isPersistent())
assert obj.isPersistent() == True
print()

objID2.destroy()




