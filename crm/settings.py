CRONJOBS = [
    ('0 */12 * * *', 'crm.cron.update_low_stock'),
]



INSTALLED_APPS = [
    # ...
    'django_crontab',
    'crm',
]
