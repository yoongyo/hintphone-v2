from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from accounts.models import Profile

class Theme(models.Model):
    roomEscape = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='themes')
    enterKey = models.CharField(max_length=50)
    hintCount = models.PositiveIntegerField(default=3)
    name = models.CharField(max_length=30)

    currentCount = models.PositiveIntegerField(default=0, blank=True, null=True)
    currentHint = models.TextField(default='', blank=True, null=True)

    manyHint = models.BooleanField(default=False)
    timer = models.PositiveIntegerField(default=60, blank=True, null=True)

    hint1 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint1 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint1 = RichTextUploadingField(blank=True, null=True,
                                       external_plugin_resources=[(
                                         'youtube',
                                         'https://hintphone.s3.amazonaws.com//static/base/vendor/ckeditor_plugins/youtube/youtube/',
                                         'plugin.js',
                                     )])
    sub_textHint1 = RichTextUploadingField(blank=True, null=True)

    hint2 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint2 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint2 = RichTextUploadingField(blank=True, null=True)
    sub_textHint2 = RichTextUploadingField(blank=True, null=True)

    hint3 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint3 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint3 = RichTextUploadingField(blank=True, null=True)
    sub_textHint3 = RichTextUploadingField(blank=True, null=True)

    hint4 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint4 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint4 = RichTextUploadingField(blank=True, null=True)
    sub_textHint4 = RichTextUploadingField(blank=True, null=True)

    hint5 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint5 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint5 = RichTextUploadingField(blank=True, null=True)
    sub_textHint5 = RichTextUploadingField(blank=True, null=True)

    hint6 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint6 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint6 = RichTextUploadingField(blank=True, null=True)
    sub_textHint6 = RichTextUploadingField(blank=True, null=True)

    hint7 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint7 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint7 = RichTextUploadingField(blank=True, null=True)
    sub_textHint7 = RichTextUploadingField(blank=True, null=True)

    hint8 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint8 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint8 = RichTextUploadingField(blank=True, null=True)
    sub_textHint8 = RichTextUploadingField(blank=True, null=True)

    hint9 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint9 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint9 = RichTextUploadingField(blank=True, null=True)
    sub_textHint9 = RichTextUploadingField(blank=True, null=True)

    hint10 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint10 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint10 = RichTextUploadingField(blank=True, null=True)
    sub_textHint10 = RichTextUploadingField(blank=True, null=True)

    hint11 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint11 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint11 = RichTextUploadingField(blank=True, null=True)
    sub_textHint11 = RichTextUploadingField(blank=True, null=True)

    hint12 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint12 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint12 = RichTextUploadingField(blank=True, null=True)
    sub_textHint12 = RichTextUploadingField(blank=True, null=True)

    hint13 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint13 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint13 = RichTextUploadingField(blank=True, null=True)
    sub_textHint13 = RichTextUploadingField(blank=True, null=True)

    hint14 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint14 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint14 = RichTextUploadingField(blank=True, null=True)
    sub_textHint14 = RichTextUploadingField(blank=True, null=True)

    hint15 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint15 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint15 = RichTextUploadingField(blank=True, null=True)
    sub_textHint15 = RichTextUploadingField(blank=True, null=True)

    hint16 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint16 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint16 = RichTextUploadingField(blank=True, null=True)
    sub_textHint16 = RichTextUploadingField(blank=True, null=True)

    hint17 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint17 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint17 = RichTextUploadingField(blank=True, null=True)
    sub_textHint17 = RichTextUploadingField(blank=True, null=True)

    hint18 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint18 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint18 = RichTextUploadingField(blank=True, null=True)
    sub_textHint18 = RichTextUploadingField(blank=True, null=True)

    hint19 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint19 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint19 = RichTextUploadingField(blank=True, null=True)
    sub_textHint19 = RichTextUploadingField(blank=True, null=True)

    hint20 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint20 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint20 = RichTextUploadingField(blank=True, null=True)
    sub_textHint20 = RichTextUploadingField(blank=True, null=True)

    hint21 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint21 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint21 = RichTextUploadingField(blank=True, null=True)
    sub_textHint21 = RichTextUploadingField(blank=True, null=True)

    hint22 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint22 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint22 = RichTextUploadingField(blank=True, null=True)
    sub_textHint22 = RichTextUploadingField(blank=True, null=True)

    hint23 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint23 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint23 = RichTextUploadingField(blank=True, null=True)
    sub_textHint23 = RichTextUploadingField(blank=True, null=True)

    hint24 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint24 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint24 = RichTextUploadingField(blank=True, null=True)
    sub_textHint24 = RichTextUploadingField(blank=True, null=True)

    hint25 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint25 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint25 = RichTextUploadingField(blank=True, null=True)
    sub_textHint25 = RichTextUploadingField(blank=True, null=True)

    hint26 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint26 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint26 = RichTextUploadingField(blank=True, null=True)
    sub_textHint26 = RichTextUploadingField(blank=True, null=True)

    hint27 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint27 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint27 = RichTextUploadingField(blank=True, null=True)
    sub_textHint27 = RichTextUploadingField(blank=True, null=True)

    hint28 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint28 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint28 = RichTextUploadingField(blank=True, null=True)
    sub_textHint28 = RichTextUploadingField(blank=True, null=True)

    hint29 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint29 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint29 = RichTextUploadingField(blank=True, null=True)
    sub_textHint29 = RichTextUploadingField(blank=True, null=True)

    hint30 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint30 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint30 = RichTextUploadingField(blank=True, null=True)
    sub_textHint30 = RichTextUploadingField(blank=True, null=True)

    hint31 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint31 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint31 = RichTextUploadingField(blank=True, null=True)
    sub_textHint31 = RichTextUploadingField(blank=True, null=True)

    hint32 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint32 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint32 = RichTextUploadingField(blank=True, null=True)
    sub_textHint32 = RichTextUploadingField(blank=True, null=True)

    hint33 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint33 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint33 = RichTextUploadingField(blank=True, null=True)
    sub_textHint33 = RichTextUploadingField(blank=True, null=True)

    hint34 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint34 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint34 = RichTextUploadingField(blank=True, null=True)
    sub_textHint34 = RichTextUploadingField(blank=True, null=True)

    hint35 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint35 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint35 = RichTextUploadingField(blank=True, null=True)
    sub_textHint35 = RichTextUploadingField(blank=True, null=True)

    hint36 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint36 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint36 = RichTextUploadingField(blank=True, null=True)
    sub_textHint36 = RichTextUploadingField(blank=True, null=True)

    hint37 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint37 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint37 = RichTextUploadingField(blank=True, null=True)
    sub_textHint37 = RichTextUploadingField(blank=True, null=True)

    hint38 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint38 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint38 = RichTextUploadingField(blank=True, null=True)
    sub_textHint38 = RichTextUploadingField(blank=True, null=True)

    hint39 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint39 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint39 = RichTextUploadingField(blank=True, null=True)
    sub_textHint39 = RichTextUploadingField(blank=True, null=True)

    hint40 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint40 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint40 = RichTextUploadingField(blank=True, null=True)
    sub_textHint40 = RichTextUploadingField(blank=True, null=True)

    hint51 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint51 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint51 = RichTextUploadingField(blank=True, null=True)
    sub_textHint51 = RichTextUploadingField(blank=True, null=True)

    hint52 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint52 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint52 = RichTextUploadingField(blank=True, null=True)
    sub_textHint52 = RichTextUploadingField(blank=True, null=True)

    hint53 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint53 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint53 = RichTextUploadingField(blank=True, null=True)
    sub_textHint53 = RichTextUploadingField(blank=True, null=True)

    hint54 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint54 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint54 = RichTextUploadingField(blank=True, null=True)
    sub_textHint54 = RichTextUploadingField(blank=True, null=True)

    hint55 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint55 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint55 = RichTextUploadingField(blank=True, null=True)
    sub_textHint55 = RichTextUploadingField(blank=True, null=True)

    hint56 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint56 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint56 = RichTextUploadingField(blank=True, null=True)
    sub_textHint56 = RichTextUploadingField(blank=True, null=True)

    hint57 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint57 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint57 = RichTextUploadingField(blank=True, null=True)
    sub_textHint57 = RichTextUploadingField(blank=True, null=True)

    hint58 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint58 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint58 = RichTextUploadingField(blank=True, null=True)
    sub_textHint58 = RichTextUploadingField(blank=True, null=True)

    hint59 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint59 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint59 = RichTextUploadingField(blank=True, null=True)
    sub_textHint59 = RichTextUploadingField(blank=True, null=True)

    hint60 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint60 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint60 = RichTextUploadingField(blank=True, null=True)
    sub_textHint60 = RichTextUploadingField(blank=True, null=True)

    hint41 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint41 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint41 = RichTextUploadingField(blank=True, null=True)
    sub_textHint41 = RichTextUploadingField(blank=True, null=True)

    hint42 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint42 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint42 = RichTextUploadingField(blank=True, null=True)
    sub_textHint42 = RichTextUploadingField(blank=True, null=True)

    hint43 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint43 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint43 = RichTextUploadingField(blank=True, null=True)
    sub_textHint43 = RichTextUploadingField(blank=True, null=True)

    hint44 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint44 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint44 = RichTextUploadingField(blank=True, null=True)
    sub_textHint44 = RichTextUploadingField(blank=True, null=True)

    hint45 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint45 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint45 = RichTextUploadingField(blank=True, null=True)
    sub_textHint45 = RichTextUploadingField(blank=True, null=True)

    hint46 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint46 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint46 = RichTextUploadingField(blank=True, null=True)
    sub_textHint46 = RichTextUploadingField(blank=True, null=True)

    hint47 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint47 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint47 = RichTextUploadingField(blank=True, null=True)
    sub_textHint47 = RichTextUploadingField(blank=True, null=True)

    hint48 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint48 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint48 = RichTextUploadingField(blank=True, null=True)
    sub_textHint48 = RichTextUploadingField(blank=True, null=True)

    hint49 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint49 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint49 = RichTextUploadingField(blank=True, null=True)
    sub_textHint49 = RichTextUploadingField(blank=True, null=True)

    hint50 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint50 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint50 = RichTextUploadingField(blank=True, null=True)
    sub_textHint50 = RichTextUploadingField(blank=True, null=True)

    hint61 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint61 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint61 = RichTextUploadingField(blank=True, null=True)
    sub_textHint61 = RichTextUploadingField(blank=True, null=True)

    hint62 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint62 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint62 = RichTextUploadingField(blank=True, null=True)
    sub_textHint62 = RichTextUploadingField(blank=True, null=True)

    hint63 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint63 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint63 = RichTextUploadingField(blank=True, null=True)
    sub_textHint63 = RichTextUploadingField(blank=True, null=True)

    hint64 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint64 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint64 = RichTextUploadingField(blank=True, null=True)
    sub_textHint64 = RichTextUploadingField(blank=True, null=True)

    hint65 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint65 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint65 = RichTextUploadingField(blank=True, null=True)
    sub_textHint65 = RichTextUploadingField(blank=True, null=True)

    hint66 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint66 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint66 = RichTextUploadingField(blank=True, null=True)
    sub_textHint66 = RichTextUploadingField(blank=True, null=True)

    hint67 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint67 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint67 = RichTextUploadingField(blank=True, null=True)
    sub_textHint67 = RichTextUploadingField(blank=True, null=True)

    hint68 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint68 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint68 = RichTextUploadingField(blank=True, null=True)
    sub_textHint68 = RichTextUploadingField(blank=True, null=True)

    hint69 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint69 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint69 = RichTextUploadingField(blank=True, null=True)
    sub_textHint69 = RichTextUploadingField(blank=True, null=True)

    hint70 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint70 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint70 = RichTextUploadingField(blank=True, null=True)
    sub_textHint70 = RichTextUploadingField(blank=True, null=True)

    hint71 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint71 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint71 = RichTextUploadingField(blank=True, null=True)
    sub_textHint71 = RichTextUploadingField(blank=True, null=True)

    hint72 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint72 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint72 = RichTextUploadingField(blank=True, null=True)
    sub_textHint72 = RichTextUploadingField(blank=True, null=True)

    hint73 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint73 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint73 = RichTextUploadingField(blank=True, null=True)
    sub_textHint73 = RichTextUploadingField(blank=True, null=True)

    hint74 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint74 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint74 = RichTextUploadingField(blank=True, null=True)
    sub_textHint74 = RichTextUploadingField(blank=True, null=True)

    hint75 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint75 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint75 = RichTextUploadingField(blank=True, null=True)
    sub_textHint75 = RichTextUploadingField(blank=True, null=True)

    hint76 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint76 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint76 = RichTextUploadingField(blank=True, null=True)
    sub_textHint76 = RichTextUploadingField(blank=True, null=True)

    hint77 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint77 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint77 = RichTextUploadingField(blank=True, null=True)
    sub_textHint77 = RichTextUploadingField(blank=True, null=True)

    hint78 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint78 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint78 = RichTextUploadingField(blank=True, null=True)
    sub_textHint78 = RichTextUploadingField(blank=True, null=True)

    hint79 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint79 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint79 = RichTextUploadingField(blank=True, null=True)
    sub_textHint79 = RichTextUploadingField(blank=True, null=True)

    hint80 = models.FileField(upload_to='mp3/', blank=True, null=True)
    sub_hint80 = models.FileField(upload_to='mp3/', blank=True, null=True)
    textHint80 = RichTextUploadingField(blank=True, null=True)
    sub_textHint80 = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.name