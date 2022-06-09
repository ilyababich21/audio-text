from .models import Audio
from django.forms import ModelForm


class AudioForm(ModelForm):

    class Meta:
        # Название модели на основе
        # которой создается форма
        model = Audio
        # Включаем все поля с модели в форму
        fields = ['title','audio']