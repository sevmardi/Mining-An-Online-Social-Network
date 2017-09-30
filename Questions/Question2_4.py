import networkx as nx
import helpers.DataLoader as dataLoader


class Question2_3:

    def main(self):

        # Load the data
        data = dataLoader.DataLoader()
        medium = data.load_medium()
        large = data.load_large()

        # Send it to the opener
        med = self.opener(medium)
        lg = self.opener(large)

        # Print the results
        print("Q2.4 How many weakly connected components and how many strongly connected components does this network have? How many nodes and links are in the largest strongly connected component of this graph?\n")

        print("Number of weakly connected components Medium: " + str(nx.number_weakly_connected_components(med)))
        print("Number of weakly connected components Large: " + str(nx.number_weakly_connected_components(lg)))
        print("\n")
        print("Number of strongly connected components Medium: " +  str(nx.number_strongly_connected_components(med)))
        print("Number of strongly connected components Large: " + str(nx.number_strongly_connected_components(lg)))
        print("\n")
        print("How many nodes are in the largest strongly connected component?")
        print("Medium Network: " + str(nx.number_of_nodes(max(nx.strongly_connected_component_subgraphs(med), key=len))))
        print("Large Network: " + str(nx.number_of_nodes(max(nx.strongly_connected_component_subgraphs(lg), key=len))))
        print("\n")
        print("How many edges are in the largest strongly connected component?")
        print("Medium Network: " + str(nx.number_of_edges(max(nx.strongly_connected_component_subgraphs(med), key=len))))
        print("Large Network: " + str(nx.number_of_edges(max(nx.strongly_connected_component_subgraphs(lg), key=len))))

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