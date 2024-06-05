# Copyright (c) 2024, jamil and contributors
# For license information, please see license.txt

from re import S
import frappe
from frappe.model.document import Document
from frappe import _
# from frappe.utils import add_to_date , getdate
# import frappe.utils
# today=getdate()

class CIBLoan(Document):
    def on_trash(self):
        doc = frappe.get_doc("CIB Loan", "CIB-LN-00038")
        doc.branch_name ="Aleppo D2C"
        frappe.msgprint("i am in  {0}".format(doc.branch_name))
        doc.save()
        frappe.msgprint("i am in  {0}".format(doc.branch_name))
    # def validate(self):
    #     frappe.msgprint("hello i am in validate {0}".format(self.loan_amount))

                    
    def on_submit(self):
        journal_entry = frappe.new_doc("Journal Entry")
        journal_entry.voucher_type = "Journal Entry"
        journal_entry.posting_date = self.posting_date
        
        #frist row
        Accounts_row = journal_entry.append("accounts", {})
        Accounts_row.account = self.loan_account
        Accounts_row.credit_in_account_currency = self.loan_amount
        Accounts_row.credit = self.loan_amount
        #second row
        Accounts_row = journal_entry.append("accounts", {})
        Accounts_row.account = self.disbursement_account
        Accounts_row.debit_in_account_currency = self.loan_amount
        Accounts_row.debit = self.loan_amount
        #reference field
        journal_entry.cib_loan = self.name
        
        
        journal_entry.insert()
		# journal_entry.submit()
        
        
    def on_update(self):
        self.loan_schedule = []
        if self.repayment_months ==0:
            frappe.throw(_("Please Enter Repayment Months"))
        if self.loan_amount ==0:
            frappe.throw(_("Please Enter Loan Amount"))
        if self.repayment_date < self.posting_date:
            frappe.throw(_("Repayment Date cannot be less than Posting Date"))
        
        for i in range(int(self.repayment_months)):
			# repament is a raw variable


            repayment = self.append("loan_schedule", {})
            repayment.payment_date = frappe.utils.add_to_date(self.repayment_date, months=i)
            repayment.principal_amount = self.loan_amount / self.repayment_months
            repayment.interest_amount = repayment.principal_amount * float(self.interest) /100
            repayment.total_payment = repayment.principal_amount + repayment.interest_amount
            repayment.balance_loan_amount = (self.loan_amount + self.loan_amount * float(self.interest) /100) - (repayment.total_payment * (i+1))

    def update_status(self,status_counter): 
            frappe.msgprint( "hello i am in update status")
            status_counter == 0
            self.loan_schedule
            for row in self.loan_schedule:
                if row.payment_date < self.posting_date :
                    status_counter += 1
                elif row.payment_date > self.posting_date  :
                    status_counter += 0
                else:
                    status_counter += 0
            if status_counter == len(self.loan_schedule):
                frappe.db.set_value("CIB Loan", self.name, "status", "Paid")
            elif status_counter == 0:
                frappe.db.set_value("CIB Loan", self.name, "status", "Unpaid")
            else:
                frappe.db.set_value("CIB Loan", self.name, "status", "Partially Paid")
            
            frappe.msgprint( "status counter is",status_counter)
            frappe.msgprint( "len is",len(self.loan_schedule))
    #     #----------------------25/5/2024--------------------------------------------
    # def validate(self):
    #     # status =self.status
    #     # frappe.msgprint(f"hello i am in validate,and the status is " +  status )
    #     # frappe.msgprint(f"hello i am in validate,and the status is " +  self.status )
    #     frappe.msgprint("hello i am in validate,and the status is {0}").format("jamil")
def check_loan ():
    today=getdate()
    loans = frappe.db.get_list("CIB Loan", fields=["name"], filters=[["status", "in", ["Unpaid","Partially Paid"]]])
    for record in loans:
        loan = frappe.get_doc("CIB Loan", record.name) 
        for row in loan.loan_schedule:
            if row.payment_date < loan.posting_date:
                frappe.throw(_("Payment date cannot be less than Posting Date"))
            if row.payment_date == today and row.journal_entry == None and loan.docstatus == 1:
                journal_entry = frappe.new_doc("Journal Entry")
                journal_entry.voucher_type = "Journal Entry"
                journal_entry.posting_date = row.payment_date
        
                #frist row
                Accounts_row = journal_entry.append("accounts", {})
                Accounts_row.account = record.loan_account
                Accounts_row.credit_in_account_currency = row.total_payment
                Accounts_row.credit = row.total_payment
                #second row
                Accounts_row = journal_entry.append("accounts", {})
                Accounts_row.account = record.repayment_account
                Accounts_row.debit_in_account_currency = row.total_payment
                Accounts_row.debit = row.total_payment
                journal_entry.insert()
                row.journal_entry = journal_entry.name
                loan.save()
        