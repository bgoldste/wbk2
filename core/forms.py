from django.forms import ModelForm
from core.models import Subscriber, Spot

class EmailForm(ModelForm):
	class Meta:
		model = Subscriber
		fields = ['email_address']


class SpotForm(ModelForm):
	class Meta:
		model = Spot
		fields = ['name', 'url']