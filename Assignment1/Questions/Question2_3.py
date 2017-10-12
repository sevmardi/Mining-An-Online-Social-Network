import networkx as nx
import helpers.DataLoader as dataLoader
import matplotlib.pyplot as plt
import helpers.DataLoader as data


class Question2_3:

    def main(self):
        """
        Caclulate the indegree and outdegree distribution of the given graph
        """
        # Load the data
        data = dataLoader.DataLoader()
        medium = data.load_medium()
        large = data.load_large()

        # Send it to the opener
        med = self.opener(medium)
        lg = self.opener(large)

        # Call the methods
        # You can change the "med" by "lg" to get the indegree and outdegree of the large dataset
        in_degree = med.in_degree().values()
        out_degree = med.out_degree().values()

        # Plot the values
        # Change the below list param by out_degree or in_degree to get right results
        o = list(in_degree)
        plt.hist(o)
        # Need to change to title to either In-degree or Out-degree of chosen dataset
        plt.title("Out Degree Distribution Medium Network")
        plt.xlabel("degrees")
        plt.ylabel("frequency")
        plt.show()

    def opener(self, data):
        dg = nx.DiGraph()

        with open(data, 'r') as file:
            for i in file:
                line = i.rstrip('\n')
                vec = line.split(" ")
                dg.add_edge(vec[0], vec[1])
        return dg


if __name__ == '__main__':
    p = Question2_3()
    p.main()
