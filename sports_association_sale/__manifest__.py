# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "sports association sales",
    "summary": "Module for sports ticket sales",
    "version": "17.0.1.0.0",
    "category": "Uncategorized",
    "website": "https://github.com/potxolate",
    "author": "potxolate",
    # see https://odoo-community.org/page/maintainer-role for a description of the maintainer role and responsibilities
    "maintainers": ["potxolate"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "preloadable": True,
    "depends": [
        "web",
        "sale",
        "sports_association",
    ],
    "data": [
        "views/sale_order_views.xml",
        "views/sport_ticket_views.xml",
    ],
}
