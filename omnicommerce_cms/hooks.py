from . import __version__ as app_version

app_name = "omnicommerce_cms"
app_title = "Omnicommerce Cms"
app_publisher = "Crowdechain s.r.o"
app_description = "Cms to handle template section"
app_email = "developers@crowdechain.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/omnicommerce_cms/css/omnicommerce_cms.css"
# app_include_js = "/assets/omnicommerce_cms/js/omnicommerce_cms.js"

# include js, css files in header of web template
# web_include_css = "/assets/omnicommerce_cms/css/omnicommerce_cms.css"
# web_include_js = "/assets/omnicommerce_cms/js/omnicommerce_cms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "omnicommerce_cms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "omnicommerce_cms.utils.jinja_methods",
#	"filters": "omnicommerce_cms.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "omnicommerce_cms.install.before_install"
# after_install = "omnicommerce_cms.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "omnicommerce_cms.uninstall.before_uninstall"
# after_uninstall = "omnicommerce_cms.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "omnicommerce_cms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

doc_events = {
    "B2B Menu": {
        "on_update": "omnicommerce_cms.omnicommerce_cms.home.update_b2b_menu_hook"    
        }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"omnicommerce_cms.tasks.all"
#	],
#	"daily": [
#		"omnicommerce_cms.tasks.daily"
#	],
#	"hourly": [
#		"omnicommerce_cms.tasks.hourly"
#	],
#	"weekly": [
#		"omnicommerce_cms.tasks.weekly"
#	],
#	"monthly": [
#		"omnicommerce_cms.tasks.monthly"
#	],
# }

scheduler_events = {
	# "all": ["mymb_ecommerce.mymb_b2c.inventory.update_inventory_on_shopify"],
	"weekly": [],
	"monthly": [],
	"cron": {
		# Every 3 hours
		"30 5 * * *": [
			"omnicommerce_cms.omnicommerce_cms.home.update_b2b_menu_hook",
		# 	# "mymb_ecommerce.unicommerce.inventory.update_inventory_on_unicommerce",
		],
	},
}

# Testing
# -------

# before_tests = "omnicommerce_cms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "omnicommerce_cms.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "omnicommerce_cms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["omnicommerce_cms.utils.before_request"]
# after_request = ["omnicommerce_cms.utils.after_request"]

# Job Events
# ----------
# before_job = ["omnicommerce_cms.utils.before_job"]
# after_job = ["omnicommerce_cms.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"omnicommerce_cms.auth.validate"
# ]
