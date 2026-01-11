#!/bin/bash

# Run Django shell command to delete inactive customers
deleted_count=$(python3 ~/alx-backend-graphql_crm/manage.py shell -c "
from crm.models import Customer
from django.utils import timezone
from datetime import timedelta

cutoff = timezone.now() - timedelta(days=365)
qs = Customer.objects.filter(order__isnull=True, created_at__lt=cutoff)
count = qs.count()
qs.delete()
print(count)
")

# Log result with timestamp
timestamp=$(date +"%d/%m/%Y-%H:%M:%S")
echo \"$timestamp Deleted customers: $deleted_count\" >> /tmp/customer_cleanup_log.txt
