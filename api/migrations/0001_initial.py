# Generated by Django 4.2.11 on 2025-05-13 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("side", models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("official", models.CharField(blank=True, max_length=200, null=True)),
                ("cca2", models.CharField(max_length=2, unique=True)),
                ("cca3", models.CharField(blank=True, max_length=3, null=True)),
                ("ccn3", models.CharField(blank=True, max_length=3, null=True)),
                ("cioc", models.CharField(blank=True, max_length=3, null=True)),
                (
                    "independent",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        default="officially-assigned",
                        max_length=200,
                        null=True,
                    ),
                ),
                ("un_member", models.BooleanField(default=False)),
                ("region", models.CharField(blank=True, max_length=200, null=True)),
                ("subregion", models.CharField(blank=True, max_length=200, null=True)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
                (
                    "landlocked",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
                ("area", models.FloatField(blank=True, null=True)),
                ("flag_emoji", models.CharField(blank=True, max_length=200, null=True)),
                ("population", models.BigIntegerField(blank=True, null=True)),
                ("fifa", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "startOfWeek",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("google_maps", models.URLField(blank=True, null=True)),
                ("openstreet_maps", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Idd",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("root", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="idds",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Translation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("language", models.CharField(blank=True, max_length=200, null=True)),
                ("official", models.CharField(blank=True, max_length=200, null=True)),
                ("common", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TopLevelDomain",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("domain", models.CharField(max_length=200)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tlds",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Timezone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="timezones",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="suffix",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("suffix", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "Idd",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="suffixes",
                        to="api.idd",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PostalCode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("format", models.CharField(blank=True, max_length=200, null=True)),
                ("regex", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="postal_codes",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NativeName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("official", models.CharField(blank=True, max_length=200, null=True)),
                ("common", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="native_names",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=200)),
                ("name", models.CharField(max_length=200)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="languages",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Gini",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.CharField(blank=True, max_length=200, null=True)),
                ("value", models.FloatField(blank=True, null=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gini",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Flag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("png_url", models.URLField(blank=True, null=True)),
                ("svg_url", models.URLField(blank=True, null=True)),
                ("alt_text", models.TextField(blank=True, null=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="flag",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Demonym",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("f", models.CharField(blank=True, max_length=200, null=True)),
                ("m", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="demonyms",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(blank=True, max_length=200, null=True)),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("symbol", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="currencies",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Continent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="continents",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CoatOfArms",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("png_url", models.URLField(blank=True, null=True)),
                ("svg_url", models.URLField(blank=True, null=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="coat_of_arms",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CarSign",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sign", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="car_sign",
                        to="api.car",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="car",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cars",
                to="api.country",
            ),
        ),
        migrations.CreateModel(
            name="capitalInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lat", models.FloatField(blank=True, null=True)),
                ("lng", models.FloatField(blank=True, null=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="capital_info",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="capital",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("capital", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="capitals",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Border",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("border_country_code", models.CharField(max_length=3)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="borders",
                        to="api.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="altSpellings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "alt_spelling",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="alt_spellings",
                        to="api.country",
                    ),
                ),
            ],
        ),
    ]
