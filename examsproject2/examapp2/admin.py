from django.contrib import admin
from examapp2.models import TotalScore
from examapp2.models import UserProfileInfo
# Register your models here.
class TotalScoreAdmin(admin.ModelAdmin):
    list_display=['username','sixthquestionanswer','sixthquestionmarks','seventhquestionanswer','seventhquestionmarks','eigthquestionanswer','eigthquestionmarks','ninthquestionanswer','ninthquestionmarks','totalmarks','percentage']
admin.site.register(TotalScore,TotalScoreAdmin)

admin.site.register(UserProfileInfo)
