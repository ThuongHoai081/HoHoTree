from django.db import models
from django.conf import settings

class Plant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='plants')
    name_tree = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    planted_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    note = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.species})"


class ScanHistory(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='scan_histories')
    image = models.ImageField(upload_to='plant_scans/')
    diagnosis = models.CharField(max_length=255)
    confidence_score = models.FloatField()
    scan_time = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Scan on {self.scan_time.strftime('%Y-%m-%d %H:%M')} for {self.plant.name}"
