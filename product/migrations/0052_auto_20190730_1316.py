# Generated by Django 2.2.1 on 2019-07-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0051_auto_20190729_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='alegrogoods',
            name='description_clean',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='alegrogoods',
            name='price_pol',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='alegrogoods',
            name='car_model',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]