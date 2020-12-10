class Person:
	def __init__(self, f_name, l_name):
		self.f_name = f_name
		self.l_name = l_name
	def display_name(self):
		print(self.f_name, self.l_name)
	

if __name__=="__main__":
	person1 = Person('Andrew', 'Smith')
	person1.display_name()
