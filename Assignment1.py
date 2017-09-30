import networkx as nx
import helpers.DataLoader as data
from scipy.sparse.csc import _cs_matrix
import scipy.sparse as ss
import matplotlib.pyplot as plt
import numpy as np
from graph_tool.all import *
import _pickle as cPickle


class FileOpener:
    def opener(self, dg, data):
        with open(data, 'r') as file:
            for i in file:
                line = i.rstrip('\n')
                vec = line.split(" ")
                dg.add_edge(vec[0], vec[1])
        return dg


class Assignment1(FileOpener):


    def question2_5(self, medium, large):
        """
         Calculate the distance distribution of largest weakly connected components
        :param medium:
        :param large:
        :return:
        """
        dg = Graph()
        med = self.opener(dg, medium)
        # lg = self.opener(dg, large)

        l = graph_tool.topology.label_largest_component(lg)
        u = graph_tool.topology.GraphView(lg, vfilt=l)
        print(u.num_vertices())

        dist = graph_tool.stats.distance_histogram(u)
        self.dump(dist[0], 'pickles/Large_Distance_Histogram.pickle')

        MediumFn = "pickles/Large_Distance_Histogram.pickle"
        MediumHistogram = cPickle.load(open(MediumFn, 'rb'))
        x = range(len(MediumHistogram))
        y = MediumHistogram
        fig = plt.figure()
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        axes.bar(x, y, align='center', width=0.5)
        axes.set_xlabel('Distances')
        axes.set_ylabel('Count')
        axes.set_title('Distance Distribution Large Network');
        fig.savefig("diagrams/Large_Distance_Distribution.png")





        # dg = nx.DiGraph()
        # med = self.opener(dg, medium)
        #
        # weakly_connected_in_medium = max(nx.weakly_connected_component_subgraphs(med), key=len)
        # # lar = weakly_connected_in_medium[0]
        # values = {}
        #
        # for i in weakly_connected_in_medium.nodes():
        #     d = nx.single_source_shortest_path_length(weakly_connected_in_medium, i)
        #     for key, value in d.items():
        #         if value not in values:
        #             values[value] = 0
        #         values[value] +=1
        #
        # items = sorted(values.items())
        #
        # plt.bar([k for k, v in items], [v for k,v in items], color='g')
        # plt.show()



        # values.append(list(nx.single_source_shortest_path_length(dg, i).values()))
        # x = np.unique(np.asarray(values))
        # plt.hist(values)
        # plt.show()

    def dump(self, picle, file_name):
        cPickle.dump(picle, open(file_name, 'wb'))





if __name__ == '__main__':
    p = Assignment1()
    data = data.DataLoader()

    medi = data.load_medium()
    lage = data.load_large()

    o = p.question2_2(medi, lage)
    print(o)
    # print(o["large"])
