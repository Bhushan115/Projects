# Copyright (c) 2023, Bhushan Sapkal and contributors
# For license information, please see license.txt

import frappe

from frappe.model.document import Document

class Airline(Document):
    pass


	# def add_custom_web_link(doc):
	# 	if doc.website:
	# 		web_link = f'<a class="btn-open-website" href="{doc.website}" target="_blank">Open Official Website</a>'
	# 		frappe.msgprint(web_link)

	# # Attach the function to the Airline DocType
	# frappe.get_doc('Airline').add_custom_function('validate', 'add_custom_web_link')

	