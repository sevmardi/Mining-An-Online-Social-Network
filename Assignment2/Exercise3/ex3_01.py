from ttp import ttp
from datetime import datetime, time
import networkx as nx
import sys
import csv


# https://stackoverflow.com/questions/7626643/python-tweet-parsing

data = 'data/twitter-small.in'
# Example how to user twitter text parser
# p = ttp.Parser()
# result = p.parse("@burnettedmond, you now support #IvoWertzel's tweet parser! https://github.com/edburnett/")
# print(result.reply)


def create_adjacency_list(file):
    p = ttp.Parser()
    adj_list = {}
    tweet_counter = 0
    with open(file, 'r') as tweets:
        for line in tweets:
            tweet = line.rstrip('\n')
            tweet = line.split("\t")
            tweet_counter += 1
            timestamp = int(datetime.strptime(
                tweet[0], "%Y-%m-%d %H:%M:%S").strftime("%s"))
            usrs = p.parse(tweet[2], html=False).users

            username = tweet[1]

            if len(usrs) > 0:
                if username not in adj_list:
                    adj_list[username] = {}
                for i in usrs:
                    if i not in adj_list[username]:
                        adj_list[username][i] = {}
                        adj_list[username][i]['timestamps'] = [timestamp]
                    else:
                        adj_list[username][i]['timestamps'] += [timestamp]
                adj_list[username][i]['timestamps'].sort()
                adj_list[username][i]['first_mention'] = adj_list[
                    username][i]['timestamps'][0]
                adj_list[username][i]['number_of_mentions'] = adj_list[
                    username][i]['timestamps'][0]

    return adj_list
    # print(adj_list)


def output_adj_list(adjust_list, file):

    edge_list = []

    for user in adjust_list:
        for mention_user in adjust_list[user]:
            weight = adjust_list[user][mention_user]['number_of_mentions']
            timestamp = adjust_list[user][mention_user]['first_mention']
            edge_list += [(user, mention_user, weight, timestamp)]

    with open(file) as edge_list_file:
        csv_out = csv.writer(edge_list)
        csv_out.writerow(['Source', 'Target', 'Weight', 'Timestamp'])
        for row in edge_list:
            csv_out.writerow(row)


if __name__ == '__main__':
    small = create_adjacency_list(data)
    output_adj_list(small, data)
