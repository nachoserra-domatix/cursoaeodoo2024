# Copyright <2024> <Angel Martinez>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association",
    "summary": "Manage sports association members, teams, events",
    "version": "17.0.1.0.0",
    "category": "Sports",
    "author": "Angel Martinez",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
    ],

    "data": ["data/sport_license_data.xml",
             "security/groups.xml",
             "security/ir.model.access.csv",
             "views/sport_issue.xml",
             "views/sport_issue_tag_views.xml",
             "views/sport_clinic_views.xml",
             "views/sport_issue_views.xml",
             ],
}