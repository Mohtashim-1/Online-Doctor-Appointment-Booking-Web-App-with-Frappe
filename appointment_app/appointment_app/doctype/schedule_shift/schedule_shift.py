# Copyright (c) 2024, Mohtashim and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class ScheduleShift(Document):
	def before_save(self):
		# set the title field to start time and end time 
		self.title = "abcd"
		# self.title = self.start_time + "-" + self.end_time
