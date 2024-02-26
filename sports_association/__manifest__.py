# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "sports association",
    "summary": "Module for sports association",
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
        "base",
    ],
    
    "data": [
        "security/ir.model.access.csv",
        "views/sport_issue_views.xml"
    ],    
}