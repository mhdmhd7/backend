# Create a file named create_admin_user.py in a management/commands directory within one of your Django apps.

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates an admin user if it does not exist'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(email='admincar@admin.com').exists():
            User.objects.create_superuser(
                email='admincar@admin.com',
                password='admin'
            )
            self.stdout.write(self.style.SUCCESS('Admin user created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists'))
