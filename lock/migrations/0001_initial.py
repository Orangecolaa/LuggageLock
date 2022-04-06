# Generated by Django 3.2.11 on 2022-04-06 14:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrower', models.CharField(max_length=20)),
                ('lock', models.CharField(max_length=20)),
                ('borrower_phone_number', models.CharField(blank=True, max_length=30)),
                ('location', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('start_day', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_day', models.DateTimeField(default=datetime.datetime(2022, 4, 6, 15, 53, 14, 846320, tzinfo=utc))),
                ('open_or_close', models.IntegerField(choices=[(0, '使用中'), (1, '已归还')], default=0)),
                ('delete_status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.CharField(blank=True, max_length=20)),
                ('closed_at', models.DateTimeField(auto_now=True)),
                ('closed_by', models.CharField(default='', max_length=20)),
            ],
            options={
                'db_table': 'borrow_record',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('contact', models.EmailField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.CharField(default='Admin', max_length=20)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'manufacturer',
            },
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(default='', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('operation_type', models.CharField(choices=[('success', '创建'), ('waring', '更新'), ('danger', '删除'), ('info', '关闭')], default='success', max_length=20)),
                ('target_model', models.CharField(default='', max_length=20)),
                ('detail', models.CharField(default='', max_length=50)),
                ('delete_status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'user_activity',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('profile_pic', models.ImageField(blank=True, default='/static/assets/images/user/avatar-2.jpg', null=True, upload_to='profile/%Y%m%d/')),
                ('age', models.PositiveIntegerField(default=18)),
                ('gender', models.CharField(choices=[('m', '男'), ('f', '女')], default='m', max_length=10)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Lock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Title')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_borrow_times', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=10)),
                ('status', models.IntegerField(choices=[(0, '被使用'), (1, '未使用')], default=1)),
                ('delete_status', models.IntegerField(default=0)),
                ('lockshelf_number', models.CharField(default='0001', max_length=10, verbose_name='Lockshelf Number')),
                ('updated_by', models.CharField(default='Admin', max_length=20)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location', to='lock.location')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manufacturer', to='lock.manufacturer')),
            ],
            options={
                'db_table': 'lock',
            },
        ),
    ]
