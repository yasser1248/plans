// Copyright (c) 2024, jamil and contributors
// For license information, please see license.txt

frappe.ui.form.on("Private Bank", {
	// enabled: function(frm) {
    //     frm.call({
    //         doc : frm.doc,
    //         method : "get_bank_name",
    //         args: {
    //             bank_name : frm.doc.bank_name
    //         },
    //         freeze : true,
    //         freeze_message : __("Fetching Bank Name"),
    //         callback : function(r) {
    //             // frappe.msgprint(__("Status : {0}").format(r.message));
    //             frappr.msgprint(r.message);

    //         }

    //     })

	// },
    enabled: function(frm) {
        frappe.call({
            method : "plans.plans.doctype.private_bank.private_bank.get_bank_name",
            // method : "get_bank_name",
            args: {
                bank_name : "FRappe Bank"
            },
            freeze : true,
            freeze_message : __("Fetching Bank Name"),
            callback : function(r) {
                // frappe.msgprint(__("Status : {0}").format(r.message));
                frappe.msgprint(r.message);

            }

        })

	},
});
