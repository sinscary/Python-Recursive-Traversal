import os
import re

class ContactFinder:
	
	def __init__(self):
		self.pattern = re.compile('^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$')

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
			if self.pattern.match(contact):
				print contact		

contact = ContactFinder()
contact.traverse('/home/sinscary/Documents/angular')
