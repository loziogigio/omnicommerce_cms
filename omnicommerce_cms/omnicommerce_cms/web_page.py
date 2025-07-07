import frappe

    
@frappe.whitelist(allow_guest=True, methods=['GET'])
def get_web_page_detail(route=None):
    try:
        # Check if the route is provided
        if route is None:
            return {"error": "Route is a mandatory field."}

        # Get the web page  using the provided route
        web_page = frappe.get_all("Web Page", fields=["*"], filters={"route": route}, limit=1)

        # Check if a web page  was found
        if not web_page:
            return {"error": "No Web Page found for the given route."}

        result = {
            "data": web_page[0],  # Return the first (and only) matching web page 
        }

        return result

    except Exception as e:
        frappe.log_error(message=f"An unexpected error occurred: {str(e)}", title="Unexpected Error in get_web_page_detail")
        return {
            "error": f"An unexpected error occurred. {str(e)}"
        }
    


import json
from frappe.utils import cstr, now

@frappe.whitelist(allow_guest=True, methods=["GET"])
def update_hook_b2b_main_web_page(doc=None, method=None):
    cache_key = "b2b_web_page_detail:main"
    web_page = frappe.get_all("Web Page", fields=["*"], filters={"route": "main"}, limit=1)

    if web_page:
        data = dict(web_page[0])

        # Converti datetime in stringa se necessario
        for key in ["creation", "modified", "start_date", "end_date"]:
            if data.get(key):
                data[key] = cstr(data[key])

        frappe.cache().set_value(cache_key, data)
        frappe.log_error( title="update_hook_b2b_main_web_page:main", message=f"Time update: {now()}")
        return {"data": data}
    else:
        frappe.cache().delete_value(cache_key)
        frappe.log_error( title="update_hook_b2b_main_web_page:main", message=f"Time delete: {now()}")
        return {"error": "No Web Page found with route 'main'"}
