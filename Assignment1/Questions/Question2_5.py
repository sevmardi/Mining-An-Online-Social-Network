import networkx as nx
import helpers.DataLoader as dataLoader
import _pickle as pic
from graph_tool.all import *
import matplotlib.pyplot as plt


class Question2_5:
    def main(self):
        """
         Calculate the distance distribution of largest weakly connected components
        """
        # Load the data
        data = dataLoader.DataLoader()
        medium = data.load_medium()
        large = data.load_large()

        # Send it to the opener
        med = self.opener(medium)
        lg = self.opener(large)

        # using the graph_tool lib call the largest component with given dataset
        # You might need to change the param 'lg' to 'med' to get the results of the proper dataset
        l = graph_tool.topology.label_largest_component(lg)
        u = graph_tool.topology.GraphView(lg, vfilt=l)

        dist = graph_tool.stats.distance_histogram(u)
        self.dump(dist[0], 'pickles/Large_Distance_Histogram.pickle')

        data_pic = "pickles/Large_Distance_Histogram.pickle"
        data_hist = pic.load(open(data_pic, 'rb'))

        x = range(len(data_hist))
        y = data_hist

        # Start plotting
        fig = plt.figure()
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        axes.bar(x, y, align='center', width=0.5)
        axes.set_xlabel('Distances')
        axes.set_ylabel('Count')
        axes.set_title('Distance Distribution Large Network')
        fig.savefig("diagrams/Large_Distance_Distribution.png")

    def opener(self, data):
        dg = nx.DiGraph()

        with open(data, 'r') as file:
            for i in file:
                line = i.rstrip('\n')
                vec = line.split(" ")
                dg.add_edge(vec[0], vec[1])
        return dg

    def dump(self, picle, file_name):
        pic.dump(picle, open(file_name, 'wb'))


if __name__ == '__main__':
    p = Question2_5()
    p.main()
