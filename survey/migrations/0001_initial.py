# Generated by Django 3.2.7 on 2021-09-30 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.patient')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.type')),
            ],
        ),
        migrations.CreateModel(
            name='Question_Response',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_id', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=200)),
                ('response_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.response')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.type')),
            ],
        ),
    ]
