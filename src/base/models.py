from django.db import models

class BaseModel(models.Model): 
    
    is_deleted = models.BooleanField(default=False)


    def delete(self): 
        self.is_deleted = True 
        self.save()

    class Meta: 
        abstract = True
    