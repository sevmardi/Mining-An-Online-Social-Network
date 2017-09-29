import networkx as nx
import helpers.DataLoader as data
from scipy.sparse.csc import _cs_matrix
import scipy.sparse as ss
import time
import _pickle as cPickle
import matplotlib.pyplot as plt
import numpy as np


class FileOpener:
    def opener(self, dg, data):

        with open(data, 'r') as file:
            for i in file:
                line = i.rstrip('\n')
                vec = line.split(" ")
                dg.add_edge(vec[0], vec[1])
        return dg


class Assignment1(FileOpener):
    def question2_1(self, medium, large):
        """
        Count number of directed links the given network has
        :param medium:
        :param large:
        :return: object
        """
        dg = nx.DiGraph()
        # med = self.opener(dg, medium)
        lag = self.opener(dg, large)

        return {
            # "medium": nx.number_of_edges(med),
            "large": nx.number_of_edges(lag)
        }

    def question2_2(self, medium, large):
        """
        Count number of nodes does the given network has
        :param medium:
        :param large:
        :return: object
        """
        dg = nx.DiGraph()
        med = self.opener(dg, medium)
        # lag = self.opener(dg, large)
        return {
            "medium": nx.number_of_nodes(med),
            # "large": nx.number_of_nodes(lag)
        }

    def question2_3(self, medium, large):
        """
        Caclulate the indegree and outdegree distribution of the given graph
        :param medium:
        :param large:
        :return: object
        """
        dg = nx.DiGraph()
        # med = self.opener(dg, medium)
        lg = self.opener(dg, large)
        
        in_degree = lg.in_degree().values()
        out_degree = lg.out_degree().values()
        o = list(out_degree)

        plt.hist(o)
        plt.title("In Degree Distribution Medium Network")
        plt.xlabel("In degrees")
        plt.ylabel("frequency")
        plt.show()
        
        # xvalues = []
        #
        # for i in range(len(in_degree)):
        #         xvalues += [i]
        # x = np.array(xvalues)
        # y = np.array(out_degree)
        #
        # options = {}
        # options["x"] = x
        # options["xlabel"] = 'In degrees'
        # options["y"] = y
        # options["ylabel"] = 'frequency'
        # options["title"] = 'In Degree Distribution Medium Network'
        # options["filename"] = 'diagrams/Medium_In_Degree_Distribution.png'
        #
        # fig = plt.figure()
        # axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)
        # axes.plot(options['x'], options['y'], 'r')
        # axes.set_xlabel(options['xlabel'])
        # axes.set_ylabel(options['ylabel'])
        # axes.set_title(options['title'])
       
    def question2_4(self, medium, large):
        """
        Calcaulte the nodes and edges of the strongly connected components
        :param medium:
        :param large:
        :return:
        """
        dg = nx.DiGraph()
        med = self.opener(dg, medium)
        # lg = self.opener(dg, large)

        return {
            "medium": nx.number_strongly_connected_components(med),
            # "large": nx.number_strongly_connected_components(lg),

            # both work
            # "medium_weakly": nx.number_weakly_connected_components(med),
            # "large_weakly": nx.number_weakly_connected_components(lg),

            # both work
            # "How many nodes are in the largest strongly connected component? ": nx.number_of_nodes(max(nx.strongly_connected_component_subgraphs(med), key=len)),
            # "How many nodes are in the largest strongly connected component? ": nx.number_of_nodes(max(nx.strongly_connected_component_subgraphs(lg), key=len)),

            #both work
            # "How many edges are in the largest strongly connected component?": nx.number_of_edges(max(nx.strongly_connected_component_subgraphs(med), key=len)),
            # "How many edges are in the largest strongly connected component?": str(nx.number_of_edges(max(nx.strongly_connected_component_subgraphs(lg), key=len)))
        }

    def question2_5(self, medium, large):
        """
         Calculate the distance distribution of largest weakly connected components
        :param medium:
        :param large:
        :return:
        """
        dg = nx.DiGraph()
        med = self.opener(dg, medium)
        # large = self.opener(dg, large)

        weakly_connected_in_medium = sorted(nx.weakly_connected_component_subgraphs(med), key=len, reverse=True )
        lar = weakly_connected_in_medium[0]
        
        values = []
        
        for i in lar:
            # values +=
            values.append(list(nx.single_source_shortest_path_length(dg, i).values()))

        x = np.unique(np.asarray(values))
        plt.hist(values)
        plt.show()
            
    












       


    









if __name__ == '__main__':
    p = Assignment1()
    data = data.DataLoader()

    medi = data.load_medium()
    lage = data.load_large()

    o = p.question2_5(medi, lage)
    # print(o)
    # print(o["large"])
