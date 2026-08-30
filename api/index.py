import os
import sys
from pathlib import Path

# Add the project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

# Import Django and setup
import django
django.setup()

# Import WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
