import numpy
import matplotlib.pyplot as plt
import csv

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

def Export_Data(Sample,file_name):
    with open(file_name,"w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Generation","Lifetime","Consumption"])
        n_Generation = 0
        for Generation in Sample:
            for being in range(0,len(Generation[0])):
                writer.writerow([n_Generation,Generation[0][being],Generation[1][being]])
            n_Generation += 1


if __name__ == "__main__":
    Sample = [15, 24, 27, 19, 15, 7, 6, 91, 15, 7]
    Export_Data([[[6, 28, 8, 26, 14, 41, 23, 26, 26, 6], [170, 36, 141, 40, 72, 25, 45, 39, 40, 196]], [[11, 15, 8, 21, 38, 12, 8, 16, 11, 39], [96, 70, 129, 49, 27, 89, 126, 65, 95, 26]], [[13, 18, 18, 21, 14, 16, 21, 21, 9, 10], [79, 56, 58, 50, 72, 63, 50, 48, 120, 111]], [[20, 18, 53, 14, 112, 8, 32, 91, 5, 39], [52, 58, 19, 76, 9, 141, 32, 11, 202, 26]], [[28, 15, 51, 28, 11, 12, 44, 9, 91, 11], [36, 68, 20, 37, 94, 90, 23, 112, 11, 95]]],"test.csv")
