# Generated by Django 3.1.2 on 2020-10-28 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teas', '0002_auto_20201028_1218'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Suggestion',
        ),
        migrations.AlterField(
            model_name='tea',
            name='suggestion',
            field=models.CharField(max_length=50),
        ),
    ]
