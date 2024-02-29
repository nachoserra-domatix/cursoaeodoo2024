# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association",
    "summary": "Module summary",
    "version": "17.0.1.0.0",
    # see https://odoo-community.org/page/development-status
    #"development_status": "Alpha|Beta|Production/Stable|Mature",
    "category": "Sports",
    #"website": "https://github.com/OCA/<repo>" or "https://github.com/OCA/<repo>/tree/<branch>/<addon>",
    #"author": "<AUTHOR(S)>, Odoo Community Association (OCA)",
    # see https://odoo-community.org/page/maintainer-role for a description of the maintainer role and responsibilities
    #"maintainers": ["your-github-login"],
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
        "base",
    ],
    # this feature is only present for 11.0+
    # "excludes": [
    #     "module_name",
    # ],
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        # "templates/assets.xml",
        "views/sport_issue_views.xml",
        "views/sport_clinic_views.xml",
        "views/sport_issue_tag_views.xml",
        "views/sport_sport_views.xml",
        "views/sport_player_views.xml",
        "views/sport_team_views.xml",
        # "wizards/wizard_model_view.xml",
        "views/sport_issue.xml",
        "data/sport_license_data.xml",
        "data/sport_issue_tag_data.xml",
    ],
    "demo": [
        "demo/assets.xml",
        "demo/res_partner_demo.xml",
    ],
    # "qweb": [
    #     "static/src/xml/module_name.xml",
    # ]
}