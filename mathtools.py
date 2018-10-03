import math

class vector(object):
	def __init__(self, vector):
		self.vector = vector

	def __repr__(self):
		return repr(self.vector)

	def __add__(a, b):
		return [sum(a.vector) for a.vector in zip(a.vector, b.vector)]

	def __sub__(a, b):
		return [a.vector - b.vector for (a.vector, b.vector) in zip(a.vector, b.vector)]
	
	def __mul__(a, b):
		mul = [b, b, b]
		return [a.vector * mul for (a.vector, mul) in zip(a.vector, mul)]

	# DOESN'T WORK YET
	def __div__(a, b):
		div = [b, b, b]
		return [a.vector / div for (a.vector, div) in zip(a.vector, div)]

"""
		for i in a.vector:
			divide = a.vector[i] / b
			div.append(divide)
		#a.vector = div
		return div
"""

vector1 = vector([4,3,8])
vector2 = vector([2,0,1])

print('result of vector operation:', vector1 * 2)


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
	
	def veclen(x):
		vecsum = 0
		for i in x:
			vecsum += math.pow(i, 2)
		magnitude = math.sqrt(vecsum)
		return magnitude
	
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
