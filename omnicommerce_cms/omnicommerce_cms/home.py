import frappe
import os
import frappe
from datetime import datetime, timedelta
from urllib.parse import urlparse
from mymb_ecommerce.repository.MytptparReposiotory import MytptparRepository
from frappe.utils import now

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
def update_home_b2b_hook(doc=None, method=None):
    cache_key = "home_b2b_data"
    
    data = get_home()
    frappe.cache().set_value(cache_key, data)
    frappe.log_error( title="update_home_b2b_hook", message=f"Time: {now()}")
    return data


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

    popular_departments = frappe.get_list('Popular Departments', order_by=order_by , fields=['*'])
    data_home_popular_department = [map_home_popular_department_to_doctype(popular_department) for popular_department in popular_departments]

    flyers = frappe.get_list('Flyer', order_by=order_by , fields=['*'])
    data_flyer = [map_flyer_to_doctype(flyer) for flyer in flyers]
    
    # Create a dictionary containing the slider_top data
    data = {
        'slider_top': data_slider,
        'promo_banner':data_promo,
        'home_category':data_home_category,
        'home_brand':data_home_brand,
        'popular_department':data_home_popular_department,
        'flyer': data_flyer

        }
    
    return data


def map_flyer_to_doctype(flyer):
    doctype = {
        'order': flyer.get('order'),
        'label': flyer.get('label'),
        'url': flyer.get('pdf'),
        'flyer_image': flyer.get('flyer_image'),
        'b2b': flyer.get('b2b', False),
        'b2c': flyer.get('b2c', False),
        'status': flyer.get('status', 'Published')
    }
    return doctype


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
        'text_color': slider.get('text_color'),
        'status': slider.get('status'),
        'background_transparency': slider.get('background_transparency'),
        'slide_image': [{'url': f'{web_site_domain}{image_name}'}] if image_name else None,
        'slide_image_mobile': [{'url': f'{web_site_domain}{image_name_mobile}'}] if image_name_mobile else None,
        'b2b': slider.get('b2b', False),
        'b2c': slider.get('b2c', False),
    }
    return doctype

def map_promo_banner_to_doctype(promo_banner):
    image_name = promo_banner['image_banner']
    web_site_domain = get_website_domain()

    
    doctype = {
        'order': promo_banner['order'],
        'label': promo_banner['label'],
        'url': promo_banner['url'],
        'slide_image':  f'{web_site_domain}{image_name}',
        'background_color_banner': promo_banner.get('background_color_banner'),
        'text_color': promo_banner.get('text_color'),
        'background_transparency': promo_banner.get('background_transparency'),
        'b2b': promo_banner.get('b2b', False),
        'b2c': promo_banner.get('b2c', False),
        'status': promo_banner.get('status'),
    }
    return doctype

def map_home_category_to_doctype(home_category):
    image_name = home_category['image']
    web_site_domain = get_website_domain()

    
    doctype = {
        'order': home_category['order'],
        'label': home_category['label'],
        'url': home_category['url'],
        'image':  f'{web_site_domain}{image_name}',
        'b2b': home_category.get('b2b', False),
        'b2c': home_category.get('b2c', False),
        'status': home_category.get('status'),
    }
    return doctype

def map_home_brand_to_doctype(home_brand):
    image_name = home_brand['image']
    web_site_domain = get_website_domain()

    
    doctype = {
        'order': home_brand['order'],
        'label': home_brand['label'],
        'url': home_brand['url'],
        'image':  f'{web_site_domain}{image_name}',
        'b2b': home_brand.get('b2b', False),
        'b2c': home_brand.get('b2c', False),
        'status': home_brand.get('status'),
    }
    return doctype

def map_home_popular_department_to_doctype(popular_department):
    image_name = popular_department['image']
    web_site_domain = get_website_domain()

    
    doctype = {
        'order': popular_department['order'],
        'label': popular_department['label'],
        'url': popular_department['url'],
        'image':  f'{web_site_domain}{image_name}',
        'b2b': popular_department.get('b2b', False),
        'b2c': popular_department.get('b2c', False),
        'status': popular_department.get('status'),
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
    # item['url'] += '&tab_name='  + item_name if item['url'] else '' //hide the tab_category name issue
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
        'category_banner_image_mobile': f'{web_site_domain}{item["category_banner_image_mobile"]}' if item.get("category_banner_image_mobile") else None,
        'disable': item.get('disable', False),

    }
    return doctype



