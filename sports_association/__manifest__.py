# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association",
    "summary": "Manage sports association members, teams and events, issues and clinics",
    "version": "17.0.1.0.0",
    # see https://odoo-community.org/page/development-status
    "development_status": "Beta",
    "category": "Sports",
    "website": "https://github.com/cbmMazagon/cursoaeodoo2024",
    "author": "Carlos Borras, Playa de Mazagon",
    # see https://odoo-community.org/page/maintainer-role for a description of the maintainer role and responsibilities
    "maintainers": ["https://github.com/cbmMazagon"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    #"preloadable": True,
    #"pre_init_hook": "pre_init_hook",
    #"post_init_hook": "post_init_hook",
    #"post_load": "post_load",
    #"uninstall_hook": "uninstall_hook",
    # "external_dependencies": {
    #     "python": [],
    #     "bin": [],
    # },
    "depends": [
        "base", "web", "portal"
    ],
    # this feature is only present for 11.0+
    # "excludes": [
    #     "module_name",
    # ],
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        # "templates/assets.xml",
        "wizards/sport_issues_done.xml",
        "views/sport_issue_views.xml",
        "views/sport_clinic_views.xml",
        "views/sport_issue_tag_views.xml",
        "views/sport_sport_views.xml",
        "views/sport_player_views.xml",
        "views/sport_team_views.xml",
        "views/sport_license_views.xml",
        "wizards/sport_create_match.xml",
        "views/sport_league_views.xml",
        "views/sport_match_views.xml",
        "views/sport_ticket_views.xml",
        "views/sport_issue.xml",
        "data/sport_license_data.xml",
        "data/sport_issue_tag_data.xml",
        "data/ir_cron.xml",
        "wizards/sport_create_issue.xml",
        "report/sports_issue_report.xml",
        "report/sports_league_report.xml",
        "report/sports_match_report.xml"
    ],
    # "demo": [
    #     "demo/assets.xml",
    #     "demo/res_partner_demo.xml",
    # ],
    # "qweb": [
    #     "static/src/xml/module_name.xml",
    # ]
}