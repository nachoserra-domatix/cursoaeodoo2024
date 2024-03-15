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
        "web",
    ],
    
    "data": [
        "security/sport_issue_security.xml",
        "security/ir.model.access.csv",        
        "views/sport_issue_views.xml",
        "views/sport_clinic_views.xml",
        "views/sport_license_views.xml",
        "views/sport_issue_tag_views.xml",
        "views/sport_team_views.xml",
        "views/sport_player_views.xml",
        "views/sport_league_views.xml",
        "views/sport_match_views.xml",
        "views/sport_sport_views.xml",
        "views/sport_association_menus.xml",        
        "data/sport_license_data.xml",
        "data/sport_issue_tag_data.xml",
        "report/sport_issue_report.xml",
        "report/sport_league_report.xml",
        "wizard/sport_create_issue.xml",
        "wizard/sport_league_match_views.xml",
        "data/ir_cron.xml",
    ],    
}