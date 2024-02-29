# Copyright 2024 Lorena Garrido
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association",
    "summary": "Manage sports association members, teams and events",
    "version": "17.0.1.0.0",
    "category": "Sports",
    "author": "Lorena Garrido, Ontinet",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/sport_issue_views.xml",
        "views/sport_clinic_views.xml",
        "views/sport_issue_tag_views.xml",
        "views/sport_team_views.xml",
        "views/sport_sport_views.xml",
        "views/sport_player_views.xml",
        "views/sport_issue_menu.xml",
        "data/sport_issue_tag.xml",
        "data/sport_license_data.xml",
    ],
}