// Copyright (c) 2024, jamil and contributors
// For license information, please see license.txt

frappe.ui.form.on("CIB Loan", {
  refresh(frm) {},
  repayment_months: function (frm) {
    calculate(frm);
  },
  loan_amount: function (frm) {
    calculate(frm);
  },
  interest: function (frm) {
    calculate(frm);
  },
});
function calculate(frm) {
  if (frm.doc.loan_amount && frm.doc.repayment_months) {
    var monthly = frm.doc.loan_amount / frm.doc.repayment_months;
    var monthly = monthly + (monthly * frm.doc.interest) / 100;
    frm.doc.monthly_repayment = monthly;
    frm.set_value("monthly_repayment", monthly);
    refresh_field("monthly_repayment");
  }
}
frappe.ui.form.on("loan_schedule", {
  loan_schedule_add(frm,cdt,cdn) {
    frappe.msgprint(" New row added");
  },
  before_fieldnameloan_schedule_remove(frm,cdt,cdn) {
    frappe.msgprint(" row before remove");
  },
  loan_schedule_remove(frm,cdt,cdn) {
    frappe.msgprint(" New row removED");
  },
  
  loan_schedule_move(frm,cdt,cdn) {
    frappe.msgprint(" New row moved");
  },
  form_render(frm,cdt,cdn) {
    frappe.msgprint(" form render");
  },

})
//-------------------------25/5/2024-----------------------
frappe.ui.form.on ("CIB Loan", {
  // refresh: function(frm) {
  //   frm.set_intro("Fill the form and save it, it will create a new CIB Loan", frm.is_new());
  //   frappe.msgprint (__("CIB Loan saved successfully {0} {1} {2}",[frm.doc.loan_amount,frm.doc.monthly_repayment,frm.doc.interest])  );
  // }
// ,before_submit: function(frm) {
//     frappe.msgprint("CIB Loan saved successfully");
//     frappe.set_intro(__("you on two few steps to create a CIB Loan"));  
// //   }
// loan_amount: function(frm) {
//     frm.set_value("branch_name", frm.doc.loan_amount+" "+frm.doc.monthly_repayment+" "+frm.doc.interest);
  // }
refresh: function(frm) {
    frm.add_custom_button(__("CIB Loan1"), function () {
    frappe.msgprint("clicked me!");
  },"primary");
    frm.add_custom_button(__("CIB Loan2"), function () {
    frappe.msgprint("clicked me!");
  },"primary");
    frm.add_custom_button(__("CIB Loan3"), function () {
    frappe.msgprint("clicked me!");
  },"primary");}

})