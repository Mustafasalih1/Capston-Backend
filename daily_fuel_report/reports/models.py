from django.db import models
from location.models import Site
from users.models import User
# Createing report models .

class DailyFuelReport(models.Model):
    
    report_date = models.DateField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="reports")
    fuel_consumed = models.CharField(max_length=50)
    planned_quantity = models.CharField(max_length=40)
    delivered_quantity = models.CharField(max_length=40)
    remaining_quantity = models.CharField(max_length=40)
    status = models.CharField(max_length=100)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    craeted_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.site} - {self.report_date}"