from django.contrib.gis.db import models

class Point(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField()

    point = models.PointField()

    def __str__(self):
        return self.title

    def to_json(self):
        return {'lat': self.point.y, 'lng': self.point.x}
