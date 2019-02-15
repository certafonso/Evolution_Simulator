import random

class Being:
    def __init__(self,food_comsumption,food_production,food_initial):
        self.food_comsumption = food_comsumption
        self.food_production = food_production
        self.food_stored = food_initial
        self.alive = True
        self.Tick = 0

    def pass_tick(self):
        self.food_stored = self.food_stored - self.food_comsumption + self.food_production #for every tick reduces the food comsumed and adds food produced
        if self.food_stored < 0: # checks if being is still alive (has food stored)
            self.alive = False
        self.Tick += 1 #marks 1 more tick

    def pass_life(self):
        while self.alive: #while being is still alive passes a tick
            self.pass_tick()
        return self.Tick #returns lifetime at the end

def create_Sample(size):
    Sample = [[[],[],[]]] #[[[Saves the beings and the lifetime],[saves consumption],[saves production]]]

    for i in range(0,size): #creates beings with random atributes
        comsumption = 0
        production = 1
        while comsumption <= production: #makes consumption less than production so the being won't live forever
            comsumption = random.randint(10,200)
            production = random.randint(10,200)
        Sample[0][0].append(Being(comsumption,production,1000))
        Sample[0][1].append(comsumption)
        Sample[0][2].append(production)
    return Sample

def natural_selection(Sample):
    Sample_sorted = sorted(Sample[-1][0],reverse=True) #sorts the lifetimes from the highest to the lowests
    Survivors = []
    for i in Sample_sorted: #creates a list with the indexs of all the beings sorted
        Survivors.append(Sample[-1][0].index(i))

    for i in range(len(Sample_sorted)-1,-1,-1): #will decide for every being if it will survive or not
        if len(Survivors) > len(Sample_sorted)/2: #makes no more than the half is killed
            rand_number = random.randint(0,100000)/100000 #adds randomness
            if rand_number < i/(len(Sample_sorted)-1): #beings with higher lifetimes will have higher chances of survival
                del Survivors[i]

    while len(Survivors) > len(Sample_sorted)/2: #makes sure that only half of the beings survive
        del Survivors[-1]

    return Survivors

def reproduction(Sample,Parents,mutation_factor):
    Sample.append([[],[],[]])

    for Parent in Parents:
        for child in range(0,2):
            comsumption = 0
            production = 1
            while comsumption <= production: #makes consumption less than production so the being won't live forever
                comsumption = Sample[-2][1][Parent] + random.randint(-mutation_factor,mutation_factor) #mutates the attributes by a mutation factor
                production = Sample[-2][2][Parent] + random.randint(-mutation_factor,mutation_factor)
            Sample[-1][0].append(Being(comsumption,production,1000))
            Sample[-1][1].append(comsumption)
            Sample[-1][2].append(production)
    return Sample

def pass_generation(Sample):
    if len(Sample) > 1: #applies natural selection and reproduction
        Sample = reproduction(Sample,natural_selection(Sample),mutation_factor)
    for i in range(0,len(Sample[-1][0])): #makes all the beings pass a life
        Sample[-1][0][i] = Sample[-1][0][i].pass_life()
    return Sample

def main():
    Sample = create_Sample(10)
    n_generations = 1
    for Generation in range(0,n_generations):
        pass_generation(Sample)

if __name__ == "__main__":
    # main()
    print(pass_generation(create_Sample(10)))
