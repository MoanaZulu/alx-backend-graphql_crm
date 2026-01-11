CRONJOBS = [
    ('0 */12 * * *', 'crm.cron.update_low_stock'),
]



INSTALLED_APPS = [
    # ...
    'django_crontab',
    'crm',
]



INSTALLED_APPS = [
    # ...
    'django_crontab',
    'crm',
]



CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.log_crm_heartbeat'),
]



INSTALLED_APPS = [
    # ...
    'django_crontab',
    'crm',
]

CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.log_crm_heartbeat'),
]
