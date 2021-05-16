
class GeoPoint:
	def __init__(self, lat, lon):
		self.__lat=lat
		self.__lon=lon

	def getLat(self):
		return self.__lat

	def getLon(self):
		return self.__lon

pos1=GeoPoint(40.85,14.28)
print(pos1.getLat(), pos1.getLon())

