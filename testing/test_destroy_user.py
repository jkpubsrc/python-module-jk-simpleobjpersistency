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
obj.store()
print()

obj.destroy()

obj = ppdm.getObject(MyUserObj, "myUser")
assert obj is None

obj = ppdm.createObject(MyUserObj, "myUser")
obj.destroy()

obj = ppdm.getObject(MyUserObj, "myUser")
assert obj is None

