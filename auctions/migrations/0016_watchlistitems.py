# Generated by Django 3.2 on 2021-05-24 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20210524_0654'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchlistItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.listings')),
                ('watchlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', related_query_name='item', to='auctions.watchlist')),
            ],
        ),
    ]