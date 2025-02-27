# Generated by Django 4.2.1 on 2023-06-02 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reviewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('confirm_password', models.CharField(max_length=50)),
                ('review', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('youtube', models.BooleanField()),
            ],
        ),
    ]
