from typing import Iterator, Optional, Tuple

from edi_parser.segments.HL_HierarchicalLevel import (
    HierarchialLevel as HierarchialLevelSegment,
)

from edi_parser.segments.utilities import find_identifier
from edi_parser.segments.NM1_IndivOrgName import IndivOrgName
from edi_parser.segments.EB_BenefitInformation import BenefitInformation as BenefitInformationSegment


class BenefitInformation:
	initiating_identifier = BenefitInformationSegment.identification
	terminating_identifiers = [
		BenefitInformationSegment.identification,
		'SE'
	]

	def __init__(self, benefitInformation = None):
		self.benefitInformation: BenefitInformationSegment = benefitInformation


	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())

	@classmethod
	def build(cls, current_segment: str, segments: Iterator[str]) -> Tuple[
		'BenefitInformation', Optional[Iterator[str]], Optional[str]
	]:
		benefitInformation = BenefitInformation()
		benefitInformation.benefitInformation = BenefitInformationSegment(current_segment)
		while True:
			try:
				segment = segments.__next__()
				identifier = find_identifier(segment)
                #TODO Add Segment Code
				
			except StopIteration:
				return benefitInformation, None, None
