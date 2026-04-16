from django.contrib.auth.models import AbstractUser
from django.db import models
import random

class User(AbstractUser):
    is_active = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)

    def generate_code(self):
        code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        self.confirmation_code = code
        self.save()
        return code