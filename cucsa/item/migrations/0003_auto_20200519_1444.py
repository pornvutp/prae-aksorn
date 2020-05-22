# Generated by Django 3.0.3 on 2020-05-19 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0002_auto_20200517_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DraftFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.SmallIntegerField()),
                ('file_dir_draft', models.TextField()),
                ('file_dir_op', models.TextField()),
                ('detail', models.TextField(max_length=500)),
                ('draft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.ItemDraft')),
            ],
        ),
    ]