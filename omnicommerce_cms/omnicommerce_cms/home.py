
import frappe



import frappe

web_site_domain = frappe.utils.get_url()

@frappe.whitelist(allow_guest=True, methods=['GET'])
def get_home(args=None):
    # Define the order_by variable if needed, for example:
    order_by = 'creation desc'
    
    # Use frappe.get_list to fetch records from the database
    sliders_top = frappe.get_list('Home Slider', order_by=order_by , fields=['*'])
    data_slider = [map_slider_to_doctype(slider) for slider in sliders_top]
    
    # Create a dictionary containing the slider_top data
    data = {'slider_top': data_slider}
    
    return data


def map_slider_to_doctype(slider):
    image_name = slider['image']

    
    doctype = {
        'order': slider['order'],
        'position': slider['position'],
        'title_1': slider['text'],
        'title_2': slider['second_text'],
        'titolo_3': slider['button'],
        'url':slider['url'],
        'background_color_banner': slider['background_color_banner'],
        'text_color': slider['background_color_banner'],
        'status': 'Published',
        'background_transparency': slider['background_transparency'],
        'slide_image': [{'url': f'{web_site_domain}/{image_name}'}]
    }
    return doctype

def map_slider_to_doctype(slider):
    image_name = slider['image']

    
    doctype = {
        'order': slider['order'],
        'position': slider['position'],
        'title_1': slider['text'],
        'title_2': slider['second_text'],
        'titolo_3': slider['button'],
        'url':slider['url'],
        'background_color_banner': slider['background_color_banner'],
        'text_color': slider['background_color_banner'],
        'status': 'Published',
        'background_transparency': slider['background_transparency'],
        'slide_image': [{'url': f'{web_site_domain}/{image_name}'}]
    }
    return doctype




