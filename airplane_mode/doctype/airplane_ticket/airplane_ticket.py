# Copyright (c) 2023, Bhushan Sapkal and contributors
# For license information, please see license.txt

import frappe
import random
import string
import frappe.utils 
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator

class AirplaneTicket(WebsiteGenerator):
	def before_save(self):
		# self.addon()
		self.document()
		self.generate_seat()
		


	def document(self):
		price=self.flight_price
		doc=0
		for row in self.add_ons:
			doc=doc+row.amount
		self.total_amount=price+doc

	
	def validate(doc):
		add_on_types = set()
		for add_on in doc.add_ons:
			if add_on.item in add_on_types:
				frappe.throw(("Add-on '{0}' is duplicated.").format(add_on.item))
			add_on_types.add(add_on.item)	


	def generate_seat(self):

		if not self.seat:
			random_integer = random.randint(1, 100)  
			random_letter = random.choice(string.ascii_uppercase[:5])  
			self.seat = f"{random_integer}{random_letter}"

	def validate(self):
		self.validate_capacity()
	def validate_capacity(doc):
		# Get the airplane associated with the ticket
		airplane = frappe.get_value("Airplane", doc.airplane, "capacity")

		# Count existing tickets for this flight
		existing_tickets = frappe.get_all("Airplane Ticket", filters={"flight": doc.flight})

		if len(existing_tickets) >= airplane:
			frappe.throw(("The flight is fully booked. No more tickets can be created."))
		

	# def addon(self):
	# 	doc=frappe.get.doc('Airplane Ticket Add-on Item','add_ons')
	# 	# for doc in self.ad_ons:
	# 	self.item=doc.item
	# 	self.amount=doc.amount


	# def totalamount(self):
	# 	total = self.flight_price
	# 	for add_on in self.add_ons:
	# 		total += add_on.amount
	# 	self.total_amount = total





	# def set_status_to_completed(doc, method):
	# 	if method == 'on_submit' and doc.status != 'Completed':
	# 		doc.status = 'Completed'
	# 		doc.save()

	# # Hook this method to the Airplane Flight DocType
	# frappe.get_doc('Airplane Flight').on_submit = set_status_to_completed           

	# def connect(self):
	# 	doc=frappe.db.get_value('Airplane Ticket Add-on Item',doc,self.amount)
	# 	doc_as_integer = frappe.utils.cint(doc)
	# 	self.total_amount=self.flight_price + doc_as_integer
