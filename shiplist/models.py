from django.db import models

STATUS_CHOICES = (
    (0, 'Pending'),
    (1, 'Untracked'),
    (2, 'Sailing'),
    (3, 'Sunken'),
)

class Ship(models.Model):
    ship_no = models.IntegerField()
    half = models.CharField(max_length=50)
    half_username = models.CharField(max_length=50, blank=True)
    half_other = models.CharField(max_length=50)
    half_other_username = models.CharField(max_length=50, blank=True)

    # 0 = Pending, 1 = Untracked, 2 = Sailing, 3 = Sunken
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    shipped_date = models.DateTimeField(auto_now_add=True)
    remarks = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.half} x {self.half_other}"
    
class Rule(models.Model):
    article_number = models.FloatField()
    rule_content = models.TextField()
