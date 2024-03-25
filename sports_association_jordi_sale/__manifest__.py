# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association Tickets",
    "summary": "Manager sports Tickets",
    "version": "17.0.1.0.0",
    "category": "Sports",
    "author": "<Jordi Navarro>, I2T",
    "maintainers": ["JordiNavarro"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "sports_association_jordi","sale_management"
    ],
   "data":[
        "views/sports_ticket_views.xml",
        "views/sale_order_views.xml",
        "views/product_template_views.xml"
         ]
}