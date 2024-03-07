# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association",
    "summary": "Manage sports summary",
    "version": "17.0.1.0.0",
    "category": "Sports",
    "author": "<AUTHOR(S)>",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "data/sport_license_data.xml",
        "data/sport_issue_tag_data.xml",
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/sport_license_views.xml",
        "views/sport_issue_views.xml",
        "views/sport_clinic_views.xml",
        "views/sport_sport_views.xml",
        "views/sport_team_views.xml",
        "views/sport_player_views.xml",
        "views/sport_league_views.xml",
        "views/sport_match_views.xml",
        "views/sport_menuitems.xml",
        ]
}