# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association Francisco",
    "summary": "A sport association module",
    "version": "17.0.1.0.0",
    "category": "Sport",
    "author": "<FranRM(S)>",
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "base","web"
    ],
    "data":[
        "security/groups.xml",
        "security/ir.model.access.csv",
        "wizard/sport_create_issue.xml",
        "wizard/check_all_issues.xml",
        "views/sport_clinic_menu_items.xml",
        "views/sport_clinic_views.xml",
        "views/sport_issue_menu_items.xml",
        "views/sport_issue_views.xml",
        "views/sport_license_menu_items.xml",
        "views/sport_player_menu_items.xml",
        "views/sport_sport_menu_items.xml",
        "views/sport_team_menu_items.xml",
        "views/sport_player_views.xml",
        "views/sport_sport_views.xml",
        "views/sport_team_views.xml",
        "data/sport_license_data.xml",
        "views/sport_leage_menu_items.xml",
        "views/sport_leage_views.xml",
        "views/sport_match_menu_items.xml",
        "views/sport_match_views.xml",
        "data/sport_tag_data.xml",
        "data/ir_cron.xml",
        "report/paper_format.xml",
        "report/sport_issue_report.xml"
    ]
}