# Copyright NuoBiT Solutions - Kilian Niubo <kniubo@nuobit.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    "name": "Sports Association",
    "version": "17.0.1.0.0",
    "author": "NuoBiT Solutions SL",
    "license": "AGPL-3",
    "category": "base",
    "website": "https://github.com/nuobit/odoo-addons",
    "depends": [
        "base",
    ],
    "data": [
        "data/sport_license_data.xml",
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/sport_clinic_views.xml",
        "views/sport_issue_tag_views.xml",
        "views/sport_issue_views.xml",
        "views/sport_player_views.xml",
        "views/sport_sport_views.xml",
        "views/sport_team_views.xml",
        "views/sport_menuitems.xml",
    ],
}
