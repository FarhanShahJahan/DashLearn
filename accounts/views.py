from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from accounts.forms import RegistrationForm , profileForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from datetime import *
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool
from accounts.models import Marks, Courseperformance, Course, Assignment
from accounts.models import Account as userAcc
import pandas as pd 
import numpy as np 
from bokeh.core.properties import value
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource
# Create your views here.
context ={}

def indexView(request):
    return render(request, 'index.html')

# Histogram Function
def histo(field, subject, matric,rangee):
    getValue = subject
    fieldname =field
    histRange= rangee
    dataBins = 50
    search_type1 = 'gte'
    search_type2 = 'lte'
    filter1 = fieldname + '__' + search_type1
    filter2 = fieldname + '__' + search_type2
    getMatric = matric

    marks = Courseperformance.objects.filter(cousecode=getValue).values_list(fieldname, flat=True)
    userMarks = Courseperformance.objects.filter(matric__exact=getMatric,cousecode=getValue).values_list(fieldname, flat=True)
    marksM = Courseperformance.objects.filter(**{ filter1: userMarks, filter2 : userMarks},cousecode=getValue).values_list(fieldname, flat=True)
    arr_hist, edges = np.histogram(marks , 
                               bins = dataBins,
                               range=histRange)
    delays = pd.DataFrame({'arr_delay': arr_hist, 
                       'left': edges[:-1], 
                       'right': edges[1:]})  
   
    arr_histM, edgesM = np.histogram(marksM , 
                               bins = dataBins,
                               range=histRange)
    delaysM = pd.DataFrame({'arr_delayM': arr_histM, 
                       'left': edgesM[:-1], 
                       'right': edgesM[1:]})  
    return delays,delaysM

#-------------------------------------------------------------------------------------------------
@login_required
@csrf_exempt
def subjectView(request):
    getValue = request.session['nxtPg']
    getMatric = request.user.matric
    getCourse = Courseperformance.objects.filter(matric__exact=getMatric)

    getCourseButton = Courseperformance.objects.filter(matric__exact=getMatric).values_list('cousecode', flat=True)

    for course in getCourseButton:
        buttonInput= request.POST.get(course,False)
        if buttonInput != False:
            response = redirect('/accounts/course/')
            request.session['nxtPg'] =  buttonInput
            return response
             
    #----Overall------------------------------
    delays,delaysM =histo('totalcarrymark',getValue,getMatric,[0,60])
    plot = figure( plot_height = 600, plot_width = 600, 
           title = 'Overall Up-To-Date Performance',
          x_axis_label = 'Total Marks', 
           y_axis_label = 'Number of Students', background_fill_color="#fafafa")

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
    plot.sizing_mode='scale_width'
#--- Prediction Line------------------------------
    test = ['Test1', 'Test 2', 'Amali','Quiz','Final']
    getWeek7 = [str(elem) for elem in list(Courseperformance.objects.filter(matric__exact=getMatric,cousecode=getValue).values_list('week7', flat=True))]
    getWeek14 = [str(g7) for g7 in list(Courseperformance.objects.filter(matric__exact=getMatric,cousecode=getValue).values_list('week14', flat=True))]
    getAmali = [str(gf) for gf in list(Courseperformance.objects.filter(matric__exact=getMatric,cousecode=getValue).values_list('amali', flat=True))]
    getQuiz = [str(gf) for gf in list(Courseperformance.objects.filter(matric__exact=getMatric,cousecode=getValue).values_list('quiz', flat=True))]
    getTotal = [str(gf) for gf in list(Courseperformance.objects.filter(matric__exact=getMatric,cousecode=getValue).values_list('predictedmarks', flat=True))]
    getWeek7 = [float(i) for i in  getWeek7]
    getWeek14 = [float(i) for i in  getWeek14]+getWeek7
    getWeek14 = [sum(getWeek14)]
    getAmali = [float(i) for i in  getAmali] + getWeek14
    getAmali = [sum(getAmali)]
    getQuiz = [float(i) for i in  getQuiz]+ getAmali
    getQuiz =[sum(getQuiz)]
    getTotal = [float(i) for i in  getTotal]
    realData = (getWeek7,getWeek14,getAmali,getQuiz)
    predictData = (getWeek7,getWeek14,getAmali,getQuiz,getTotal)
    print(realData)


    predictGraph = figure(plot_height = 300,plot_width= 400, title='Carry Marks(Cumulative) and Predictions',x_range=test,y_range=(0,100), x_axis_label='Tests',
                  y_axis_label='Marks')
    
    predictGraph.line(test, predictData, line_width=2, line_color='#f5a142', line_dash=[8,7],legend='Predicted')
    predictGraph.line(test, realData, line_width=2, line_color='blue', legend='Your Achievement')
    predictGraph.toolbar.autohide = True
    predictGraph.legend.location = "top_left"
    predictGraph.sizing_mode='scale_width'
