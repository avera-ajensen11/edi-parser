from edi_parser.elements.identifier import Identifier
from edi_parser.segments.utilities import split_segment


class IndivOrgName:
	identification = 'NM1'

	identifier = Identifier()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.entityIDCode = segment[1]
		self.entityTypeQual = segment[2]
		self.nameLastOrOrg = segment[3]
		self.nameFirst = segment[4]
		self.nameMiddle = segment[5]
		self.namePrefix = segment[6]
		self.nameSuffix = segment[7]
		self.idCodeQual = segment[8]
		self.idCode = segment[9]

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
