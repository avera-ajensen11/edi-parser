from collections import namedtuple

import pandas as pd

from edi_parser.loops.HL_HierarchicalLevel import (
    HeirarchialLevel as HeirarchialLevelLoop,
)
from edi_parser.segments.utilities import find_identifier, split_segment
from edi_parser.transaction_set.transaction_set import TransactionSet

BuildAttributeResponse = namedtuple('BuildAttributeResponse', 'key value segment segments')


class TxSet_271(TransactionSet):

	def __init__(self, filePath):
		super().__init__(filePath)
		segment = self.segments.__next__()
		while True:
			try:
				fields = split_segment(segment)
				identifier = find_identifier(segment)
				if identifier == "HL":
					heirarchialLevelLoop, segments, segment = HeirarchialLevelLoop.build(segment, self.segments)
					levelCode = heirarchialLevelLoop.heirarchialLevel.levelCode
					if levelCode == '20': # Information Source (Payer)
						self.payerLoop = heirarchialLevelLoop
					elif levelCode == '21': # Information Receiver (Provider)
						self.providerLoop = heirarchialLevelLoop
					elif levelCode == '22': # Subscriber
						self.subscriberLoop = heirarchialLevelLoop
					elif levelCode == '23': # Dependent
						self.dependentLoop = heirarchialLevelLoop
				else:
					segment = self.segments.__next__()
			except StopIteration:
				return

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())

	"""
	def to_dataframe(self) -> pd.DataFrame:
		data = []
		for claim in self.claims:
			for service in claim.services:

				datum = TransactionSet.serialize_service(
					self.financial_information,
					self.payer,
					claim,
					service
				)

				for index, adjustment in enumerate(service.adjustments):
					datum[f'adj_{index}_group'] = adjustment.group_code.code
					datum[f'adj_{index}_code'] = adjustment.reason_code.code
					datum[f'adj_{index}_amount'] = adjustment.amount

				for index, reference in enumerate(service.references):
					datum[f'ref_{index}_qual'] = reference.qualifier.code
					datum[f'ref_{index}_value'] = reference.value

				for index, remark in enumerate(service.remarks):
					datum[f'rem_{index}_qual'] = remark.qualifier.code
					datum[f'rem_{index}_code'] = remark.code.code

				data.append(datum)

		return pd.DataFrame(data)
	"""