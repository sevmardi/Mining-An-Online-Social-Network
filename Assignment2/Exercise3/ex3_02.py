import sys
import networkx as nx
import _pickle as pic
import csv
import numpy as np
from graph_tool.all import *

# sys.setdefaultencoding("UTF-8")

data = 'data/twitter-small.in'
csv_file = "csv/twitter-small.csv"


def number_of_edges(graph, title):
    print('Number of Edges')
    print(title + ": " + str(nx.number_of_edges(graph)))
    print('\n')


def number_of_nodes(graph, title):
    print("Number of Nodes in the network")
    print(title + ": " + str(nx.number_of_nodes(graph)))
    print('\n')


def network_density(graph, title):
    print('Network Density')
    print(title + ': ' + str(nx.density(graph)))
    print('\n')


def in_degree_distribution(DiGraph, title, filename):
    in_degrees = DiGraph.in_degree().values()
    bin_count = np.bincount(np.array(in_degrees))
    # dump(bin_count, filename)
    # print("In Degree Distribution " + title + " \n")
    # print(bin_count)
    # print("\n")


def out_degree_distribution(DiGraph, title, filename):
    out_degree = DiGraph.out_degree().values()
    bin_count = np.bincount(np.array(out_degree))
    dump(bin_count, filename)
    print("Out Degree Distribution " + title + " \n")
    print(bin_count)
    print("\n")


def number_of_weakly_connected_components(graph, title):
    print("Number of weakly connected components")
    print(titel + ": " + str(nx.number_weakly_connected_components(graph)))
    print("\n")


def number_of_strongly_connected_components(graph, title):
    print('Number of weakly connected components')
    print(titel + ": " + str(nx.number_strongly_connected_components(graph)))


def get_largest_component(graph, titel, filename):
    number_of_edges(graph, titel)
    number_of_nodes(graph, titel)
    network_density(graph, title)
    in_degree_distribution(graph, title, filename)
    out_degree_distribution(graph, titel, filename)

    # Save the largest file
    nx.write_weighted_edgelist(graph, filename, delimiter=",")

#TODO
def aprox_distance_distribution(filename):
    pass

def parse_file_to_digraph(filename):
    dg = nx.DiGraph()
    with open(filename, 'r') as files:
        for line in files:
            line = line.rstrip('\n')
            v = line.split(",")

            # dg.add_edge(vec[0], vec[1])
            dg.add_edge(v[0],v[1],{'weight':v[2],'timestamp':v[3]});
            # dg.add_edge(t[0], t[1], {'weight': t[2], 'timestamp': t[3]})

    return dg

# TODO
def parse_file_to_gtdigraph(filename):
    """
    """


def dump(picle, filename):
    pic.dump(picle, open(filename, 'wb'))


def main():
    small = parse_file_to_digraph(csv_file)
    # number_of_edges(small, 'Small Network')
    # number_of_edges(small, "Small network") 
    # network_density(small, "network Density")
    in_degree_distribution(small, "Small network", "pickles/Small_In_Degree_Distribution.pickle")


if __name__ == '__main__':
    main()
