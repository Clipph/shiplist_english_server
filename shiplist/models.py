from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    (0, 'Pending'),
    (1, 'Untracked'),
    (2, 'Sailing'),
    (3, 'Sunken'),
    (4, 'Dropped'),
)

RULES_SECTIONS = (
    (0, 'CEO Policies'),
    (1, 'Staff Policies'),
    (2, 'General Policies'),
)

class Ship(models.Model):
    ship_no = models.AutoField(primary_key=True)
    half = models.CharField(max_length=50)
    half_username = models.CharField(max_length=50, blank=True)
    half_other = models.CharField(max_length=50)
    half_other_username = models.CharField(max_length=50, blank=True)

    status = models.IntegerField(choices=STATUS_CHOICES, default=0, help_text="'Pending' is for ships you're not sure about. 'Untracked' is for ghost ships. 'Dropped' is for discarded ships.")

    shipped_date = models.DateTimeField(auto_now_add=True)
    remarks = models.CharField(max_length=255, blank=True)

    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='ships_updated')

    def __str__(self):
        return f"Ship no. {self.ship_no}"
    
class Rule(models.Model):
    section = models.IntegerField(choices=RULES_SECTIONS, default=0)
    article_number = models.FloatField()
    title = models.CharField(max_length=100, blank=True)
    rule_content = models.TextField()
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='rules_updated')

    def __str__(self):
        return f"Article {self.article_number} - {self.title}"