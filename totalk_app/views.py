from django.template import RequestContext, loader, Context
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from totalk_app.models import Profile, Invitation
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
def index(request):
	return render(request, 'index.html') 

# Create Profile Funtion:
@login_required
def create_profile(request):
	if request.method == "POST" and request.FILES.items():

		image = request.FILES['image']
		city = request.POST.get('city')
		Bio = request.POST.get('Bio')
		ocupation = request.POST.get('ocupation')
		linkedin = request.POST.get('linkedin')
		insta = request.POST.get('insta')

		profile, created = Profile.objects.get_or_create(
			user=request.user,
			image= image,
			city= city,
			Bio=Bio,
			ocupation=ocupation,
			linkedin=linkedin,
			insta=insta,
			)
		return HttpResponseRedirect('/totalk/going_out')
	else:
		return render(request, 'create_profile.html')
@login_required
def invitation(request):
	
	if request.method=="POST":

		raising_request_for = request.POST.get('raising_request_for')
		location = request.POST.get('location')
		dateandtime = request.POST.get('dateandtime')
		going_out_for = request.POST.get('going_out_for')

		profile, created = Invitation.objects.get_or_create(
			profile = request.user.profile_set.get(),
			raising_request_for=raising_request_for,
			location=location,
			dateandtime=dateandtime,
			going_out_for=going_out_for,

			)

		return HttpResponseRedirect('/totalk/going_out')
	else:
		profile = Profile.objects.get(user=request.user)
		return render(request, 'invitation.html', {'profile':profile})

@login_required
def going_out_requests(request):
	profile=Profile.objects.get(user=request.user)
	invitation = Invitation.objects.all().order_by('-pub_date')
	query = request.GET.get('q')
	if query:
		invitation = invitation.filter(location__icontains=query) | invitation.filter(going_out_for__icontains=query) 
	paginator = Paginator(invitation, 18)

	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)

	return render(request, 'going_out_requests.html', {'invitation':invitation, 'contacts':contacts, 'profile':profile})

def inv_detail(request, id):
	invitation = Invitation.objects.get(id=id)
	is_interested=False
	if invitation.interested.filter(id=request.user.id).exists():
		invitation.interested.remove(request.user)
		is_interested=False
	else:
		invitation.interested.add(request.user)
		is_interested=True
	return render(request, 'inv_detail.html', {'inv':invitation, 'is_interested':is_interested})

def interested(request):
	invitation = get_object_or_404(Invitation, id=request.POST.get('id'))
	is_interested= False
	if invitation.interested.filter(id=request.user.id).exists():
		invitation.interested.remove(request.user)
		is_interested= False
	else:
		invitation.interested.add(request.user)
		is_interested=True
	return HttpResponseRedirect('/totalk/going_out/')

@login_required
def profile(request):
	profile=Profile.objects.get(user=request.user)
	inv=profile.invitation_set.all()
	return render(request, 'profile.html', {'profile':profile, 'inv':inv})