# Generated by Django 5.0.7 on 2024-08-13 12:53

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=255, verbose_name='Объект')),
                ('mark_range_min', models.SmallIntegerField(default=0, verbose_name='Минимальная оценка')),
                ('mark_range_max', models.SmallIntegerField(default=5, verbose_name='Максимальная оценка')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=255, verbose_name='Пароль')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Админ')),
                ('role', models.CharField(choices=[('manager_contractor', 'Менеджер Исполнитель'), ('manager_customer', 'Менеджер Заказчик'), ('representative_customer', 'Руководитель Объекта'), ('representative_contractor', 'Руководитель Клининга')], default='manager_customer', max_length=55, verbose_name='Роль')),
                ('groups', models.ManyToManyField(blank=True, help_text='Роли к которым принадлежит пользователь.', related_name='custom_user_set', to='auth.group', verbose_name='Роли')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Специальные возможности пользователя.', related_name='custom_user_permissions_set', to='auth.permission', verbose_name='Возможности пользователя')),
                ('location', models.ManyToManyField(blank=True, related_name='users', to='main.location', verbose_name='Объекты')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_name', models.CharField(max_length=255, verbose_name='Название зоны')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='zones', to=settings.AUTH_USER_MODEL, verbose_name='Создано')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zones', to='main.location', verbose_name='Объект')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.SmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='Оценка')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Подтверждение')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Последние изменение')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='main.location', verbose_name='Объект')),
                ('user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='marks', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='main.zone', verbose_name='Зона')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_made_by_customer_not_contractor', models.BooleanField(verbose_name='Это сделано Заказчиком, а не Исполнителем')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('allocated_time', models.TimeField(default=django.utils.timezone.now, verbose_name='Время')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='./attachments/', verbose_name='Фото')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Последение изменение')),
                ('user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.location', verbose_name='Объект')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.zone', verbose_name='Зона')),
            ],
        ),
    ]
