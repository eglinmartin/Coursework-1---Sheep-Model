# ------------------------------- INITIAL SETUP -------------------------------


#IMPORT MODULES
import matplotlib, matplotlib.pyplot, matplotlib.animation
import tkinter, agentframework, csv
matplotlib.use('TkAgg')



#CREATE AGENT LIST
wolves = agentframework.WolfAgent()
sheep = agentframework.SheepAgent()
farmers = agentframework.FarmerAgent()
sheep, wolf, farmer = [], [], []



#DEFINE CONSTANTS
num_of_sheep, num_of_wolves, num_of_farmers = 10, 3, 1
neighbourhood, riflerange = 5, 20
num_of_iterations = 10
carry_on = True



#IMPORT TERRAIN

#Open 'in.txt'
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

#Create 'environment' list to store the data in
environment = []
for row in reader:
    
    #Create 'rowlist' sublist to store row data in
    rowlist = []
    environment.append(rowlist)
    for value in row:
        rowlist.append(value)
        
#Close 'in.txt'
f.close()



#CREATE CHART PARAMETERS
fig = matplotlib.pyplot.figure(figsize=(3, 3))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(False)



# ----------------------------- RUNNING THE MODEL -----------------------------

#RESET PARAMETERS BEFORE MODEL RUNS
def resetparameters():
    
    #Giving the classes their information
    for i in range(num_of_sheep):
        sheep.append(agentframework.SheepAgent(environment, sheep))
    for i in range(num_of_wolves):
        wolf.append(agentframework.WolfAgent(wolf, sheep))
    for i in range(num_of_farmers):
        farmer.append(agentframework.FarmerAgent(farmer, wolf, sheep))

    #Reset the position of each agent
    for i in range(num_of_sheep):
        sheep[i].reset() 
    for i in range(num_of_wolves):
        wolf[i].reset() 
    for i in range(num_of_farmers):
        farmer[i].reset()



#lOOP THE ANIMATION AND ENACT MODEL PROCESSES
def update(num_of_iterations):
    
    fig.clear()
    global carry_on
    
    #Create results list
    result_sheepalive, result_sheeppen, result_sheepdead = \
    num_of_sheep, 0, 0
    
    #Moving the sheep / making them eat
    for i in range(num_of_sheep):
        
        #Check if sheep is dead - if not, enact processes
        if sheep[i].dead == 0:
            sheep[i].move(neighbourhood)
            sheep[i].eat()
            sheep[i].share_with_neighbours(neighbourhood)
        
        #If sheep is dead, update the relevant results accordingly
        else:
            result_sheepalive -= 1
            result_sheepdead += 1

    #Enact actions - wolves
    for i in range(num_of_wolves):
        
        #Check if wolf is dead - if not, enact processes
        if wolf[i].dead == 0:
            wolf[i].move()
            wolf[i].eat(neighbourhood)

    #Enact actions - farmers
    for i in range(num_of_farmers):
        farmer[i].move()
        farmer[i].kill(riflerange)

    #Plot the chart  
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.xlim(0, 100)

    #Plotting four fence lines using their corner coordinates
    matplotlib.pyplot.plot([30, 30], [70, 30], color='brown', \
    linestyle='-', linewidth=2)
    matplotlib.pyplot.plot([30, 70], [30, 30], color='brown', \
    linestyle='-', linewidth=2)
    matplotlib.pyplot.plot([70, 30], [70, 70], color='brown', \
    linestyle='-', linewidth=2)
    matplotlib.pyplot.plot([70, 70], [30, 70], color='brown', \
    linestyle='-', linewidth=2)
 
    #Plotting the farmers on the map
    for i in range(num_of_farmers):
        matplotlib.pyplot.scatter(farmer[i]._x, farmer[i]._y, color = 'blue') 

    #Plotting the wolves
    for i in range(num_of_wolves):
        
        #if alive, plot a grey circle
        if wolf[i].dead == 0:
            matplotlib.pyplot.scatter(wolf[i]._x, wolf[i]._y, color = 'grey')
            
        #if dead, plot a red cross
        else:
            matplotlib.pyplot.scatter(wolf[i]._x, wolf[i]._y, marker = 'x',\
            color = 'red')
 
    #Plotting the sheep
    for i in range(num_of_sheep):
        
        #Check if sheep are dead; if so, draw a black 'x'
        if sheep[i].dead == 1:
            matplotlib.pyplot.scatter(sheep[i]._x, sheep[i]._y, marker = 'x',\
            color = 'black')
            
        else:
            #Check if the sheep are in the pen; if so, draw pink circle
            if sheep[i].penned == 1:
                result_sheeppen += 1
                matplotlib.pyplot.scatter(sheep[i]._x, sheep[i]._y,\
                color = 'pink')
                
            #If alive but not in pen, plot a white circle
            else:
                matplotlib.pyplot.scatter(sheep[i]._x, sheep[i]._y,\
                color = 'white')

    #Draw the map     
    matplotlib.pyplot.imshow(environment, vmin=0, vmax=255, cmap = 'Greens')

    #Export results
    with open('out.txt', mode='w') as out:
        
        #Create / overwrite 'out.txt'
        writer = csv.writer(out, delimiter=',', quotechar='"',\
        quoting=csv.QUOTE_MINIMAL)
        
        #Write the model parameters to the file
        writer.writerow(['*MODEL PARAMETERS*'])  
        writer.writerow(['Number of sheep = ' + format(num_of_sheep)])
        writer.writerow(['Number of wolves = ' + format(num_of_wolves)])
        writer.writerow(['Number of farmers = ' + format(num_of_farmers)])
        
        #Write the sheep statuses to the file
        writer.writerow(['*MODEL RESULTS*'])
        writer.writerow(['Number of sheep alive = '+ \
        format(result_sheepalive)])    
        writer.writerow(['Number of sheep in pen = '+ \
        format(result_sheeppen)]) 
        writer.writerow(['Number of sheep eaten = ' + \
        format(result_sheepdead)])

    

