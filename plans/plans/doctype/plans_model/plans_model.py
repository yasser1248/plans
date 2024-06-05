# Copyright (c) 2024, jamil and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import getdate , date_diff
from frappe.model.document import Document



class PlansModel(Document):
	def validate(self):
		brand = self.brand
		if len(brand) != 5:
			frappe.throw(_("Brand Must be in 5 letters"))
	
def update_days_untill_now():
    order = frappe.db.get_list("Plans Model", fields = ["name","date", "days_until_now"])
    now = getdate()
    for o in order :
        diff=date_diff(now, o.date)
        frappe.msgprint("inside")
        frappe.db.set_value("Plans Model", o.name, "days_until_now", diff, update_modified=False)
    frappe.db.commit()
    
frappe.msgprint("from out")
print("from out")