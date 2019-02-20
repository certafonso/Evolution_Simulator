import numpy
import matplotlib.pyplot as plt

def calc_Average(Sample,Averages): #takes one generation per run
    if Averages == []:
    	Averages = [[],[],[]] #saves Averages, maximum and minimum

    Averages[0].append(sum(Sample)/len(Sample)) #calculates Average
    Averages[1].append(max(Sample)) #calculates maximum
    Averages[2].append(min(Sample)) #calculates minimum
    return Averages

def Show_graph(Averages):
    x_max = len(Averages[0])-1
    generations = list(range(0,x_max+1))
    y_max = max(Averages[1])+2
    plt.plot(generations, Averages[0],"r-",generations, Averages[1],"k-",generations, Averages[2],"k-")
    plt.axis([0,x_max,0,y_max])
    plt.show()


if __name__ == "__main__":
    Sample = [15, 24, 27, 19, 15, 7, 6, 91, 15, 7]
    print(Show_graph([[1,2,3],[4,5,6],[7,8,9],[10,12,13],[14,15,16],[17,18,19],[20,21,22],[23,24,25],[26,27,28],[29,30,31],[32,33,34]]))
