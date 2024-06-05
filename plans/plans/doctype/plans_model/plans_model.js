// Copyright (c) 2024, jamil and contributors
// For license information, please see license.txt

frappe.ui.form.on("Plans Model", {
	refresh(frm) {
    },
    repayment_months :function (frm) {
        if (frm.doc.loan_amount && frm.doc.repayment_months) {
            var monthly = (frm.doc.loan_amount / frm.doc.repayment_months);
            var monthly = monthly + (monthly * frm.doc.interest /100);
            frm.doc.monthly_repayment = monthly;
            frm.set_value("monthly_repayment", monthly);
            refresh_field("monthly_repayment");
            
    }},
    loan_amount :function (frm) {
        if (frm.doc.loan_amount && frm.doc.repayment_months) {
            var monthly = (frm.doc.loan_amount / frm.doc.repayment_months);
            var monthly = monthly + (monthly * frm.doc.interest /100);
            frm.doc.monthly_repayment = monthly;
            frm.set_value("monthly_repayment", monthly);
            refresh_field("monthly_repayment");
    }},
    interest :function (frm) {
        if (frm.doc.loan_amount && frm.doc.repayment_months) {
            var monthly = (frm.doc.loan_amount / frm.doc.repayment_months);
            var monthly = monthly + (monthly * frm.doc.interest /100);
            frm.doc.monthly_repayment = monthly;
            frm.set_value("monthly_repayment", monthly);
            refresh_field("monthly_repayment");
    }}
});
