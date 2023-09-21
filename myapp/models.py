from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    # ESTO LO QUE HACE ES QUE REGRESE LOS NOMBRES DE LOS OBJETOS EN LA TABLA
    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.project.name
