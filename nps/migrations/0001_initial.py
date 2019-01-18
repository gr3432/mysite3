# Generated by Django 2.1.5 on 2019-01-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=2)),
                ('user_id', models.IntegerField()),
                ('feedback_text', models.CharField(max_length=200)),
                ('answer_date', models.DateField()),
            ],
        ),
    ]
