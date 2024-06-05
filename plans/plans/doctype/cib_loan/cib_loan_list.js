frappe.listview_settings["CIB Loan"] = {
    get_indicator(doc){
        if(doc.status == "Paid"){
            return [__("Paid"), "blue", "status,=,Paid"];
    } else {
            return [__("Unpaid"), "light-blue", "status,=,Unpaid"];}}    
}