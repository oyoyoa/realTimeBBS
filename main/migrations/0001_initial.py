# Generated by Django 2.2.2 on 2019-07-18 10:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import main.models.base
import main.models.user
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(default='guest user', max_length=64)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, validators=[django.core.validators.EmailValidator])),
                ('password', models.CharField(max_length=254)),
                ('icon', models.ImageField(blank=True, null=True, upload_to=main.models.user.icon_file_path)),
                ('device_uuid', models.UUIDField(default=uuid.uuid4)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            bases=(main.models.base.DeletePreviousFileMixin, models.Model),
            managers=[
                ('objects', main.models.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('tweet_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=140, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
