from django.db import models

# Create your models here.

class Join(models.Model):
	email=models.EmailField()
	friend=models.ForeignKey("self",related_name='referral',null=True,blank=True,on_delete=models.CASCADE)
	ref_id=models.CharField(max_length=120,default='abc',unique=True)
	ip_address=models.CharField(max_length=120,default='127.0.0.1')
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__(self):
		return self.email

	class Meta:
		unique_together=['email','ref_id',]