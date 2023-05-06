
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

    promos_banner = frappe.get_list('Promo Banner', order_by=order_by , fields=['*'])
    data_promo = [map_promo_banner_to_doctype(promo_banner) for promo_banner in promos_banner]

    home_categories = frappe.get_list('Home Category', order_by=order_by , fields=['*'])
    data_home_category = [map_home_category_to_doctype(home_category) for home_category in home_categories]

    home_brands = frappe.get_list('Home Brand', order_by=order_by , fields=['*'])
    data_home_brand = [map_home_brand_to_doctype(home_brand) for home_brand in home_brands]
    
    # Create a dictionary containing the slider_top data
    data = {
        'slider_top': data_slider,
        'promo_banner':data_promo,
        'home_category':data_home_category,
        'home_brand':data_home_brand
        }
    
    return data


def map_slider_to_doctype(slider):
    image_name = slider['image']

    
    doctype = {
        'order': slider['order'],
        'position': slider['position'],
        'title_1': slider['text'],
        'title_2': slider['second_text'],
        'button': slider['button'],
        'url':slider['url'],
        'background_color_banner': slider['background_color_banner'],
        'text_color': slider['background_color_banner'],
        'status': 'Published',
        'background_transparency': slider['background_transparency'],
        'slide_image': [{'url': f'{web_site_domain}{image_name}'}]
    }
    return doctype

def map_promo_banner_to_doctype(promo_banner):
    image_name = promo_banner['image_banner']

    
    doctype = {
        'order': promo_banner['order'],
        'label': promo_banner['label'],
        'url': promo_banner['url'],
        'slide_image':  f'{web_site_domain}{image_name}'
    }
    return doctype

def map_home_category_to_doctype(home_category):
    image_name = home_category['image']

    
    doctype = {
        'order': home_category['order'],
        'label': home_category['label'],
        'url': home_category['url'],
        'image':  f'{web_site_domain}{image_name}'
    }
    return doctype

def map_home_brand_to_doctype(home_brand):
    image_name = home_brand['image']

    
    doctype = {
        'order': home_brand['order'],
        'label': home_brand['label'],
        'url': home_brand['url'],
        'image':  f'{web_site_domain}{image_name}'
    }
    return doctype





