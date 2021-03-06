# Generated by Django 2.2.7 on 2019-11-28 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inaraApp', '0011_proc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whyus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.TextField(blank=True, max_length=520, null=True)),
                ('p1_d', models.TextField(blank=True, max_length=520, null=True)),
                ('p2', models.TextField(blank=True, max_length=520, null=True)),
                ('p2_d', models.TextField(blank=True, max_length=520, null=True)),
                ('p3', models.TextField(blank=True, max_length=520, null=True)),
                ('p3_d', models.TextField(blank=True, max_length=520, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='home/')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='proc',
            name='d1',
            field=models.TextField(blank=True, max_length=520),
        ),
        migrations.AlterField(
            model_name='proc',
            name='t1',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