#GENERATE THE ANIMATION
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 10) & (carry_on) :
        # Returns control and waits next call.
        yield a			
        a = a + 1



# -------------------------------- UI COMMANDS --------------------------------

#RUN THE ANIMATION
def run():
    
    #Reset the model's parameters
    resetparameters()
    
    #Initialise and draw the animation
    update(num_of_iterations)
    animation = matplotlib.animation.FuncAnimation(fig, update,\
    repeat=False, frames=num_of_iterations)
    canvas.draw()



#CHANGE THE NUMBER OF SHEEP
def change_sheep():
    
    #Import sheep number
    global num_of_sheep
    
    #Request console input for new number and set it
    num_of_sheep = int(input("Number of sheep (default = 10) :"))



#CHANGE THE NUMBER OF WOLVES
def change_wolves():
    
    #Import wolf number
    global num_of_wolves
    
    #Request console input for new number and set it
    num_of_wolves = int(input("Number of wolves (default = 3) :"))
    
    
    
#CHANGE THE NUMBER OF FARMERS
def change_farmers():
    
    #Import farmer number
    global num_of_farmers
    
    #Request console input for new number and set it
    num_of_farmers = int(input("Number of farmers (default = 1) :"))
    
   
    
#CHANGE THE ANIMATION'S LENGTH IN FRAMES
def change_length():
    
    #Import animation length
    global num_of_iterations
    
#Request console input for new number and set it  
    num_of_iterations = int(input\
    ("Length of animation (default = 100 frames) :"))



# -------------------------------- CREATING UI --------------------------------

#Use tkinter to create window
root = tkinter.Tk()
root.wm_title("Sheep Model")

#Draw menu bar
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
model_parameters = tkinter.Menu(menu_bar)

#Create the 'menu' option
menu_bar.add_cascade(label="Menu", menu=model_menu)

#Create the 'run model with current parameters' sub-option
model_menu.add_command(label="Run model with current parameters", command=run)
model_menu.entryconfig("Run model with current parameters", state = "normal")

#Create the 'parameters' option
menu_bar.add_cascade(label="Edit Parameters", menu=model_parameters)

#Create the sub-options for changing each parameter
model_parameters.add_command(label="Number of sheep", command=change_sheep)
model_parameters.add_command(label="Number of wolves", command=change_wolves)
model_parameters.add_command(label="Number of farmers", command=change_farmers)
model_parameters.add_command(label="Animation length", command=change_length)

#Create the canvas for the map to be drawn upon
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#Stop the program
tkinter.mainloop()