# Generated by Django 3.0.8 on 2020-09-30 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100000)),
                ('location', models.CharField(max_length=100)),
                ('size', models.SmallIntegerField()),
                ('extras', models.CharField(max_length=500)),
                ('features', models.CharField(max_length=500)),
                ('category', models.CharField(choices=[('Sale', 'Sale'), ('Rent', 'Rent'), ('Buy', 'Buy')], max_length=10)),
                ('image1', models.ImageField(default='property_default.png', upload_to='properties_pics')),
                ('image2', models.ImageField(default='property_default.png', upload_to='properties_pics')),
                ('image3', models.ImageField(default='property_default.png', upload_to='properties_pics')),
                ('image4', models.ImageField(default='property_default.png', upload_to='properties_pics')),
                ('image5', models.ImageField(default='property_default.png', upload_to='properties_pics')),
            ],
        ),
        migrations.CreateModel(
            name='InteriorFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedroom', models.SmallIntegerField()),
                ('bathroom', models.SmallIntegerField()),
                ('kitchen', models.SmallIntegerField()),
                ('reception', models.SmallIntegerField()),
                ('prop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Property')),
            ],
        ),
        migrations.CreateModel(
            name='ExteriorFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('garage', models.SmallIntegerField()),
                ('parking', models.SmallIntegerField()),
                ('domestic_accomodation', models.SmallIntegerField()),
                ('security', models.BooleanField()),
                ('pool', models.BooleanField()),
                ('prop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Property')),
            ],
        ),
    ]