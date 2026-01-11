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
    
    def save(self, *args, **kwargs):
        self.remaining_quantity = self.planned_quantity - self.delivered_quantity

        if self.delivered_quantity == 0:
            self.status = "Not Delivered"
        elif self.delivered_quantity < self.planned_quantity:
            self.status = "Partial"
        else:
            self.status = "Completed"

        super().save(*args, **kwargs)