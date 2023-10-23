from typing import Iterator, Optional, Tuple

from edi_parser.segments.HL_HierarchicalLevel import (
    HierarchialLevel as HierarchialLevelSegment,
)
from edi_parser.segments.NM1_IndivOrgName import IndivOrgName
from edi_parser.segments.utilities import find_identifier


class HeirarchialLevel:
	initiating_identifier = HierarchialLevelSegment.identification
	terminating_identifiers = [
		HierarchialLevelSegment.identification,
		'SE'
	]

	def __init__(self, heirarchialLevel = None, indivOrgName = None):
		self.heirarchialLevel: HierarchialLevelSegment  = heirarchialLevel
		self.indivOrgName: IndivOrgName = indivOrgName

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())

	@classmethod
	def build(cls, current_segment: str, segments: Iterator[str]) -> Tuple[
		'HeirarchialLevel', Optional[Iterator[str]], Optional[str]
	]:
		heirarchialLevel = HeirarchialLevel()
		heirarchialLevel.heirarchialLevel = HierarchialLevelSegment(current_segment)
		while True:
			try:
				segment = segments.__next__()
				identifier = find_identifier(segment)

				if identifier == IndivOrgName.identification:
					heirarchialLevel.indivOrgName = IndivOrgName(segment)

				elif identifier in cls.terminating_identifiers:
					return heirarchialLevel, segments, segment

			except StopIteration:
				return heirarchialLevel, None, None
