class Employee:
	def __init__(self, first, last):
		self.first = first
		self.last = last

	@property
	def email(self):
		return f'{self.first}{self.last}@email.com'

	@property
	def fullname(self):
		return f'{self.first} {self.last}'

	@property.setter
	def fullname(self, name):
		first, last = name.split(" ")
		self.first = first
		self.last = last

	@property.deleter
	def fullname(self):
		self.first = None
		self.last = None

emp_1 = Employee('Jhonn', 'Smith')

print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = "Corey Schafer"


del emp_1.fullname