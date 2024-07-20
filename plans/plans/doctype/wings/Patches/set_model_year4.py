import frappe

def execute():
    # frappe.reload_doc("plans", "doctype", "wings")
    wings = frappe.get_all("Wings", fields=["name","wing_name", "model_year"])
    for wing in wings:
        if not wing.model_year:
            if wing.wing_name == "hof-65484":
                wing.model_year = "2022"
            elif wing.wing_name == "sdakfn-3443":
                wing.model_year = "2023"
            elif wing.wing_name == "sdakfn-34433":
                wing.model_year = "2024"
                
            frappe.db.set_value("Wings", wing.name, "model_year", wing.model_year, update_modified=False)
        else:
            frappe.msgprint(" i in else")
