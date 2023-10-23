from edi_parser.elements.identifier import Identifier
from edi_parser.segments.utilities import split_segment


class HierarchialLevel:
	identification = 'HL'

	identifier = Identifier()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.heirarchialID = segment[1]
		self.parentID = segment[2]
		self.levelCode = segment[3]
		self.childCode = segment[4]

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
