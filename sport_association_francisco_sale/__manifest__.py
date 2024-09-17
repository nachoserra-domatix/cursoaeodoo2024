# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association Francisco Sale",
    "summary": "A sport association sale module",
    "version": "17.0.1.0.0",
    "category": "Sport",
    "author": "<FranRM(S)>",
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "sale","sport_association_francisco"
    ],
    "data":[
        "views/sport_ticket_views.xml",
        "views/sale_order.xml",
    ]
}