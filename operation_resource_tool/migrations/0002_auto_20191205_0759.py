# Generated by Django 2.1.5 on 2019-12-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_resource_tool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('origin_name', models.CharField(blank=True, db_index=True, max_length=300, null=True, verbose_name='origin_name')),
                ('type', models.CharField(blank=True, db_index=True, max_length=300, null=True, verbose_name='type')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='name')),
                ('path', models.CharField(blank=True, max_length=300, null=True, verbose_name='path')),
                ('created_at', models.DateTimeField(db_index=True, null=True, verbose_name='created_at')),
            ],
        ),
        migrations.DeleteModel(
            name='SaveFileModel',
        ),
    ]
