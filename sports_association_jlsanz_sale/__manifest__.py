# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association",
    "summary": "Manage sports summary",
    "version": "17.0.1.0.0",
    "category": "Sports",
    "author": "<AUTHOR(S)>",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "sports_association_jlsanz",
        "sale_management",
    ],
    "data": [
        "views/sport_ticket_views.xml",
        "views/sale_order_views.xml",
        "views/product_views.xml",
        ]
}