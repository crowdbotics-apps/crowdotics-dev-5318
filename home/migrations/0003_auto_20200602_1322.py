# Generated by Django 2.2.12 on 2020-06-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ged',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abcd', models.BigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='customtext',
            name='jhjh',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
