from django.utils.translation import gettext_lazy as _
from django.db import models
from solidaire_common.models import AbstractModel
from solidaire_auth.models import User

# Create your models here.

class Post(AbstractModel):
    
    class Status(models.TextChoices):
        DRAFT = "draft", _("Draft")
        PUBLISHED = "published", _("Published")
        REMOVED  = "removed", _("Removed")
    
    owner = models.ForeignKey(
        User,
        verbose_name=("Owner"),
        related_name="posts",
        on_delete=models.CASCADE,
    )
    
    title = models.CharField(_("Title"), max_length=255)
    body = models.TextField(_("Body"))
    
    street = models.CharField(_("Street"), max_length=255, null=True)
    city = models.CharField(_("City"), max_length=255, null=True)
    state = models.CharField(_("State"), max_length=255, null=True)
    country = models.CharField(_("Country"), max_length=255, null=True)
    postal_code = models.CharField(_("Postal Code"), max_length=8, null=True)
    
    status = models.CharField(
        _("Status"), max_length=16, choices=Status.choices, default=Status.DRAFT
    )
    
    def __str__(self):
        return self.title

class Comment(AbstractModel):
    owner = models.ForeignKey(
        User,
        verbose_name=("Owner"),
        related_name="comments",
        on_delete=models.CASCADE,
    )
    
    post = models.ForeignKey(
        Post,
        verbose_name=("Post"),
        related_name="comments",
        on_delete=models.CASCADE,
    )
    
    body = models.TextField(_("Body"))
    
    is_deleted = models.BooleanField(_("Is deleted"), default=False)
    
    def __str__(self):
        return self.body