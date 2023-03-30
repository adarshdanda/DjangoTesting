from django.db import models
import uuid

# Create your models here.
class BaseProduct(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name            = models.CharField(max_length=200, null=True)
    brand           = models.CharField(blank = False, max_length=300, null=True)
    signatures      = models.CharField(max_length=500, blank=True, null=True)
    description     = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['name']
    
 
class FinalProduct(BaseProduct):
    size            = models.IntegerField(blank = False)
    color           = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.name
    



    
#    class Meta(BaseProduct.Meta):
#        ordering = ['brand']

#   x=BaseProduct.objects.all()
#   namelist = []
#   for product in x:
#     namelist.append(product.name)
#   product         = models.CharField(max_length=300, choices=namelist)
#    product         = models.ManyToOneRel(BaseProduct, on_delete=models.CASCADE)
#
#    @property
#    def name(self):
#        return self.product.name
#
#    size            = models.IntegerField(blank = False)
#    color           = models.TextField(blank=False)


