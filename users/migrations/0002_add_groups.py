# Generated by Django 2.2.1 on 2019-05-09 16:35

from django.contrib.auth.models import Group, Permission
from django.db import migrations


def add_group_permissions(apps, schema_editor):
    """
    Pre-defined groups
    """
    group, created = Group.objects.get_or_create(name='manager')
    if created:
        perm_codename = ['view_reservation', 'view_room']
        b_perm = Permission.objects.filter(content_type__app_label='booking',
                                           codename__in=perm_codename)
        for p in b_perm.all():
            group.permissions.add(p)


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_group_permissions),
    ]
