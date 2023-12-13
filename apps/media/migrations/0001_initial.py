# Generated by Django 5.0 on 2023-12-13 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='posts')),
                ('is_first', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'media',
                'managed': True,
            },
        ),
    ]