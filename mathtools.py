import math

class vector(object):
	def __init__(self, data):
		self.data = data
	
	def __repr__(self):
		return self.__class__.__name__+'('+repr(self.data)+')'
	
	def __add__(self, other):
		return self.__class__([a + b for a, b in zip(self.data, other.data)])
	
	def __sub__(self, other):
		return self.__class__([a - b for a, b in zip(self.data, other.data)])
	
	def __mul__(self, other):
		a = []
		for i in range(len(self.data)):
			a.append(self.data[i] * other)
		return self.__class__(a)

	def __truediv__(self, other):
		a = []
		for i in range(len(self.data)):
			a.append(self.data[i] / other)
		return self.__class__(a)

class veclen(object):
	def __init__(self, data):
		self.data = data
		self.vecmagnitude()

	def __float__(self):
		return self.data
	
	def __repr__(self):
		return repr(self.data)
	
	def vecmagnitude(self):
		vecsum = 0
		for i in self.data.data:
			vecsum += math.pow(i, 2)
			magnitude = math.sqrt(vecsum)
		self.data = float(magnitude)
		return self.data


"""
	def vecnormalize(x):
		vecsum = 0
		unitvec = []
		for i in x:
			vecsum += math.pow(i, 2)
		veclen = math.sqrt(vecsum)
		for i in x:
			unitvec.append(i / veclen)
		return unitvec
	
	
	def pointdistance(x, y):
		return math.sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))
	
	def dotproduct(x, y):
		return sum((a * b) for a, b in zip(x, y))
	
	# get angle between two vectors
	def vecangle(x, y): # this is unfished fix it
		zerovector = []
		for i in range(len(x)):
			zerovector.append(0)
		# put both vectors at origo
		xorigo = vecadd(vecsub(zerovector, x), x)
		yorigo = vecadd(vecsub(zerovector, y), y)
		dotxy = dotproduct(x, y)
		dotlen = veclen(x) * veclen(y)
		return math.acos(dotxy / dotlen)
	
	def barycentric(x, y, z, a, b, c):
		inside = a + b + c
		return vecdiv(vecadd(vecadd(vecmul(x, a), vecmul(y, b)), vecmul(z, c)), inside)
	
	# loop through list
	def feature_rescaling(x):
		xmin = x[0]
		xmax = x[0]
		newvec = []
		for i in x: # get xmin
			if i < xmin:
				xmin = i
			if i > xmax: # get xmax
				xmax = i
		for g in x:
			r = (g - xmin) / (xmax - xmin)
			#print('feature rescaling:', r)
			newvec.append(r)
		return newvec
	
	def vecmean(x): # mean of vectors not components
		zerovec = []
		meanvec = []
		for i in x[0]:
			zerovec.append(0)
		for i in x:
			zerovec = vecadd(i, zerovec)
		for i in zerovec:
			mean = i / len(x)
			meanvec.append(mean)
		return meanvec
	
	# linear interpolation
	def lerp(x, y, s): # vec1, vec2, scalar
		return vecadd(x, vecmul(vecsub(y, x), s))

def spherical_to_cartesian(r, theta, phi): # altitude, longitude, latitude
	x = r * math.sin(theta) * math.cos(phi)
	y = r * math.sin(theta) * math.sin(phi)
	z = r * math.cos(theta)
	return sphere_x, sphere_y, sphere_z

def cartesian_to_spherical(x, y, z): # z is up
	r = math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))
	theta = math.acos(z / r)
	phi = math.atan(y / x)
	return r, theta, phi

def parabola(x, h, k):
	return a * math.pow(x - h, 2) + k

def cubicpolynomial(x, a, b, c):
	return math.pow(x, 3) + (a * math.pow(x, 2)) + (b * x) + c
"""