#---------------------Histo Test 1---------------------------------------------------------------
    histT1,histT11 =histo('week7',getValue,getMatric,[0,20])

    plotTest1 = figure( plot_height = 300, plot_width = 400, 
           title = 'Performance of the class for Test 1',x_axis_label = 'Total Marks', 
           y_axis_label = 'Number of Students', background_fill_color="#fafafa")

    plotTest1.quad(bottom=histT1['arr_delay'], top=0, 
       left=histT1['left'], right=histT1['right'],
       fill_color="navy", line_color="white", alpha=0.5)

    plotTest1.quad(bottom=histT11['arr_delayM'], top=0, 
       left=histT11['left'], right=histT11['right'],
       fill_color="red", line_color="white", alpha=0.5)
    plotTest1.y_range.start = 0
    plotTest1.legend.location = "center_right"
    plotTest1.legend.background_fill_color = "#fefefe"
    plotTest1.toolbar.autohide = True
    plotTest1.grid.grid_line_color="white"
    plotTest1.sizing_mode='scale_width'
#---------------------Histo Test 2---------------------------------------------------------------
    histT2,histT21 =histo('week14',getValue,getMatric,[0,20])

    plotTest2 = figure( plot_height = 300, plot_width = 400, 
           title = 'Performance of the class for Test 2',x_axis_label = 'Total Marks', 
           y_axis_label = 'Number of Students', background_fill_color="#fafafa")

    plotTest2.quad(bottom=histT2['arr_delay'], top=0, 
       left=histT2['left'], right=histT2['right'],
       fill_color="navy", line_color="white", alpha=0.5)

    plotTest2.quad(bottom=histT21['arr_delayM'], top=0, 
       left=histT21['left'], right=histT21['right'],
       fill_color="red", line_color="white", alpha=0.5)
    plotTest2.y_range.start = 0
    plotTest2.legend.location = "center_right"
    plotTest2.legend.background_fill_color = "#fefefe"
    #plotTest2.toolbar.autohide = True
    plotTest2.grid.grid_line_color="white"
    plotTest2.sizing_mode='scale_width'
#---------------------Histo Amali---------------------------------------------------------------
    histT2,histT21 =histo('amali',getValue,getMatric,[0,10])

    plotAmali = figure( plot_height = 300, plot_width = 400, 
           title = 'Performance of the class for Amali',x_axis_label = 'Total Marks', 
           y_axis_label = 'Number of Students', background_fill_color="#fafafa")

    plotAmali.quad(bottom=histT2['arr_delay'], top=0, 
       left=histT2['left'], right=histT2['right'],
       fill_color="navy", line_color="white", alpha=0.5)

    plotAmali.quad(bottom=histT21['arr_delayM'], top=0, 
       left=histT21['left'], right=histT21['right'],
       fill_color="red", line_color="white", alpha=0.5)
    plotAmali.y_range.start = 0
    plotAmali.legend.location = "center_right"
    plotAmali.legend.background_fill_color = "#fefefe"
    plotAmali.toolbar.autohide = True
    plotAmali.grid.grid_line_color="white"
    plotAmali.sizing_mode='scale_width'
#---------------------Histo Quiz---------------------------------------------------------------
    histT2,histT21 =histo('quiz',getValue,getMatric,[0,10])

    plotQuiz = figure( plot_height = 300, plot_width = 400, 
           title = 'Performance of the class for Quiz',x_axis_label = 'Total Marks', 
           y_axis_label = 'Number of Students', background_fill_color="#fafafa")

    plotQuiz.quad(bottom=histT2['arr_delay'], top=0, 
       left=histT2['left'], right=histT2['right'],
       fill_color="navy", line_color="white", alpha=0.5)

    plotQuiz.quad(bottom=histT21['arr_delayM'], top=0, 
       left=histT21['left'], right=histT21['right'],
       fill_color="red", line_color="white", alpha=0.5)
    plotQuiz.y_range.start = 0
    plotQuiz.legend.location = "center_right"
    plotQuiz.legend.background_fill_color = "#fefefe"
    plotQuiz.toolbar.autohide = True
    plotQuiz.grid.grid_line_color="white"
    plotQuiz.sizing_mode='scale_width'
#---------------------------------------------------------------------------------
    row2 = row(plotAmali,plotQuiz)
    row1= row(plotTest1,plotTest2)
    column1= column(predictGraph,row1,row2)
    column1.sizing_mode='scale_width'
    graphs = row(plot,column1)
    graphs.sizing_mode='scale_width'
    script, div = components(graphs)
    subName=''
    subName=getValue
    return render(request,'subject.html',{'script': script, 'div':div, 'postsSB': getCourse, 'subName': subName})

