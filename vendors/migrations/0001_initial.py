# Generated by Django 5.1.4 on 2025-04-17 14:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='vendor_logos/')),
                ('cover_image', models.ImageField(upload_to='vendor_covers/')),
                ('address', models.TextField()),
                ('registration_number', models.CharField(max_length=50)),
                ('tax_number', models.CharField(max_length=50)),
                ('website', models.URLField(blank=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('business_certificate', models.FileField(upload_to='vendor_documents/')),
                ('tax_certificate', models.FileField(upload_to='vendor_documents/')),
                ('insurance_certificate', models.FileField(upload_to='vendor_documents/')),
                ('status', models.CharField(choices=[('pending', 'Pending Approval'), ('approved', 'Approved'), ('suspended', 'Suspended'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('is_featured', models.BooleanField(default=False)),
                ('verification_notes', models.TextField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('bank_name', models.CharField(max_length=100)),
                ('bank_account_name', models.CharField(max_length=100)),
                ('bank_account_number', models.CharField(max_length=50)),
                ('bank_routing_number', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('business', 'Business Certificate'), ('tax', 'Tax Certificate'), ('insurance', 'Insurance Certificate'), ('other', 'Other')], max_length=20)),
                ('file', models.FileField(upload_to='vendor_documents/')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('verified_at', models.DateTimeField(blank=True, null=True)),
                ('verification_notes', models.TextField(blank=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='VendorReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor')),
            ],
            options={
                'unique_together': {('user', 'vendor')},
            },
        ),
    ]
