from kvsqlite.sync import Client as C
from config import database_name
#انشاء
#dev = [1160471152,435009958]
db = C(f"{database_name}.sqlite")
db.autocommit = True

#members = []
#db.delete("users")
#for i in open("mem.txt","r").readlines():
#	members.append(int(i.replace("\n","")))
#	db.set("users",members)
#	print(len(members))
#print(len(db.get("users")))
#print(members)
