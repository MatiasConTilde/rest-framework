# Copyright 2018 ACSONE SA/NV
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Base Rest Demo",
    "summary": """
        Demo addon for Base REST""",
    "version": "13.0.4.2.0",
    "development_status": "Beta",
    "license": "LGPL-3",
    "author": "ACSONE SA/NV, " "Odoo Community Association (OCA)",
    "maintainers": ["lmignon"],
    "website": "https://github.com/OCA/rest-framework",
    "depends": [
        "base_rest",
        "base_rest_datamodel",
        "base_rest_pydantic",
        "component",
        "extendable",
    ],
    "data": [],
    "demo": [],
    "external_dependencies": {
        "python": ["jsondiff", "extendable-pydantic", "pydantic"]
    },
    "installable": True,
}
