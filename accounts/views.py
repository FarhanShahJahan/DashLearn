from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from accounts.forms import RegistrationForm
#----------------------------------------------Bokeh
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool
from accounts.models import Marks, Courseperformance, Course
from accounts.models import Account as userAcc
import pandas as pd 
import numpy as np 

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
def performView(request):
    fieldname ='cgpa'
    dataBins = 85
    dataRange=[2.0,4.0]
    search_type1 = 'gte'
    search_type2 = 'lte'
    filter1 = fieldname + '__' + search_type1
    filter2 = fieldname + '__' + search_type2
    getMatric = request.user.matric
    getProgram = userAcc.objects.filter(matric__exact=getMatric).values_list('program', flat=True)
    getCourse = Courseperformance.objects.filter(matric__exact=getMatric)
    cgpas = userAcc.objects.filter(program=getProgram[0]).values_list(fieldname, flat=True)
    
    marksM = userAcc.objects.filter(matric__exact=getMatric).values_list(fieldname, flat=True)
    userCgpa = userAcc.objects.filter(**{ filter1: marksM, filter2 : marksM }).values_list(fieldname, flat=True)
    arr_hist, edges = np.histogram(cgpas, 
                               bins = dataBins,
                               range=dataRange)
    delays = pd.DataFrame({'arr_delay': arr_hist, 
                       'left': edges[:-1], 
                       'right': edges[1:]})  
    arr_histM, edgesM = np.histogram(userCgpa , 
                               bins = dataBins,
                               range=dataRange)
    delaysM = pd.DataFrame({'arr_delayM': arr_histM, 
                       'left': edgesM[:-1], 
                       'right': edgesM[1:]})  
                  
    #----pure bokeh------------------------------
    plot = figure(plot_height = 600, plot_width = 600, 
           title = 'Students Cgpa ',
          x_axis_label = 'CGPA', 
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
    return render(request,'performance.html',{'script': script, 'div':div, 'posts': getCourse})



#----------------------------------------------------------------------------
@login_required
def subjectView(request):
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
    marks = Courseperformance.objects.filter(courseid=3).values_list(fieldname, flat=True)
    userMarks = Courseperformance.objects.filter(matric__exact=getMatric,courseid=3).values_list(fieldname, flat=True)
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
           title = 'Histogram for Test 1 Performance',
          x_axis_label = 'CGPA', 
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
    return render(request, 'dashboard.html')

@login_required
def profileView(request):
    return render(request, 'profile.html')

@login_required
def assignmentView(request):
    return render(request, 'assign.html')