#-------------------------------------------------------------------------------------------------
@login_required
def dashboardView(request):
    getMatric = request.user.matric
    getCourseButton = Courseperformance.objects.filter(matric__exact=getMatric).values_list('cousecode', flat=True)
    getDetails = Courseperformance.objects.filter(matric__exact=getMatric)
    getAssign = Assignment.objects.filter(matric__exact=getMatric,status=False)
    for assign in getAssign:
        today = date.today()
        future = assign.duedate
        b= (future - today).days
        if b <=5:
            if b>=0:
                messages.warning(request,((" Due date for %s's assignment is %s days left" % (assign.courseid,b))))
            else:
                messages.error(request,(("You have passed the due date for %s's assignment" % (assign.courseid))))
        else:
            messages.info(request,((" Due date for %s's assignment is %s days left" % (assign.courseid,b))))
            
    for course in getCourseButton:
        buttonInput= request.POST.get(course,False)
        if buttonInput != False:
            response = redirect('/accounts/course/')
            request.session['nxtPg'] =  buttonInput
            return response

   


    
    fieldname ='cgpa'
    search_type1 = 'gte'
    search_type2 = 'lte'
    filter1 = fieldname + '__' + search_type1
    filter2 = fieldname + '__' + search_type2
    getWeek7 = [str(elem) for elem in list(Courseperformance.objects.filter(matric__exact=getMatric).values_list('week7', flat=True))]
    getWeek14 = [str(g7) for g7 in list(Courseperformance.objects.filter(matric__exact=getMatric).values_list('week14', flat=True))]
    getAmali = [str(gf) for gf in list(Courseperformance.objects.filter(matric__exact=getMatric).values_list('amali', flat=True))]
    getWeekFinal = [str(gf) for gf in list(Courseperformance.objects.filter(matric__exact=getMatric).values_list('quiz', flat=True))]
    getProgram = userAcc.objects.filter(matric__exact=getMatric).values_list('program', flat=True)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
    getCourse= Courseperformance.objects.filter(matric__exact=getMatric)
    getXaxis= [str(elem) for elem in list(Courseperformance.objects.filter(matric__exact=getMatric).values_list('cousecode', flat=True))]
    getWeekFinal = [float(i) for i in  getWeekFinal]
    getWeek7 = [float(i) for i in  getWeek7]
    getWeek14 = [float(i) for i in  getWeek14]
    getAmali = [float(i) for i in  getAmali]             
    #----pure bokeh------------------------------
    fruits = getXaxis
    years = ["Test 1", "Test 2", "Amali","Quiz"]
    colors = ["#472358", "#6b3484", "#8f46b0", "#b358dd"]

    data = {'fruits' : fruits,
            'Test 1'   : getWeek7,
            'Test 2'   : getWeek14,
            'Amali'   : getAmali,
            'Quiz'   : getWeekFinal}

    p = figure(x_range=fruits,  y_axis_label='Marks', x_axis_label='Courses',plot_height=500, title="Total Carry Marks",
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


 
    p.sizing_mode='scale_width'
    script, div = components(p)
    return render(request, 'dashboard.html',{'script': script, 'div':div, 'postsSB': getCourse})
#-------------------------------------------------------------------------------------------------
@login_required
def profileView(request):
    getMatric = request.user.matric
    getDetails = Courseperformance.objects.filter(matric__exact=getMatric)
    return render(request, 'profile.html',{'posts': getDetails})
#-------------------------------------------------------------------------------------------------
@login_required  
def editprofileView(request):
    getMatric = request.user.matric
    getCourse= Courseperformance.objects.filter(matric__exact=getMatric)
    getCourseButton = Courseperformance.objects.filter(matric__exact=getMatric).values_list('cousecode', flat=True)
    
    for course in getCourseButton:
        buttonInput= request.POST.get(course,False)
        if buttonInput != False:
            response = redirect('/accounts/course/')
            request.session['nxtPg'] =  buttonInput
            return response
             
    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST, user= request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'editProfile.html', args,{'postsSB': getCourse})
#-------------------------------------------------------------------------------------------------
@login_required
def assignmentView(request):
    getMatric = request.user.matric
    getCourse= Courseperformance.objects.filter(matric__exact=getMatric)
    getDetails = Courseperformance.objects.filter(matric__exact=getMatric)
    getAssignment = Assignment.objects.filter(matric__exact=getMatric,status=True)
    getCourseButton = Courseperformance.objects.filter(matric__exact=getMatric).values_list('cousecode', flat=True)
    
    for course in getCourseButton:
        buttonInput= request.POST.get(course,False)
        if buttonInput != False:
            response = redirect('/accounts/course/')
            request.session['nxtPg'] =  buttonInput
            return response
             
    return render(request, 'assign.html',{'posts1': getAssignment,'posts': getDetails,'postsSB': getCourse})

#-------------------------------------------------------------------------------------------------