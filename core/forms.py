from django.forms import ModelForm
from core.models import Subscriber

class EmailForm(ModelForm):
	class Meta:
		model = Subscriber
		fields = ['email_address']