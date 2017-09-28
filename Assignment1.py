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
        med = self.opener(dg, medium)
        # lg = self.opener(dg, large)
        in_degree = med.in_degree().values()
        out_degree = med.out_degree().values()

        plt.hist(list(in_degree))
        plt.show()

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
            # "medium": nx.number_strongly_connected_components(med),
            # "large": nx.number_strongly_connected_components(lg),

            # "medium_weakly": nx.number_weakly_connected_components(med),
            # "large_weakly": nx.number_weakly_connected_components(lg),

            # "How many nodes are in the largest strongly connected component? ": nx.number_of_nodes(max(nx.strongly_connected_component_subgraphs(med), key=len)),
            # "How many nodes are in the largest strongly connected component? ": nx.number_of_nodes(max(nx.strongly_connected_component_subgraphs(lg), key=len)),

            "How many edges are in the largest strongly connected component?": nx.number_of_edges(max(nx.strongly_connected_component_subgraphs(med), key=len)),
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

        s = nx.single_source_shortest_path_length(dg, 0)
        print(s)
        # plt.hist(list(s))
        # plt.show()


    def question2_6(self, medium, large):
        return None






if __name__ == '__main__':
    p = Assignment1()
    data = data.DataLoader()

    medi = data.load_medium()
    lage = data.load_large()

    o = p.question2_2(medi, lage)
    print(o)
    # print(o["large"])
