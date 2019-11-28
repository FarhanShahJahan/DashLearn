from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from accounts.forms import RegistrationForm , profileForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from datetime import *
#----------------------------------------------Bokeh
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool
from accounts.models import Marks, Courseperformance, Course, Assignment
from accounts.models import Account as userAcc
import pandas as pd 
import numpy as np 
from bokeh.core.properties import value
#------------------------------------------------------
# Create your views here.
context ={}
def registerView(request):
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'registration/register.html', context)

def indexView(request):
    return render(request, 'index.html')
#-------------------bokeh------------------------------
@login_required
@csrf_exempt
def performView(request):
    fieldname ='cgpa'
    search_type1 = 'gte'
    search_type2 = 'lte'
    filter1 = fieldname + '__' + search_type1
    filter2 = fieldname + '__' + search_type2
    getMatric = request.user.matric
    getWeek7 = [str(elem) for elem in list(Courseperformance.objects.filter(matric__exact=getMatric).values_list('week7', flat=True))]
    getWeek14 = [str(g7) for g7 in list(Courseperformance.objects.filter(matric__exact=getMatric).values_list('week14', flat=True))]
    getAmali = [str(gf) for gf in list(Courseperformance.objects.filter(matric__exact=getMatric).values_list('amali', flat=True))]
    getWeekFinal = [str(gf) for gf in list(Courseperformance.objects.filter(matric__exact=getMatric).values_list('quiz', flat=True))]
    getProgram = userAcc.objects.filter(matric__exact=getMatric).values_list('program', flat=True)
    getCourse= Courseperformance.objects.filter(matric__exact=getMatric)
    getXaxis= [str(elem) for elem in list(Courseperformance.objects.filter(matric__exact=getMatric).values_list('cousecode', flat=True))]

    getCourseButton = Courseperformance.objects.filter(matric__exact=getMatric).values_list('cousecode', flat=True)
    getWeekFinal = [float(i) for i in  getWeekFinal]
    getWeek7 = [float(i) for i in  getWeek7]
    getWeek14 = [float(i) for i in  getWeek14]
    getAmali = [float(i) for i in  getAmali]             
    #----pure bokeh------------------------------
    fruits = getXaxis
    years = ["First 7 Week", "Week 7-14", "Amali","Quiz"]
    colors = ["#c9d9d3", "#718dbf", "#e84d60", "#56bacf"]

    data = {'fruits' : fruits,
            'First 7 Week'   : getWeek7,
            'Week 7-14'   : getWeek14,
            'Amali'   : getAmali,
            'Quiz'   : getWeekFinal}

    p = figure(x_range=fruits, plot_height=500, title="Overall",
            toolbar_location=None, tools="hover", tooltips="$name @fruits: @$name")

    p.vbar_stack(years, x='fruits', width=0.5, color=colors, source=data,
                legend=[value(x) for x in years])

    p.y_range.start = 0
    p.y_range.end = 100
    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.axis.minor_tick_line_color = None
    p.outline_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"


    for course in getCourseButton:
        buttonInput= request.POST.get(course,False)
        if buttonInput != False:
            response = redirect('/accounts/course/')
            request.session['nxtPg'] =  buttonInput
            return response
    
   
    #------------------------------------------
    script, div = components(p)
    return render(request,'performance.html',{'script': script, 'div':div, 'posts': getCourse})



#----------------------------------------------------------------------------
@login_required
def subjectView(request):
    getValue = request.session['nxtPg']
    fieldname ='total'
    dataBins = 50
    search_type1 = 'gte'
    search_type2 = 'lte'
    filter1 = fieldname + '__' + search_type1
    filter2 = fieldname + '__' + search_type2
    getMatric = request.user.matric
#---------------------------------------------------------
    getCourse = Courseperformance.objects.filter(matric__exact=getMatric)
#---------------------------------------------------------
    marks = Courseperformance.objects.filter(cousecode=getValue).values_list(fieldname, flat=True)
    userMarks = Courseperformance.objects.filter(matric__exact=getMatric,cousecode=getValue).values_list(fieldname, flat=True)
    marksM = Courseperformance.objects.filter(**{ filter1: userMarks, filter2 : userMarks }).values_list(fieldname, flat=True)
    arr_hist, edges = np.histogram(marks , 
                               bins = dataBins,
                               range=[0,100])
    delays = pd.DataFrame({'arr_delay': arr_hist, 
                       'left': edges[:-1], 
                       'right': edges[1:]})  
    arr_histM, edgesM = np.histogram(marksM , 
                               bins = dataBins,
                               range=[0,100])
    delaysM = pd.DataFrame({'arr_delayM': arr_histM, 
                       'left': edgesM[:-1], 
                       'right': edgesM[1:]})  
                  
    #----pure bokeh------------------------------
    plot = figure(plot_height = 600, plot_width = 600, 
           title = 'Performance of the class',
          x_axis_label = 'Total Marks', 
           y_axis_label = 'Students', background_fill_color="#fafafa")

    plot.quad(bottom=delays['arr_delay'], top=0, 
       left=delays['left'], right=delays['right'],
       fill_color="navy", line_color="white", alpha=0.5)

    plot.quad(bottom=delaysM['arr_delayM'], top=0, 
       left=delaysM['left'], right=delaysM['right'],
       fill_color="red", line_color="white", alpha=0.5)
    plot.y_range.start = 0
    plot.legend.location = "center_right"
    plot.legend.background_fill_color = "#fefefe"
    plot.toolbar.autohide = True
    plot.grid.grid_line_color="white"
    


    #------------------------------------------
    script, div = components(plot)
    return render(request,'subject.html',{'script': script, 'div':div, 'posts': getCourse})


@login_required
def dashboardView(request):
    getMatric = request.user.matric
    getAssign = Assignment.objects.filter(matric__exact=getMatric,status=False)
    for assign in getAssign:
        today = date.today()
        future = assign.duedate
        b= (future - today).days
        if b <=5:
                messages.warning(request,((" Due date for %s's assignment is near" % (assign.courseid))))

    return render(request, 'dashboard.html')

@login_required
def profileView(request):
    getMatric = request.user.matric
    getDetails = Courseperformance.objects.filter(matric__exact=getMatric)
    return render(request, 'profile.html',{'posts': getDetails})

@login_required  
def editprofileView(request):
    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST, user= request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'editProfile.html', args)

@login_required
def assignmentView(request):
    getMatric = request.user.matric
    getAssignment = Assignment.objects.filter(matric__exact=getMatric)
    return render(request, 'assign.html',{'posts': getAssignment})

