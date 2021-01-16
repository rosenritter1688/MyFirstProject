# Generated by Django 3.1.3 on 2020-11-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20201127_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_desc', models.CharField(max_length=200)),
                ('item_price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='item',
        ),
    ]
