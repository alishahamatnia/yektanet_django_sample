# Generated by Django 3.2.5 on 2021-07-12 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseAdvertising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.IntegerField(default=0)),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('baseadvertising_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='advertising_management.baseadvertising')),
                ('name', models.CharField(max_length=30)),
            ],
            bases=('advertising_management.baseadvertising',),
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('baseadvertising_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='advertising_management.baseadvertising')),
                ('title', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('img_url', models.URLField()),
                ('ad_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertising_management.advertiser')),
            ],
            bases=('advertising_management.baseadvertising',),
        ),
    ]
