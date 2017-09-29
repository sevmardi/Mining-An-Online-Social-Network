import networkx as nx
import numpy as np
import helpers.DataLoader as dataLoader


class FileOpener:
    def opener(self, dg, data):
        with open(data, 'r') as file:
            for i in file:
                line = i.rstrip('\n')
                vec = line.split(" ")
                dg.add_edge(vec[0], vec[1])
        return dg


class Question2_1(FileOpener):

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


if __name__ == '__main__':
    p = Question2_1()
    data = dataLoader.DataLoader()

