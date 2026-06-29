from django.db import models


class CertificationModel(models.Model):
    """
    Represents a specific certification model.
    """

    title = models.CharField(max_length=255)
    accreditor = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.accreditor}"
