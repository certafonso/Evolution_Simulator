import numpy
import matplotlib.pyplot as plt

def calc_Percentile(Sample,Percentiles): #takes one generation per run
    if Percentiles == []:
    	Percentiles = [[],[],[],[],[],[],[],[],[],[],[]] #saves percentiles from 0 to 100

    for i in range(0,11):
        Percentiles[i].append(numpy.percentile(Sample,i*10)) #calculates Percentile
    return Percentiles

def Show_graph(Percentiles):
    x_max = len(Percentiles[0])-1
    generations = list(range(0,x_max+1))
    y_max = max(Percentiles[10])+2
    plt.plot(generations, Percentiles[0],"k-",generations, Percentiles[1],"k-",generations, Percentiles[2],"k-",generations, Percentiles[3],"k-",generations, Percentiles[4],"k-",generations, Percentiles[5],"r-",generations, Percentiles[6],"k-",generations, Percentiles[7],"k-",generations, Percentiles[8],"k-",generations, Percentiles[9],"k-",generations, Percentiles[10],"k-")
    plt.axis([0,x_max,0,y_max])
    plt.show()


if __name__ == "__main__":
    Sample = [15, 24, 27, 19, 15, 7, 6, 91, 15, 7]
    print(Show_graph([[1,2,3],[4,5,6],[7,8,9],[10,12,13],[14,15,16],[17,18,19],[20,21,22],[23,24,25],[26,27,28],[29,30,31],[32,33,34]]))
