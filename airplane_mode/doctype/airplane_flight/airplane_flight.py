# Copyright (c) 2023, Bhushan Sapkal and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
	def after_save(doc):
		doc.duration=frappe.utils.format_duration(doc.duration)
		doc.date=frappe.utils.format_date(doc.date_of_departure, "d MMMM, YYYY")