import importlib
import os
import re
import sys
from typing import Any, List, Optional, Tuple, Type


def split_segment(segment: str) -> List[str]:
	"""different payers use different characters to delineate elements"""
	asterisk = '*'
	pipe = '|'

	asterisk_segment_count = len(segment.split(asterisk))
	pipe_segment_count = len(segment.split(pipe))

	if asterisk_segment_count > pipe_segment_count:
		return segment.split(asterisk)
	else:
		return segment.split(pipe)


def find_identifier(segment) -> str:
	segment = split_segment(segment)
	return segment[0]

def get_element(segment: List[str], index: int, default=None) -> Optional[str]:
	element = default
	if index < len(segment):
		element = segment[index]

	return element

def find_classes_by_substring(folder_path: str, substring: str) -> List[Tuple[str, Type[Any]]]:
	# List to store the tuples of (package path, class object) that contain the substring
	class_info: List[Tuple[str, Type[Any]]] = []

	# Regex pattern to match class definitions
	pattern = re.compile(r'class\s+([A-Za-z_][A-Za-z_0-9]*)\s*\(?.*?\)?:')

	# Normalize the folder path to ensure consistency
	folder_path = os.path.normpath(folder_path)

	# Adjust sys.path to include the root directory
	if folder_path not in sys.path:
		sys.path.insert(0, folder_path)

	# Iterate through all files in the specified folder
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			if file.endswith(".py"):
				file_path = os.path.join(root, file)
				# Calculating the package path by removing the root folder path
				# and replacing file system separators with dots
				package_path = os.path.relpath(file_path, folder_path)
				package_path = os.path.splitext(package_path)[0]
				package_path = package_path.replace(os.sep, '.')
				with open(file_path, 'r', encoding='utf-8') as f:
					content = f.read()
				# Search for class definitions in the file content
				for match in pattern.finditer(content):
					class_name = match.group(1)
					if substring in class_name:
						# Dynamically import the module and get a reference to the class
						module = importlib.import_module(package_path)
						class_ = getattr(module, class_name)
						class_info.append((package_path, class_))

	return class_info
