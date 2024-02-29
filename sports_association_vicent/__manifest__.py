# Copyright 2024 Vicent Esteve - vesteve@ontinet.com
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": "Sports Association",
    "summary": "Manage sports association members, teams and events",
    "version": "17.0.1.0.0",
    "category": "Sports",
    "author": "<Vicent Esteve>",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["base",],
    "data": [
        "data/sport_license_data.xml",
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/sport_issue_views.xml",
        "views/sport_issue_tag_views.xml",
        "views/sport_clinic_views.xml",
        "views/sport_menuitems.xml",
    ],
}
