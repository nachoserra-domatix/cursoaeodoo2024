# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association",
    "summary": "Manage sports association members, teams and events",
    "version": "17.0.1.0.0",
    "category": "Sports",
    "author": "<Gabriel Recio>, Sistemas de Datos",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
    ],
    
    "data": [
        "security/ir.model.access.csv",
        "views/sport_issue.xml",
    ],
}