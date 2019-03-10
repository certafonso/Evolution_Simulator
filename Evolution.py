import random
import Data_Treatment

class Being:
    def __init__(self,food_comsumption,food_initial):
        self.food_comsumption = food_comsumption
        self.food_stored = food_initial

    def pass_life(self):
        return self.food_stored//self.food_comsumption #returns lifetime at the end

def create_Sample(size,food_initial):
    Sample = [[[],[]]] #[[[Saves the beings and the lifetime],[saves consumption],[saves production]]]
    for i in range(0,size): #creates beings with random atributes
        comsumption = random.randint(100,200)
        Sample[0][0].append(Being(comsumption,food_initial))
        Sample[0][1].append(comsumption)
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

def reproduction(Sample,Parents,mutation_factor,food_initial):
    Sample.append([[],[]])
    for Parent in Parents:
        for child in range(0,2):
            comsumption = 0
            while comsumption <= 0:
                comsumption = Sample[-2][1][Parent] + random.randint(-mutation_factor,mutation_factor) #mutates the attributes by a mutation factor
            Sample[-1][0].append(Being(comsumption,food_initial))
            Sample[-1][1].append(comsumption)
    return Sample

def pass_generation(Sample):
    for i in range(0,len(Sample[-1][0])): #makes all the beings pass a life
        Sample[-1][0][i] = Sample[-1][0][i].pass_life()
    return Sample

def main():
    food_initial = 100000
    mutation_factor = 1
    Sample_size = 100 #Sample size has to be a even number
    Sample = create_Sample(Sample_size,food_initial)
    Averages = []
    while True:
        print("Welcome to the Evolution simulator. What do you want to do?\n\t(0) Exit\n\t(1) See current sample\n\t(2) Pass generations")
        if Averages != []: print("\t(3) See the evolution\n\t(4) Export data")
        option = int(input(""))

        if option == 0:
            break
        elif option == 1:
            for Being in range(0,len(Sample[-1][0])):
                print("Being nº",Being+1,"Comsumption ",Sample[-1][1][Being])
            while True:
                print("What do you want to do now?\n\t(1) Create new sample\n\t(2) Change sample size\n\t(3) Nothing")
                option = int(input(""))

                if option == 1 or option == 2:
                    while True:
                        if option == 2: Sample_size = int(input("What is the new size? (has to be a even number)"))
                        if Sample_size % 2 == 0:
                            break
                    Sample = create_Sample(Sample_size,food_initial)
                    Averages = []
                    break
                elif option == 3:
                    break

        elif option == 2:
            n_generations = int(input("How many generations do you want to pass?"))
            for Generation in range(0,n_generations):
                if type(Sample[-1][0][0]) is int: #applies natural selection and reproduction
                    Sample = reproduction(Sample,natural_selection(Sample),mutation_factor,food_initial)
                pass_generation(Sample)
                Averages = Data_Treatment.calc_Average(Sample[-1][0],Averages)
                print("Generation",len(Sample),"of",len(Sample)+n_generations-Generation-1,"passed")

        elif option == 3:
            Data_Treatment.Show_graph(Averages)

        elif option == 4:
            while True:
                file_name = input("File name:") + ".csv"
                print("The file will be called:",file_name)
                if input("Y/N: ") in ["Y","y"]:
                    break
            Data_Treatment.Export_Data(Sample,file_name)

if __name__ == "__main__":
    main()
