{
    "name": "Sports Association",
    "summary": "Manage sports association members, teams and events",
    "version": "17.0.1.0.0",
    "author": "<Gonzalo Crosio>, Crosio",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["base"],

    "data": [
        'security/ir.model.access.csv',
        'views/sport_issue.xml',
    ],

}