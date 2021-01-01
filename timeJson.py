from threading import Thread
from threading import Lock
import time
import json
import os
import sys

class dataStore:
	def __init__(self,ttl=5):
		self.__ttl=ttl
		self.__dic={}
		self.__timemap={}
		self.lock=Lock()
		self._t=Thread(target=self._expires)
		self._t.start()
	def _expires(self):
		while len(self.__dic):
			now=tme.time()
			keys=self.__timemap.keys()
			for i in key:
				val=self.__timemap[i]
				diff=now-val
				if diff>self.__ttl:
					del self.__dic[key]
					del self.__timemap[key]
	def __settime(self,key):
		self.__timemap[key]=time.time()
	def additem(self,key,value):
		value=json.dumps(value)
		print(sys.getsizeof(value))
		if sys.getsizeof(value)>64:
			print("Size of value is greater than 64KB")
			return
		if type(key)!=str:
			print("Key is not a string")
			return 
		if len(key)>32:
			print("The characters of the key is greater than 32")
			return
		if key in self.__dic:
			print("key already exist")
			return
		self.lock.acquire()
		self.__dic[key]=value
		self.__settime(key)
		self.lock.release()
	def getitem(self,key):
		if key in self.__dic:
			print("the value at key",key,"is",self.__dic[key])
		else:
			print("key does not exist")
	def deleteitem(self,key):
		if key in self.__dic:
			self.lock.acquire()
			del self.__dic[key]
			del self.__timemap[key]
			self.lock.release()
			print("item deleted")
		else:
			print("key does not exist")
		
		
			
		
