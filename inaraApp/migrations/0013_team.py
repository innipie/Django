# Generated by Django 2.2.7 on 2019-11-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inaraApp', '0012_auto_20191128_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.TextField(blank=True, max_length=520, null=True)),
                ('team1', models.ImageField(blank=True, null=True, upload_to='home/')),
                ('team2', models.ImageField(blank=True, null=True, upload_to='home/')),
                ('team3', models.ImageField(blank=True, null=True, upload_to='home/')),
            ],
        ),
    ]