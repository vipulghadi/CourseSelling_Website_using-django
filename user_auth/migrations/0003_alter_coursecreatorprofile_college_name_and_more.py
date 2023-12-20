# Generated by Django 4.2.5 on 2023-12-11 15:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_alter_coursecreatorprofile_creator_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecreatorprofile',
            name='college_name',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='coursecreatorprofile',
            name='creator_id',
            field=models.UUIDField(default=uuid.UUID('8d711490-904f-4c02-a84d-48d458478ef7')),
        ),
        migrations.AlterField(
            model_name='coursecreatorprofile',
            name='full_name',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='coursecreatorprofile',
            name='github_id',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='coursecreatorprofile',
            name='linkedin_id',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='coursecreatorprofile',
            name='social_id',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='courseuserprofile',
            name='college_name',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='courseuserprofile',
            name='github_id',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='courseuserprofile',
            name='linkedin_id',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='courseuserprofile',
            name='social_id',
            field=models.URLField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='courseuserprofile',
            name='student_id',
            field=models.UUIDField(default=uuid.UUID('a7a53cc7-11b8-4dac-9b4f-860da7800aee'), primary_key=True, serialize=False, unique=True),
        ),
    ]