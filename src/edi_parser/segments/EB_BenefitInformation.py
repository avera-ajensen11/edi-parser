from edi_parser.elements.identifier import Identifier
from edi_parser.segments.utilities import split_segment


class BenefitInformation:
	identification = 'EB'

	identifier = Identifier()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)
		try:
			self.identifier = segment[0]
			self.BenefitInfoCode = segment[1]
			self.CoverageLevelCode = segment[2]
			self.ServiceTypeCode = segment[3]
			self.InsuranceTypeCode = segment[4]
			self.PlanCoverageDesc = segment[5]
			self.TimePeriodQualifier = segment[6]
			self.MonetaryAmount = segment[7]
			self.PercentageAsDecimal = segment[8]
			self.QuantityQualifier = segment[9]
			self.Quantity = segment[10]
			self.AuthResponseCode = segment[11]
			self.InNetworkResponseCode= segment[12]
			self.ProcedureIdentifier = segment[13]
			self.CompositeDXCodePointer = segment[14]
		except:
			
			return


	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
