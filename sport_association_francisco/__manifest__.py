# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association Francisco",
    "summary": "A sport association module",
    "version": "17.0.1.0.0",
    "category": "Sport",
    "author": "<FranRM(S)>",
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "base",
    ],
    "data":[
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/sport_issue_menu_items.xml",
        "views/sport_issue_views.xml",
        "views/sport_clinic_menu_items.xml",
        "views/sport_clinic_views.xml",
        "views/sport_license_menu_items.xml",
        "data/sport_license_data.xml"
    ]
}