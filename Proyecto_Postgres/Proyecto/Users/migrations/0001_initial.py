# Generated by Django 4.1.3 on 2022-11-21 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('name_user', models.CharField(max_length=30)),
                ('lastname_user', models.CharField(max_length=30)),
                ('number_user', models.IntegerField()),
                ('age_user', models.IntegerField()),
            ],
            options={
                'db_table': '_users_5',
                'managed': True,
            },
        ),
    ]
