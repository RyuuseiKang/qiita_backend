# Generated by Django 3.2.9 on 2022-06-10 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0003_alter_item_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lgtm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lgtms', to='items.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lgtms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
