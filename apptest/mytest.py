
class Test(object):

	def view_func(self):
		return 'hello'

	def __call__(self,*args,**kwargs):
		def wrapper(func):
			return self.view_func(**kwargs)
		return wrapper