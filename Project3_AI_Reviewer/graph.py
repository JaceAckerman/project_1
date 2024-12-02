# Author: Jace Ackerman
# Date: 11/25/24
# File: graph.py
# Description: This file contains the Graph class. This class is specifically designed to output a plot designated
# for this project. It will display the amount of positives, negatives, and neutrals the phi3 model generated
# for each product. This plot will be a grouped bar chart. Imports the matplotlib.pyplot module to plot the data.
import matplotlib.pyplot as plt
import numpy as np

class Graph:
    
    def __init__(self):
        self.products = ['Series 5', 'Series 6', 'Series 7', 'Series 8', 'Series 9']
        self.positives = []  # index 0 refers to the first product, index 1 is the second product, etc.
        self.negatives = []  # index 0 refers to the first product, index 1 is the second product, etc.
        self.neutrals =  []  # index 0 refers to the first product, index 1 is the second product, etc.
        self.barWidth = .25
        self.x = []          #x values (0,1,2,3,etc.)
    
    # Bar chart positions
    def setXValues(self):
        self.x = np.arange(len(self.products))  # Positions for each product

    def setBarWidth(self, width):
        self.barWidth = width

    def plotBars(self):
        plt.bar(self.x - self.barWidth, self.positives, width=self.barWidth, label='Positive', color='green')
        plt.bar(self.x, self.neutrals, width=self.barWidth, label='Neutral', color='yellow')
        plt.bar(self.x + self.barWidth, self.negatives, width=self.barWidth, label='Negative', color='red')

    #labelPlot() handles all the labelling for the graph. This method labels the x and y axis, as well as the
    #the products for the grouped bars. It shows the legend on the graph.
    def labelPlot(self, xLabel, yLabel, title):
        # Adding labels and title
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.title(title)
        plt.xticks(self.x, self.products)  # Set the x-axis labels to the product names
        plt.legend()  # Show the legend
        
    def makePlot(self,xLabel, yLabel, title):
        self.setXValues()
        self.plotBars()
        self.labelPlot(xLabel, yLabel, title)

    # Display the plot
    def displayPlot(self):
        plt.tight_layout()  # Adjust spacing to prevent overlap
        plt.show()
        