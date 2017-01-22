import os
import re

class ContactFinder(object):
	
	def __init__(self):
		self.CONTACT_NUMBER = re.compile(r'''
					    ^  # start of line
					    (?:
					      (?:\+|0{0,2})91(\s*[\ -]\s*)?  # country code
					      |[0]?  # or leading zero
					    )?
					    [789]\d{9}  # ten digits starting 7, 8 or 9
					    |(\d[ -]?){10}\d  # or eleven digits with a separator
					    $  # end of line
					''', re.VERBOSE)

	def traverse(self,dir_path):
		for root, dirs, files in os.walk(dir_path):
			self.open_file(root, files)

	def open_file(self, root_path, files):
		for file in files:
			filename = os.path.join(root_path, file)
			with open(filename) as fn:
				self.print_contact(fn)

	def print_contact(self, filename):
		for contact in filename:
			if self.CONTACT_NUMBER.match(contact):
				print contact.rstrip()		

contact = ContactFinder()
contact.traverse('path/to/directory')
