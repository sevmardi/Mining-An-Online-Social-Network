import networkx as nx
import helpers.DataLoader as dataLoader


class Question2_1:
    def main(self):

        # Load the data
        data = dataLoader.DataLoader()
        medium = data.load_medium()
        large = data.load_large()

        # Send it to the opener
        med = self.opener(medium)
        lg = self.opener(large)

        # Print the results
        print("Q2.1 How many Directed edges does this network have?")
        print("Medium Network: " + str(nx.number_of_edges(med)))
        print("Large Network: " + str(nx.number_of_edges(lg)))

    def opener(self, data):
        dg = nx.DiGraph()

        with open(data, 'r') as file:
            for i in file:
                line = i.rstrip('\n')
                vec = line.split(" ")
                dg.add_edge(vec[0], vec[1])
        return dg


if __name__ == '__main__':
    p = Question2_1()
    p.main()






