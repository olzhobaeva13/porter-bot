# Generated by Django 4.0.6 on 2022-07-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('porter', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('movers', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('dispersal', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('trash', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]