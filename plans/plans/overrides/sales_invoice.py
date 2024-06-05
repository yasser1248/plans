# # Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# # License: GNU General Public License v3. See license.txt


# from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
# import frappe
# from frappe import _, msgprint, throw
# from frappe.contacts.doctype.address.address import get_address_display
# from frappe.model.mapper import get_mapped_doc
# from frappe.model.utils import get_fetch_values
# from frappe.utils import add_days, cint, cstr, flt, formatdate, get_link_to_form, getdate, nowdate

# import erpnext
# from erpnext.accounts.deferred_revenue import validate_service_stop_date
# from erpnext.accounts.doctype.loyalty_program.loyalty_program import (
# 	get_loyalty_program_details_with_points,
# 	validate_loyalty_points,
# )
# from erpnext.accounts.doctype.repost_accounting_ledger.repost_accounting_ledger import (
# 	validate_docs_for_deferred_accounting,
# 	validate_docs_for_voucher_types,
# )
# from erpnext.accounts.doctype.tax_withholding_category.tax_withholding_category import (
# 	get_party_tax_withholding_details,
# )
# from erpnext.accounts.general_ledger import get_round_off_account_and_cost_center
# from erpnext.accounts.party import get_due_date, get_party_account, get_party_details
# from erpnext.accounts.utils import cancel_exchange_gain_loss_journal, get_account_currency
# from erpnext.assets.doctype.asset.depreciation import (
# 	depreciate_asset,
# 	get_disposal_account_and_cost_center,
# 	get_gl_entries_on_asset_disposal,
# 	get_gl_entries_on_asset_regain,
# 	reset_depreciation_schedule,
# 	reverse_depreciation_entry_made_after_disposal,
# )
# from erpnext.assets.doctype.asset_activity.asset_activity import add_asset_activity
# from erpnext.controllers.accounts_controller import validate_account_head
# from erpnext.controllers.selling_controller import SellingController
# from erpnext.projects.doctype.timesheet.timesheet import get_projectwise_timesheet_data
# from erpnext.setup.doctype.company.company import update_company_current_month_sales
# from erpnext.stock.doctype.delivery_note.delivery_note import update_billed_amount_based_on_so
# from erpnext.stock.doctype.serial_no.serial_no import get_delivery_note_serial_no, get_serial_nos

# class JamilSalesInvoice(SalesInvoice):
#     def validate(self):
#         super().validate()
#     def jamil (self):
#         frappe.msgprint("hello from jamil def")
#     def before_save(self):
#         super().before_save()
#         self.jamil()