@frappe.whitelist(allow_guest=True, methods=['GET'])
def get_b2b_menu(args=None):

    # Construct a unique cache key for B2B menu
    cache_key = "b2b_menu_items"
    # Try to get cached data
    cached_b2b_menu = frappe.cache().get_value(cache_key)
    if cached_b2b_menu:
        return cached_b2b_menu

    data_menu = update_b2b_menu_hook()
    # Fetch records from the B2B Menu table

    return data_menu

@frappe.whitelist(allow_guest=True, methods=['GET'])
def update_b2b_menu_hook(doc=None, method=None):
    
    # Construct a unique cache key for B2B menu
    cache_key = "b2b_menu_items"

    order_by = '`order` asc'
    b2b_menu_items = frappe.get_list('B2B Menu', order_by=order_by, fields=['*'])
    data_menu = [map_b2b_menu(item, 'b2b') for item in b2b_menu_items]
    b2b_dynamic_nodes = b2b_menu_items = frappe.get_list( 'B2B Menu',  filters={'is_dynamic_node': True},  order_by=order_by, fields=['*'])
    for b2b_dynamic_node in b2b_dynamic_nodes:
        ctipo_dtpar = b2b_dynamic_node.get('search_key','None')
        my_tparty = MytptparRepository()
        node_lists = my_tparty.get_id_subtype(to_dict=True  , ctipo_dtpar=ctipo_dtpar)
        dynamic_nodes = [map_b2b_dynamic_node(item, 'b2b', parent_node=b2b_dynamic_node) for item in node_lists]
        data_menu.extend(dynamic_nodes)  # Append new items instead of reassigning

    frappe.cache().set_value(cache_key, data_menu)
    frappe.log_error( title="update_b2b_menu_hook", message=f"Time: {now()}")
    return data_menu

def is_absolute_url(url):
    """Check if the URL is absolute."""
    return bool(urlparse(url).netloc)


def map_b2b_menu(item , menu_type):

    web_site_domain = get_website_domain()
    item_url = item.get('url', '')
    item_name = item.get('name', '')

    item['url']= item_url
    # Only modify item['url'] if it's not an absolute URL
    if item_url and not is_absolute_url(item_url):
        if item_url:
            item['url'] = f"{item_url}&category_detail={item_name}"
        if item_name:
            item['url'] += f"&tab_name={item_name}"

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
        'category_banner_image_mobile': f'{web_site_domain}{item["category_banner_image_mobile"]}' if item.get("category_banner_image_mobile") else None,
        'disable': item.get('disable', False),

    }
    return doctype
    



def map_b2b_dynamic_node(item , menu_type , parent_node):
 
    id_type = item.get('ctipo_dtpar', '')
    id_subtype =  item.get('ctipo_darti', '')
    item_name = item.get('ttipo_darti', '') 
    url = f'shop?id_type={id_type}&id_subtype={id_subtype}&tab_name={item_name}'

    doctype = {
        'name': id_subtype,
        'label': item_name,
        'order': 1,
        'title': item_name,
        'url': url,
        'description': item_name,
        'is_group': False,
        'old_parent': parent_node['name'],
        'parent_menu': parent_node['name'],
        'category_menu_image': None,
        'category_banner_image':  None,
        'category_banner_image_mobile':  None,
        'disable': False,

    }
    return doctype

@frappe.whitelist(allow_guest=True, methods=['GET'])
def get_promo_slider(args=None):
    # Define the order_by variable if needed, for example:
    order_by = '`order` asc'

    # Use frappe.get_list to fetch records from the database
    promo_slider_items= frappe.get_list('Promo Slider', order_by=order_by , fields=['*'])
    data = [map_promo_slider(item ) for item in promo_slider_items]
    
    # Create a dictionary containing the data_menu data    
    return data

@frappe.whitelist(allow_guest=True, methods=['GET'])
def update_hook_promo_slider(doc=None, method=None):
    cache_key = "b2b_promo_slider"

    promo_slider_items = frappe.get_list('Promo Slider', order_by='`order` asc', fields=['*'])
    data = [map_promo_slider(item) for item in promo_slider_items]

    frappe.cache().set_value(cache_key, data)
    frappe.log_error( title="update_hook_promo_slider", message=f"Time: {now()}")

    return data



def map_promo_slider(item ):
    item['url'] = item['url'] +  '&tab_name='  + item['text'] if item['text'] else  item['url'] 
    doctype = {
        'icon': item['icon'],
        'url': item['url'],
        'text': item['text'],
        'b2b': item.get('b2b', False),
        'b2c': item.get('b2c', False)
    }
    return doctype