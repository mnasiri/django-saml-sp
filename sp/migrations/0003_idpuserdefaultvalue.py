# Generated by Django 2.2.7 on 2019-12-05 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0002_idpattribute_always_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdPUserDefaultValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('idp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_defaults', to='sp.IdP', verbose_name='identity provider')),
            ],
            options={
                'verbose_name': 'identity provider user default value',
                'verbose_name_plural': 'identity provider user default values',
                'unique_together': {('idp', 'field')},
            },
        ),
    ]
