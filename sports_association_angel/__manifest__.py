# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association",
    "summary": "Manage sports",
    "version": "17.0.1.0.0",
    "author": "Angel Martinez",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
    ],
    # this feature is only present for 11.0+
    "data": [
        "views/sport_issue.xml",
    ],
}