from django.db import models



class Todo(models.Model):
    PRIORITIES = (
        ('LOW','LOW'),
        ('MEDIUM','MEDIUM'),
        ('HIGH','HIGH'),

    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    priority = models.CharField(max_length=8, choices=PRIORITIES, default='MEDIUM')
    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(null=True)
    
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.title