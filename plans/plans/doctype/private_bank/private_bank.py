# Copyright (c) 2024, jamil and contributors
# For license information, please see license.txt

# from apps.car.car.car.doctype import bank_name
import frappe
from frappe.model.document import Document
import time

@frappe.whitelist()
def get_bank_name(bank_name):
		time.sleep(3)
		# frappe.msgprint( f"hello from {bank_name} " ) 
		return "RETURNED {0}".format(bank_name)



class PrivateBank(Document):
	# def change_bank_number(self):
	# 	ls=frappe.db.get_list("Bank Name", pluck ="bank_number")
	# 	frappe.msgprint(ls)
	# def validate(self):
	# 	self.change_bank_number()
	pass
#----------test the vedio--------



# @frappe.whitelist()
# def get_bank_name():
# 		time.sleep(3)
# 		# frappe.msgprint( f"hello from {bank_name} " ) 
# 		return "RETURNED"