import networkx as nx
import helpers.DataLoader as data
from scipy.sparse.csc import _cs_matrix


class FileOpener:
    def opener(self, dg, data):
        with open(data, 'r') as file:
            for i in file:
                line = i.rstrip('\n')
                vec = line.split(" ")
                dg.add_edge(vec[0], vec[1])
        return dg


class Assignment1(FileOpener):
    def question_1(self, medium, large):
        dg = nx.DiGraph()
        med = self.opener(dg, medium)
        lag = self.opener(dg, large)

        return {
            "medium": nx.number_of_edges(med),
            "large" : nx.number_of_edges(lag)
        }

    def question_2(self, data):
        return None

    def question_3(self, data):
        return None

    def question_4(self, data):

        return None


if __name__ == '__main__':
    p = Assignment1()
    data = data.DataLoader()

    medi = data.load_medium()
    lage = data.load_large()
    o = p.question_1(medi, lage)
    print(o['large'])
