from django.apps import AppConfig
from django.conf import settings
from django.db.utils import OperationalError
from django.contrib.auth.hashers import make_password

class CarAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'car_app'

    def ready(self):
        if 'migrate' not in settings.INSTALLED_APPS:
            from car_app.models import User
            try:
                if not User.objects.filter(email='admincar@admin.com').exists():
                    admin_user = User(
                        name='admincar',
                        email='admincar@admin.com',
                        phone_number='00000000',
                        role='admin'
                    )
                    admin_user.password = make_password('admin')  # Hashing the password
                    admin_user.save()
            except OperationalError:
                pass
