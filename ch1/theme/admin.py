from django.contrib import admin
from .models import Theme
from django import forms
from ckeditor.widgets import CKEditorWidget


class ThemeAdmin(admin.ModelAdmin):
    textHint1 = forms.CharField(widget=CKEditorWidget)

    class Meta:
        model = Theme

    list_display = ['name', 'enterKey', 'hintCount', 'currentCount']

admin.site.register(Theme, ThemeAdmin)

