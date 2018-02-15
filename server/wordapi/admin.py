from django.contrib import admin
from .models import Word, Question, Answer
from .models import Q_and_W_rel, A_and_W_rel, Q_A_and_W_rel
from .models import Q_quality, A_quality, Q_and_A_compatibility

admin.site.register(Word)
admin.site.register(Question)
admin.site.register(Q_and_W_rel)