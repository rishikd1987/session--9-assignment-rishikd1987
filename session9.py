from collections import namedtuple
from datetime import datetime,date
from time import perf_counter
from collections import Counter
import random
import string
import math

"""
	fghfghfgh)
"""

class Polygon:
	def __init__(self,edge:int,circumradius:int):
		self.edge = edge
		self.circumradius = circumradius

	def __repr__(self):
		return f"Polygon with {self.edge} edges and circumradius={self.circumradius}"

	def no_of_edges(self):
		return self.edge

	def no_of_vertices(self):
		return self.edge

	def interior_angle(self):
		return ((self.edge-2)*180/self.edge)

	def edge_length(self):
		return (2 * self.circumradius * math.sin(math.pi/self.edge))

	def apothem(self):
		return (self.circumradius * math.cos(math.pi/self.edge))

	def area(self):
		return (0.5 * self.edge * self.interior_angle() * self.apothem())

	def perimeter(self):
		return (self.edge * self.edge_length())

	def __eq__(self, other):
		if not isinstance(other, Polygon):
			raise TypeError(f"{other} is not of type Polygon")
		if self.edge == other.edge and self.circumradius == other.circumradius:
			return True
		else:
			return False

	def __gt__(self, other):
		if not isinstance(other, Polygon):
			raise TypeError(f"{other} is not of type Polygon")
		if self.edge > other.edge:
			return True
		else:
			return False

class Polygon_sequence:
	def __init__(self,largest_edge,common_circumradius):
		self.largest_edge = largest_edge
		self.common_circumradius = common_circumradius
		self.polygon_seq = [Polygon(x,self.common_circumradius) for x in range(1,self.largest_edge+1)]

	def __repr__(self):
		return str(self.polygon_seq)

	def max_efficiency(self):
		eff_list = [(x.area()/x.perimeter()) for x in self.polygon_seq]
		return self.polygon_seq[eff_list.index(max(eff_list))]

	def __len__(self):
		return len(self.polygon_seq)

	def __getitem__(self, item):
		return self.polygon_seq[item]







if __name__ == "__main__":
	x = Polygon_sequence(6,10)
	print(x)
	print(x.max_efficiency())
	print(x[2].perimeter())











