# License GPL-3.0 or later (https://www.gnu.org/licenses/gpl).
{
    "name": "Sports Association",
    "summary": "Manage sports association members, teams and events",
    "version": "17.0.1.0.0",
    "category": "Sports",
    "author": "Adasat Torres de Leon",
    "license": "GPL-3",
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
             "views/sport_issue_views.xml",
             "views/sport_issue_tag_views.xml",
             "views/sport_sport_views.xml",
             "views/sport_team_views.xml",
             "views/sport_player_views.xml",
             "views/sport_player_position_views.xml",
             "views/sport_clinic_views.xml",
             "views/sport_menuitems.xml",
             "wizards/wizard_change_headline_player.xml",
             ],
}