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
        "wizards/sport_create_issue.xml",
        "wizards/sport_issue_state.xml",
        "data/sport_license_data.xml",
        "data/sport_issue_tags_data.xml",
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/sport_clinic_views.xml",
        "views/sport_issue_views.xml",
        "views/sport_player_views.xml",
        "views/sport_sport_views.xml",
        "views/sport_team_views.xml",
        "views/sport_league_views.xml",
        "views/sport_match_views.xml",
        "views/sport_menuitems.xml",
    ],
}