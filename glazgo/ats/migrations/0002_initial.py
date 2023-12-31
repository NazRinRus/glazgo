# Generated by Django 4.2.7 on 2023-11-23 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='recruter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='recruters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='requirements',
            field=models.ManyToManyField(related_name='requirements', to='ats.requirements'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='responsibilities',
            field=models.ManyToManyField(related_name='responsibilities', to='ats.responsibilities'),
        ),
        migrations.AddField(
            model_name='message',
            name='candidate_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='candidate_messages', to='ats.candidate'),
        ),
        migrations.AddField(
            model_name='message',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cphistory',
            name='candidat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CPHC', to='ats.candidate'),
        ),
        migrations.AddField(
            model_name='cphistory',
            name='recruter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='CPHR', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cphistory',
            name='vacancy_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CPHV', to='ats.vacancy'),
        ),
        migrations.AddField(
            model_name='candidatepromotion',
            name='candidat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='candidat', to='ats.candidate'),
        ),
        migrations.AddField(
            model_name='candidatepromotion',
            name='recruter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='recruter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='candidatepromotion',
            name='vacancy_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vacancy', to='ats.vacancy'),
        ),
        migrations.AddField(
            model_name='callcandidate',
            name='candidate_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ats.candidate'),
        ),
        migrations.AddField(
            model_name='callcandidate',
            name='vacancy_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ats.vacancy'),
        ),
    ]
