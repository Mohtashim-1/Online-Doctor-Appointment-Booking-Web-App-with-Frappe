# Copyright (c) 2024, Mohtashim and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import format_time


class ScheduleShift(Document):
	frappe.msgprint('Message')
	def before_save(self):
		frappe.msgprint('Message')
		# set the title field to "start_time-end_time"
		self.title = format_time(self.start_time, "HH:mm") + "-" + format_time(self.end_time, "HH:mm")
	
   			
			
		
