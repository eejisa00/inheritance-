#creating a class
class Person:
	def __init__(self,name,age,city):
		self.name = name
		self.age = age
#creating a child class
class Worker(Person):
	def __init__(self,name,age,city,worker_id):
		super().__init__(name,age,city)
		self.worker_id=worker_id

class Server(Worker):
	def __init__(self,name,age,city,worker_id,dob):
		super().__init__(name,age,city,worker_id)
		self.dob=dob
		
#hierarichal inheritance
class Manager(Person):
	def __init__(self,name,age,city,workers=[]):
		super().__init__(name,age,city)
		self.workers=workers
	def show_workers(self):
		for worker in self.workers:
			print(worker.name)

p1=Server("Andruce","67","chennai","12345","1999")
p2=Server("Joyce","45","chennai","54321","1998")
m= Manager("Charan","38","chennai",[p1,p2])
print(m.name)
m.show_workers()
		