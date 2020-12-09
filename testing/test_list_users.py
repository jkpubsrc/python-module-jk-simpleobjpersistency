#!/usr/bin/env python3




import jk_simpleobjpersistency

from MyUserObj import MyUserObj



ppdm = jk_simpleobjpersistency.PersistencyManager("testdata")
ppdm.registerClass(MyUserObj, {
	"eMail": "example@example.com"
}, "testdata/users")



for i, identifier in enumerate(ppdm.allIdentifiers(MyUserObj)):
	print(identifier)
	obj = ppdm.getObject(MyUserObj, identifier)
	print("\tisModified(): " + str(obj.isModified()))
	if i == 0:
		print("\tsetModified()")
		obj.setModified()
		print("\tisModified(): " + str(obj.isModified()))







