# Generated by Django 3.2.4 on 2021-12-12 23:48


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gifts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wishlists', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('gift_given', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gift_given', to='gifts.gift')),
                ('gift_received', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gift_received', to='gifts.gift')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wishlist_owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wishlist_owner', to='wishlists.wishlist')),
                ('wishlist_sender', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wishlist_sender', to='wishlists.wishlist')),
            ],
        ),
    ]
