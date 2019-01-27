from joins.models import Join
from django.utils.deprecation import MiddlewareMixin

class ReferMiddleware(MiddlewareMixin):

	def process_request(self,request):
		ref_id=request.GET.get('ref')
		try:
			obj=Join.objects.get(ref_id=ref_id)
		except:
			obj=None

		if obj:
			print("id is "+str(obj.id))
			request.session['join_id_ref']=obj.id