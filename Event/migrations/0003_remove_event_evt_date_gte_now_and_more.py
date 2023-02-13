# Generated by Django 4.1.6 on 2023-02-12 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Person", "0001_initial"),
        ("Event", "0002_initial"),
    ]

    operations = [
        migrations.RemoveConstraint(model_name="event", name="evt_date_gte_now",),
        migrations.RemoveConstraint(
            model_name="participation", name="unique_person_event",
        ),
        migrations.RenameField(
            model_name="event", old_name="person", new_name="organizer",
        ),
        migrations.RenameField(
            model_name="participation", old_name="person", new_name="personne",
        ),
        migrations.AddField(
            model_name="event",
            name="participations",
            field=models.ManyToManyField(
                related_name="participations",
                through="Event.Participation",
                to="Person.person",
            ),
        ),
        migrations.AddConstraint(
            model_name="event",
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        "evt_date__gte",
                        datetime.datetime(2023, 2, 12, 18, 51, 46, 794993),
                    )
                ),
                name="Date doit être superieur au date systeme",
            ),
        ),
    ]