# Generated by Django 3.0.3 on 2020-06-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('detail', models.CharField(blank=True, max_length=255)),
                ('default_width_x', models.PositiveSmallIntegerField()),
                ('default_width_y', models.PositiveSmallIntegerField()),
                ('default_is_openshut', models.BooleanField()),
                ('default_is_mp', models.BooleanField()),
                ('default_is_sequence', models.BooleanField()),
                ('default_is_editable', models.BooleanField()),
            ],
        ),
    ]
