from typing import Iterator, Optional, Tuple

from edi_parser.segments.HL_HierarchicalLevel import (
    HierarchialLevel as HierarchialLevelSegment,
)

from edi_parser.segments.utilities import find_identifier
from edi_parser.segments.NM1_IndivOrgName import IndivOrgName
from edi_parser.segments.EB_BenefitInformation import BenefitInformation as BenefitInformationSegment
from edi_parser.loops.EB_BenefitInformation import BenefitInformation as BenefitInformationLoop


class HeirarchialLevel:
	initiating_identifier = HierarchialLevelSegment.identification
	terminating_identifiers = [
		HierarchialLevelSegment.identification,
		'SE'
	]

	def __init__(self, heirarchialLevel = None, indivOrgName = None, benefitInfomation = []):
		self.heirarchialLevel: HierarchialLevelSegment  = heirarchialLevel
		self.indivOrgName: IndivOrgName = indivOrgName
		self.benefitInformation: list[BenefitInformationLoop] = benefitInfomation

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
				elif identifier == BenefitInformationSegment.identification:
					heirarchialLevel.benefitInformation.append(BenefitInformationLoop.build(segment, segments))

				elif identifier in cls.terminating_identifiers:
					return heirarchialLevel, segments, segment

			except StopIteration:
				return heirarchialLevel, None, None
