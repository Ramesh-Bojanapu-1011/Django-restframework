from django.db import models

# Create your models here.

class SequentialIDModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            last = self.__class__.objects.order_by("-id").first()
            self.id = (last.id + 1) if last else 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        model_class = self.__class__
        super().delete(*args, **kwargs)

        # Resequence all objects to ensure ids are 1...n
        all_objs = model_class.objects.all().order_by("id")
        for idx, obj in enumerate(all_objs, start=1):
            if obj.id != idx:
                # To update primary key, we must use raw SQL or recreate the object
                model_class.objects.filter(pk=obj.pk).update(id=idx)


class Item(SequentialIDModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name