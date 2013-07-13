{
    'name': 'l10n_tn_paye',
    'category': 'Localization/Payroll',
    'author': 'Open Vision',
    'depends': ['hr_payroll'],
    'version': '1.0',
  	'website': 'http://www.openvision-tn.com',
    'description': """Tunisian Payroll Rules.
=========================================================
    * IRPP/CNSS...
    """,

	'data': [
	        'l10n_tn_paye_view.xml',
	        'l10n_tn_paye_data.xml',
    		],
    'installable': True,
    'auto_install': False,
}
