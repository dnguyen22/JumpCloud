class Action(object):

	def __init__(self, name, duration):
		self.name = name
		self.accumulator = duration
		self.count = 1

	def add(self, duration):
		self.accumulator += duration
		self.count += 1

	def get_average(self):
		return self.accumulator / self.count
