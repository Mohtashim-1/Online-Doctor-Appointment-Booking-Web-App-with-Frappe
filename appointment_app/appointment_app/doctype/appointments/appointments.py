# Copyright (c) 2024, Mohtashim and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Appointments(Document):
	def after_insert(self):
		self.add_to_appointment_queue()

		def add_to_appointment_queue(self):
			frappe.get_doc('Appointment Queue',{
				'date':self.date,
				'shift':self.shift,
				'clinic':self.clinic,
			})
