from django.shortcuts import render , get_object_or_404 ,redirect
from django.contrib import auth , messages
from .models import Degree,Course,Document,PlanningExam,User,Planning
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.db import transaction


# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')

def clubs(request):
    return render(request, 'core/clubs.html')

def index_eng(request):
    
    degrees = Degree.objects.all()
    courses = Course.objects.all()
    return render(request, 'core/eng/index.html' ,{'degrees': degrees ,'courses': courses })



from django.contrib import auth, messages
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # Redirect to the next parameter if it exists, or to the home page
            redirect_to = request.GET.get('next', '/')
            if not redirect_to:
                redirect_to = '/'
            return redirect(redirect_to)
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'core/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def licence(request):
    return render(request, 'core/master.html')


def coursedetails(request, pk):
    course = get_object_or_404(Course, description=pk)
    documents = Document.objects.all().order_by('documenttype')
    return render(request, 'core/course-details.html', {'course': course , 'documents': documents})

def planningexams(request):
    planningexams = PlanningExam.objects.all()

    
    return render(request, 'core/planningexams.html' ,{'planningexams': planningexams})


def planning(request):
    plannings = Planning.objects.all()

    
    return render(request, 'core/planning.html' ,{'plannings': plannings})



@login_required
def submit_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            document.save()
            messages.info(request, 'Document Uploaded Successfully')
            return redirect('submit_document')
    else:
        form = DocumentForm(user=request.user)

    context = {'form': form}
    return render(request, 'core/submit.html', context)



@login_required
def profpanel(request):
    user = request.user
    documents = Document.objects.filter(user=user)
    return render(request, 'core/profpanel.html', {'user': user, 'documents': documents})



@login_required
@transaction.atomic

def delete_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    
    # Check if user is authorized to delete the document
    if document.user != request.user:
        raise PermissionDenied("You are not authorized to delete this document.")

    if request.method == 'POST':
        document.delete()
        return redirect('profpanel')
        
    
    return render(request, 'core/profpanel.html', {'document': document})

@login_required
def edit_document(request, pk):
    document = get_object_or_404(Document, id=pk)

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document, user=request.user)
        if form.is_valid():
            document = form.save()
            messages.info(request, 'Document Updated Successfully')
            return redirect('profpanel')
    else:
        # Check if user is authorized to edit the document
        if document.user != request.user:
            raise PermissionDenied()
        form = DocumentForm(instance=document, user=request.user)

    return render(request, 'core/submit.html', {'form': form})




def error_404(request,exception):
    return render(request, 'core/404.html',status=404)


