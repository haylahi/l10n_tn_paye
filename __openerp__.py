{
    'name': 'l10n_tn_paye',
    'category': 'Localization/Payroll',
    'author': 'Open Vision',
    'depends': ['hr_payroll'],
    'version': '1.0',
  'website': 'http://www.openvision-tn.com',
    'description': """Tunisian Payroll Rules.
======================

    * IRPP/CNSS...
    """,
    'active': False,
    'update_xml':['l10n_tn_paye_view.xml'],
	 'data': [
        'l10n_tn_paye_view.xml',
        'l10n_tn_paye_data.xml',
		
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
	'images': ['images/l10n_tn_paye_categories.jpeg', 'images/l10n_tn_paye_structure.jpeg', 'images/l10n_tn_paye_bulletin.jpeg'],

}
