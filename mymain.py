from timeJson import dataStore
ds=dataStore()
while 1:
	print("Press 1 to add item")
	print("Press 2 to get an item")
	print("Press 3 to delete a key")
	print("press 4 to close window")
	a=int(input())
	if a==1:
		print("type key")
		key=input()
		print("if you want to add list as value press 1")
		print("if you want to add dictionary as value press 2")
		print("if you want to add integer,string or float as value press 3")
		b=int(input())
		if b==1:
			print("enter the sapce separated list inputs")
			val=input().split()
			ds.additem(key,val)
		if b==2:
			print("enter the sapce separated key inputs")
			k=input().split()
			print("enter the sapce separated value inputs")
			v=input().split()
			val={}
			for i in range(len(k)):
				val[k[i]]=v[i]
			ds.additem(key,val)
		if b==3:
			print("enter value")
			k=input()
			ds.additem(key,val)
	if a==2:
		print("type key")
		key=input()
		ds.getitem(key)
	if a==3:
		print("type key")
		key=input()
		ds.deleteitem(key)
	if a==4:
		break
			

