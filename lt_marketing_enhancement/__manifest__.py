##############################################################################
# Copyright (c) 2022 lumitec GmbH (https://www.lumitec.solutions)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
{
    'name': 'Marketing Enhancement',
    'summary': 'Enhanced marketing',
    'author': "lumitec GmbH",
    'website': "https://www.lumitec.solutions",
    'category': 'Marketing',
    'version': '15.0.1.0.0',
    'license': 'OPL-1',
    'images': ['static/description/thumbnail.gif'],
    'depends': [
        'base',
        'mail',
        'mass_mailing',
        'crm',
        'project',
        'utm',
        'calendar',
        'event',
        'website'
    ],
    'data': [
        'data/cron.xml',
        'data/mailing_contact_token_mail_data.xml',
        'security/ir.model.access.csv',
        'security/res_groups.xml',
        'views/res_config_settings_views.xml',
        'views/mailing_contact_token_templates.xml',
        'views/mailing_tag_views.xml',
        'views/mailing_contact_views.xml',
        'views/project_views.xml',
        'views/calendar_event_views.xml',
        'views/event_views.xml',
        'views/utm_campaign_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
