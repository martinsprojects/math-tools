import mathtools as mt

vec1 = mt.Vector([0,0,1])
vec2 = mt.Vector([1,0,1])
vec3 = vec2.unit
vec4 = vec1.unit
print(vec3.dot(vec4))
#print(vec1.dot(vec2))