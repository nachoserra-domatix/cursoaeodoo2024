# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association",
    "summary": "Sports Association",
    "version": "17.0",
    "category": "Uncategorized",
    "author": "<AUTHOR(S)>, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": [
        "base",
    ],
    "data": [
        "data/sport_license_data.xml",
        "data/sport_issue_tags_data.xml",
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/clinic_view.xml",
        "views/sport_issue_views.xml",
        "views/sport_menuitems.xml",
    ],
}