from django.apps import AppConfig

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        from django.contrib.auth.models import Group
        from django.db.utils import OperationalError, ProgrammingError

        try:
            roles = [
                ('manager_contractor', 'Менеджер Исполнитель'),
                ('manager_customer', 'Менеджер Заказчик'),
                ('representative_customer', 'Руководитель Объекта'),
                ('representative_contractor', 'Руководитель Клининга'),
                ('admin_account', 'Админ Аккаунт'),
            ]

            for role_name, _ in roles:
                Group.objects.get_or_create(name=role_name)

        except (OperationalError, ProgrammingError):
            # If the database isn't ready yet, we'll skip creating groups for now.
            pass
