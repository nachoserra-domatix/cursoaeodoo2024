# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association",
    "summary": "Manager sports association members, teams and sports events",
    "version": "17.0.1.0.0",
    "category": "Sports",
    "author": "<Jordi Navarro>, I2T",
    "maintainers": ["JordiNavarro"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
    ],
   "data":["security/grupos.xml",
         "security/ir.model.access.csv",
         "views/sport_issue_views.xml",
         "views/sport_menuitems.xml",
         "data/sport_license_data.xml"
         ]
}