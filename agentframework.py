#Import modules
import random


#Creating the sheep class
class SheepAgent():
    
    #Initiating the class    
    def __init__ (self, environment = None, sheep = 0, y = 0, x = 0):
        
        #Transferring model variables
        self.environment = environment
        self.sheep = sheep
        
        #Creating local variables / setting starting values
        self.store, self.dead, self.penned, self.reproduced = 0, 0, 0, 0
        self._x, self._y = random.randint(0,100), random.randint(0,100)
        
        

    #Moving the class
    def move(self, neighbourhood):
        
        #Check to see if the sheep is inside the pen; if so, restrict movement to pen limits
        if self.penned == 1:
            
            #Create a 50/50 chance for horizontal direction
            if random.random() < 0.5:
                if self._x < 68:
                    self._x += 1
            else:
                if self._x > 32:
                    self._x -= 1

            #Create a 50/50 chance for vertical direction        
            if random.random() < 0.5:
                if self._y < 68:
                    self._y = (self._y + 1)
            else:
                if self._y > 32:
                    self._y = (self._y - 1)
                    
        #Check to see if the sheep is inside the pen; if so, restrict movement to map limits
        else:
            
            #Create a 50/50 chance for horizontal direction            
            if random.random() < 0.5:
                if self._x < 100:
                    self._x += 1
            else:
                if self._x > 0:
                    self._x -= 1

            #Create a 50/50 chance for vertical direction        
            if random.random() < 0.5:
                if self._y < 100:
                    self._y = (self._y + 1)
            else:
                if self._y > 0:
                    self._y = (self._y - 1)       
                    
        #If sheep is inside pen limits, restrict their movement to the pen        
        if self._x >= 32 and self._x <= 68 and self._y >= 32 and self._y <= 68:
            self.penned = 1
        
    
    
    #Making the sheep eat
    def eat(self):
        
        #Check if environment value is greater than / equal to 10 - if so, eat 10
        if self.environment[self._y][self._x] >= 20:
            self.environment[self._y][self._x] -= 20
            self.store += 20
            
        #Check if environment value is less than 10 - if so, eat that amount
        if self.environment[self._y][self._x] < 20:
            self.store += self.environment[self._y][self._x]
            self.environment[self._y][self._x] = 0
            
        #Check if the store is greater than or equal to 100 - if so, vomit up half of it
        if self.store >= 100:
            self.store = 0
            self.environment[self._y][self._x] += 50
            
    
    
    #Resetting positions and variables on model reset
    def reset(self):
        self.store, self.dead, self.penned, self.reproduced = 0, 0, 0, 0
        self._x, self._y = random.randint(0,100), random.randint(0,100)  



    #Share food with neighbouring sheep
    def share_with_neighbours(self, neighbourhood):

        #Check distance to others
        for sheep in self.sheep:
            dist = self.distance_between(sheep)
            if dist <= neighbourhood:
                
                #Calculate half of sheep's food
                sum = self.store + sheep.store
                ave = sum /2
                
                #Split store between both sheep
                self.store = ave
                sheep.store = ave



    #Calculate distances between every sheep                
    def distance_between(self, sheep):
        return (((self._x - sheep._x)**2) + ((self._y - sheep._y)**2))**0.5
         
       

#Creating the sheep class    
class WolfAgent():

    #Initiating the class     
    def __init__ (self, wolf = 0, sheep = 0):
        
        #Transferring model variables
        self.sheep = sheep
        
        #Creating local variables   
        self.dead = 0
        
        #Setting starting values        
        self._x = random.randint(0,100)
        self._y = random.randint(0,100)        



    #Moving the class
    def move(self):
        
        #Set a random movement distance each time
        self.movex = random.random() * 5
        self.movey = random.random() * 5
        
        #Create a 50/50 chance for horizontal direction
        if random.random() < 0.5:
            
            #If there is a clear space, move the allocated movement distance
            if self._x < (100 - self.movex):
                self._x = (self._x + self.movex)
        else:
            
            #If there is a clear space, move the allocated movement distance
            if self._x > (0 + self.movex):
                self._x = (self._x - self.movex)
                
        #Create a 50/50 chance for vertical direction
        if random.random() < 0.5:

            #If there is a clear space, move the allocated movement distance
            if self._y < (100 - self.movey):
                self._y = (self._y + self.movey)
        else:
            
            #If there is a clear space, move the allocated movement distance
            if self._y > (0 + self.movey):
                self._y = (self._y - self.movey)
    
    
    
    #Making the wolf eat
    def eat(self, neighbourhood):
        for sheep in self.sheep:
            dist = self.distance_between(sheep)
            if dist <= neighbourhood:
                sheep.dead = 1
                
                
                
    #Resetting positions and variables on model reset
    def reset(self):
        self.dead = 0
        self._x, self._y = random.randint(0,100), random.randint(0,100)



    #Calculate distances between self and every sheep
    def distance_between(self, sheep):
        return (((self._x - sheep._x)**2) + ((self._y - sheep._y)**2))**0.5
    
  
#Creating the farmer class
class FarmerAgent():
    
    #Initiating the class
    def __init__ (self, farmer = 0, wolf = 0, sheep = 0):
        
        #Transferring model variables
        self.sheep, self.wolf = sheep, wolf

        #Creating local variables / setting starting values
        self._x, self._y = random.randint(30,70), random.randint(30,70)
        self.movex, self.movey = 0, 0



    #Moving the farmer
    def move(self):
        
        #Set a random movement distance each time        
        self.movex = random.random() * 2
        self.movey = random.random() * 2

        #Create a 50/50 chance for horizontal direction        
        if random.random() < 0.5:
            
            #If there is a clear space, move the allocated movement distance
            if self._x < (66 - self.movex):
                self._x = (self._x + self.movex)
        else:
            
            #If there is a clear space, move the allocated movement distance
            if self._x > (33 + self.movex):
                self._x = (self._x - self.movex)
                
        #Create a 50/50 chance for vertical direction        
        if random.random() < 0.5:
            
            #If there is a clear space, move the allocated movement distance
            if self._y < (66 - self.movey):
                self._y = (self._y + self.movey)
        else:
            
            #If there is a clear space, move the allocated movement distance
            if self._y > (33 + self.movey):
                self._y = (self._y - self.movey)



    #Killing wolves    
    def kill(self, riflerange):
        
        #Check if a wolf is within range of his rifle, and kill that wolf if so
        for wolf in self.wolf:
            dist = self.distance_between(wolf)
            if dist <= riflerange:
                wolf.dead = 1



    #Resetting positions and variables on model reset
    def reset(self):
        
        self._x, self._y = random.randint(30,70), random.randint(30,70)
        
        
        
    #Calculate distances between self and every wolf
    def distance_between(self, wolf):
        
        return (((self._x - wolf._x)**2) + ((self._y - wolf._y)**2))**0.5