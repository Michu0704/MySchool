#!/bin/bash
#script for loading inital data
python manage.py shell <<'EOF'
from my_schools.models import Catalog
Catalog.objects.all().delete()
EOF
python manage.py loaddata initial_data.json
