# Generated by Django 4.0.5 on 2022-11-26 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metering_billing", "0083_invoicelineitem_metadata"),
    ]

    operations = [
        migrations.AddField(
            model_name="plancomponent",
            name="proration_granularity",
            field=models.CharField(
                choices=[
                    ("seconds", "Second"),
                    ("minutes", "Minute"),
                    ("hours", "Hour"),
                    ("days", "Day"),
                    ("months", "Month"),
                    ("quarters", "Quarter"),
                    ("years", "Year"),
                    ("total", "Total"),
                ],
                default="total",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="historicalmetric",
            name="granularity",
            field=models.CharField(
                blank=True,
                choices=[
                    ("seconds", "Second"),
                    ("minutes", "Minute"),
                    ("hours", "Hour"),
                    ("days", "Day"),
                    ("months", "Month"),
                    ("quarters", "Quarter"),
                    ("years", "Year"),
                    ("total", "Total"),
                ],
                default="total",
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="metric",
            name="granularity",
            field=models.CharField(
                blank=True,
                choices=[
                    ("seconds", "Second"),
                    ("minutes", "Minute"),
                    ("hours", "Hour"),
                    ("days", "Day"),
                    ("months", "Month"),
                    ("quarters", "Quarter"),
                    ("years", "Year"),
                    ("total", "Total"),
                ],
                default="total",
                max_length=10,
                null=True,
            ),
        ),
    ]