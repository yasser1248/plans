import frappe
from frappe import _
from frappe.utils import getdate , date_diff
from erpnext.selling.doctype.quotation.quotation import Quotation
class customsQuotation(Quotation) :
    
    # def validate(self):
    #     frappe.throw(_("this is throwed message for testing"))
    
    def before_save(self):
        date = self.transaction_date
        valid_till = self.valid_till
        diff = date_diff(valid_till, date)
        if diff < 0:
            frappe.throw(_("valid till should be greater than transaction_date"))
            self.custom_duration = None
        elif diff == 0:
            frappe.msgprint(_("This Quotation is valid Till Today"))
            self.custom_duration = None
        else:
            self.custom_duration = diff
        
        
    
        