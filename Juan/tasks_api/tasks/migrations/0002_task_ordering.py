# Generated by Django 4.2.4 on 2023-08-16 22:33

from django.db import migrations, models

def assign_ordering(apps, schema_editor):
    Task = apps.get_model('tasks', 'Task')
    for i, task in enumerate(Task.objects.all().order_by('id')):
        task.ordering = i + 1
        task.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='ordering',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.RunPython(assign_ordering),
    ]
