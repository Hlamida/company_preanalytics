from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .constants import (
    BASE_OKVED_CHOICES,
    NALOG_CHOICES,
    OKFS_CHOICES,
    OKOPF_CHOICES,
    SMSP_CHOICES,
)


class PredictModel(models.Model):
    year = models.IntegerField(
        'Год создания компании (1991 - 2020)',
        validators=[
            MinValueValidator(1991),
            MaxValueValidator(2020),
        ],
    )
    base_okved = models.IntegerField(
        'Основной ОКВЭД',
        choices=BASE_OKVED_CHOICES,
        blank=False,
        default='46.73',
    )
    nalog = models.IntegerField(
        'Тип налогообложения',
        choices=NALOG_CHOICES,
        blank=False,
        default='Не применяется',
    )
    okfs = models.IntegerField(
        'ОКФС',
        choices=OKFS_CHOICES,
        blank=False,
        default='12',
    )
    okopf = models.IntegerField(
        'ОКОПФ',
        choices=OKOPF_CHOICES,
        blank=False,
        default='12300',
    )
    smsp = models.IntegerField(
        'СМСП',
        choices=SMSP_CHOICES,
        blank=False,
        default='Не входит',
    )
