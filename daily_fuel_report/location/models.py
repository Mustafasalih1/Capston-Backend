from django.db import models

# Createing location models .

class State(models.Model):
    
    state_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.state_name


class Site(models.Model):
    
    site_name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE , related_name="sites")
    power_source = models.CharField(max_length=50)
    capacity = models.CharField(max_length=40)
    status = models.CharField(max_length=40)
    craeted_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.site_name
    
