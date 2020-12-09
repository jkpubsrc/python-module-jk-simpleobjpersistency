#!/usr/bin/env python3




import jk_simpleobjpersistency

from MyUserObj import MyUserObj



ppdm = jk_simpleobjpersistency.PersistencyManager("testdata")
ppdm.registerClass(MyUserObj, {
	"eMail": "example@example.com"
}, dirPath="testdata/users", autoStore=True)



obj = ppdm.getObject(MyUserObj, "id3")
obj.comment = "Lorem ipsum"
obj.setModified()

del obj

ppdm.clearEntireCache()

obj = ppdm.getObject(MyUserObj, "id3")
assert obj.comment == "Lorem ipsum"









