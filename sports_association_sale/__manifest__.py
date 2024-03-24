# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sports Association Sale",
    "summary": "Manage sale Tickets",
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
        "sports_association", "sale"
    ],
    # this feature is only present for 11.0+
    # "excludes": [
    #     "module_name",
    # ],
    "data": [
        "views/sport_ticket_views.xml",
        "views/sale_order_views.xml"
         ],
}