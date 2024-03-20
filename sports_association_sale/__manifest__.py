# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association Sale Tickets",
    "summary": "Manage Sports Associations Tickets",
    "version": "17.0.1.0.0",
    "category": "Sports",
    "author": "Luis Noreña",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "preloadable": True,
    "depends": [
        "sale", "sports_association"
    ],
    "data": [
        "views/sport_ticket_views.xml",
        "views/sale_order_views.xml"
    ],
}