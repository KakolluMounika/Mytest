# Write a python program to implement code for dailer app search without consider spaces
a = {"8639522181":"mouni","9010197801":"dad","9948795543":"mom"}


class DailerClass:
	def __init__(self,search_ele):
		self.search_ele = search_ele
		self.dailer_fun()
	def dailer_fun(self):
		for i in a:
			try:
				phone_number = int(self.search_ele)
			except ValueError:
				phone_number= -1
			if(phone_number==-1 and self.search_ele in a[i]):
				print i,a[i]
			else:
				if(search_ele in i):
					print i,a[i]
				else:
					print "Sorry, record not found"

if __name__=="__main__":
	search_ele = raw_input("Enter search element: ")
	dailer = DailerClass(search_ele)
