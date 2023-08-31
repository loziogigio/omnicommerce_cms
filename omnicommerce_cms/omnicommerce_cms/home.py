import frappe
import os



def get_website_domain():

    # check if omnicommere cdn is installed
    if 'omnicommere_cdn' not in frappe.get_installed_apps():
        return ""
    
    site_name = frappe.local.site
    sites_folder = frappe.get_app_path('frappe', '..', '..', 'sites')

    site_config_path = os.path.join(sites_folder, site_name, 'site_config.json')
    if os.path.exists(site_config_path):
        with open(site_config_path, 'r') as site_config_file:
            site_config = frappe._dict(frappe.parse_json(site_config_file.read()))

        if site_config.host_name:
            website_domain = f"https://{site_config.host_name}"
        else:
            website_domain = frappe.utils.get_url()
    else:
        website_domain = frappe.utils.get_url()

    return website_domain

@frappe.whitelist(allow_guest=True, methods=['GET'])
def get_home(args=None):
    # Define the order_by variable if needed, for example:
    order_by = '`order` asc'

    
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
    image_name = slider.get('image')
    image_name_mobile = slider.get('image_mobile')
    web_site_domain = get_website_domain()

    doctype = {
        'order': slider.get('order'),
        'position': slider.get('position'),
        'title_1': slider.get('text'),
        'title_2': slider.get('second_text'),
        'button': slider.get('button'),
        'url': slider.get('url'),
        'background_color_banner': slider.get('background_color_banner'),
        'text_color': slider.get('background_color_banner'),
        'status': 'Published',
        'background_transparency': slider.get('background_transparency'),
        'slide_image': [{'url': f'{web_site_domain}{image_name}'}] if image_name else None,
        'slide_image_mobile': [{'url': f'{web_site_domain}{image_name_mobile}'}] if image_name_mobile else None
    }
    return doctype

def map_promo_banner_to_doctype(promo_banner):
    image_name = promo_banner['image_banner']
    web_site_domain = get_website_domain()

    
    doctype = {
        'order': promo_banner['order'],
        'label': promo_banner['label'],
        'url': promo_banner['url'],
        'slide_image':  f'{web_site_domain}{image_name}'
    }
    return doctype

def map_home_category_to_doctype(home_category):
    image_name = home_category['image']
    web_site_domain = get_website_domain()

    
    doctype = {
        'order': home_category['order'],
        'label': home_category['label'],
        'url': home_category['url'],
        'image':  f'{web_site_domain}{image_name}'
    }
    return doctype

def map_home_brand_to_doctype(home_brand):
    image_name = home_brand['image']
    web_site_domain = get_website_domain()

    
    doctype = {
        'order': home_brand['order'],
        'label': home_brand['label'],
        'url': home_brand['url'],
        'image':  f'{web_site_domain}{image_name}'
    }
    return doctype

@frappe.whitelist(allow_guest=True, methods=['GET'])
def get_b2c_menu(args=None):
    # Define the order_by variable if needed, for example:
    order_by = '`order` asc'

    # Use frappe.get_list to fetch records from the database
    b2c_menu_items = frappe.get_list('B2C Menu', order_by=order_by , fields=['*'])
    data_menu = [map_menu(item , 'b2c') for item in b2c_menu_items]
    
    # Create a dictionary containing the data_menu data    
    return data_menu

def map_menu(item , menu_type):
    web_site_domain = get_website_domain()
    item_url = item.get('url', '')
    item_name = item.get('name', '')
    item['url'] = item_url + '&category_detail=' + item_name if item_url else item_url
    item['url'] += '&tab_name='  + item_name if item['url'] else ''
    doctype = {
        'name': item['name'],
        'creation': item['creation'],
        'docstatus': item['docstatus'],
        'label': item['label'],
        'order': item['order'],
        'title': item['title'],
        'url': item['url'],
        'description': item['description'],
        'lft': item['lft'],
        'rgt': item['rgt'],
        'is_group': item['is_group'],
        'old_parent': item['old_parent'],
        'parent_menu': item[f'parent_{menu_type}_menu'],
        'category_menu_image': f'{web_site_domain}{item["category_menu_image"]}' if item.get("category_menu_image") else None,
        'category_banner_image': f'{web_site_domain}{item["category_banner_image"]}' if item.get("category_banner_image") else None,
        'category_banner_image_mobile': f'{web_site_domain}{item["category_banner_image_mobile"]}' if item.get("category_banner_image_mobile") else None

    }
    return doctype



@frappe.whitelist(allow_guest=True, methods=['GET'])
def get_b2b_menu(args=None):
    # Define the order_by variable if needed, for example:
    order_by = '`order` asc'

    # Use frappe.get_list to fetch records from the database
    b2b_menu_items = frappe.get_list('B2B Menu', order_by=order_by , fields=['*'])
    data_menu = [map_menu(item , 'b2b') for item in b2b_menu_items]
    
    # Create a dictionary containing the data_menu data    
    return data_menu


@frappe.whitelist(allow_guest=True, methods=['GET'])
def get_promo_slider(args=None):
    # Define the order_by variable if needed, for example:
    order_by = '`order` asc'

    # Use frappe.get_list to fetch records from the database
    promo_slider_items= frappe.get_list('Promo Slider', order_by=order_by , fields=['*'])
    data = [map_promo_slider(item ) for item in promo_slider_items]
    
    # Create a dictionary containing the data_menu data    
    return data


def map_promo_slider(item ):
    item['url'] = item['url'] +  '&tab_name='  + item['text'] if item['text'] else  item['url'] 
    doctype = {
        'icon': item['icon'],
        'url': item['url'],
        'text': item['text']
    }
    return doctype