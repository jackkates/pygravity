from math import log

class Body(object):

	def __init__(self, p, m, v):
		self.position = p
		self.mass = m
		self.veloc = v
		self.size = log(self.mass)

	def force(self, f):
		self.accel(f / self.mass)

	def accel(self, a):
		self.veloc += a

	def update(self, dt):


