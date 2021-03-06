# Generated by Django 3.2.5 on 2021-08-02 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_light_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Road',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='The road name', max_length=20, null=True)),
                ('distance', models.FloatField(blank=True, help_text='The distance of the road', null=True)),
                ('direction', models.CharField(choices=[('R', 'Right to left'), ('L', 'Left to right'), ('U', 'Up to down'), ('D', 'down to up')], help_text='The direction of the road', max_length=2)),
                ('traffic_queue', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, default='A', help_text='Road status availability', max_length=2, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
