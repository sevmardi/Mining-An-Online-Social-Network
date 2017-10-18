import sys
import networkx as nx
import _pickle as pic
import csv
import numpy as np
from graph_tool.all import *

sys.setdefaultencoding("UTF-8")

data = 'data/twitter-small.in'


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
    dump(bin_count, filename)
    print("In Degree Distribution " + title + " \n")
    print(bin_count)
    print("\n")


def out_degree_distribution(DiGraph, title, filename):
    out_degree = DiGraph.out_degree().values()
    bin_count = np.bincount(np.array(out_degree))
    dump(bin_count, filename)
    print("Out Degree Distribution " + title + " \n")
    print(bin_count)
    print("\n")


# TODO
def parse_file_to_digraph(filename):
    pass

# TODO


def parse_file_to_gtdigraph(filename):

    pass


def dump(picle, filename):
    pic.dump(picle, open(filename, 'wb'))


# TODO
def main():
    pass
