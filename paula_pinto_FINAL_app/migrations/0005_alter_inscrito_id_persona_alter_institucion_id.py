# Generated by Django 4.2.4 on 2023-12-21 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paula_pinto_FINAL_app', '0004_alter_inscrito_id_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscrito',
            name='id_persona',
            field=models.CharField(max_length=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='id',
            field=models.CharField(max_length=2, primary_key=True, serialize=False),
        ),
    ]