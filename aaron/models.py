from django.db import models
from django import forms
from wagtail.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.documents.blocks import DocumentChooserBlock
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TagBase, ItemBase

class AaronsTag(models.Model):
    tag = models.CharField(max_length=100,unique=True,null=False)
    def __str__(self):
        return self.tag
    class Meta:
        verbose_name = "Aaron's Tag"
        verbose_name_plural = "Aaron's Tags"

# Create your models here.
class AaronPage(Page):
    buttonimage = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='.JPG Image'
    )

    animate = StreamField([
        ('animate', DocumentChooserBlock()),
    ], max_num=1, use_json_field=True, blank=True)

    files = StreamField([
        ('audio_file', DocumentChooserBlock()),
    ], use_json_field=True)


    tag = models.ForeignKey(
        AaronsTag,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='aarons_tags',
        verbose_name='Tag')

    content_panels = Page.content_panels + [
        FieldPanel("tag", widget=forms.Select),
        FieldPanel("buttonimage"),
        StreamFieldPanel("animate"),
        StreamFieldPanel("files"),
    ]

    class Meta:
        verbose_name = "Aaron's Page"
        verbose_name_plural = "Aaron's Pages"

    # this is best accomplished on "save" event upon creation (vs. signals)
    # check to see if a non .mp3 is uploaded.
    def save(self, *args, **kwargs):
        print(self.files)
        # do logic here eventually
        super().save(*args, **kwargs) # Call the "real" save() method.

