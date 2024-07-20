import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.model.utils import get_fetch_values
from frappe.utils import getdate
from frappe import _

# def permission_query_conditions(user):
#     if user == "Administrator":
#         frappe.msgprint("i am in  {0} ,so i can read only this".format(user))
#         return "color != 100"