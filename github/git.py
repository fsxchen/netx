#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
File Name: git.py
Description: 
Created_Time: 2016-11-08 11:35:47
Last modified: 2016-11-23 11时54分03秒
'''

_author = 'arron'
_email = 'fsxchen@gmail.com'

import os
import json
from operator import itemgetter

from github import Github
import networkx as nx
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt

from IPython.display import IFrame
from IPython.core.display import display
from networkx.readwrite import json_graph



# git 配置
username = "fsxchen"
password = raw_input("please input password:")
g_user = Github(username, password)


def get_data(username):
    filename = "{username}.gpickle".format(username=username)
    if os.path.exists(filename):
        g = nx.read_gpickle(filename)
    else:
        g = nx.DiGraph()
        user = g_user.get_user(username)
        g.add_node(user.login + '(user)', type='user')
        followers = user.get_followers()
        following = user.get_following()

        for fols in followers:
            g.add_node(fols.login + '(user)', type='user')
            g.add_edge(fols.login + '(user)', user.login + '(user)', type='follows')
            for f in fols.get_followers():
                g.add_node(f.login + '(user)', type='user')
                g.add_edge(f.login + '(user)', fols.login + '(user)',
                        type='follows')
            for fi in fols.get_following():
                g.add_node(fi.login + '(user)', type='user')
                g.add_edge(fols.login + '(user)', fi.login + '(user)',
                        type='following')

        for follin in following:
            g.add_node(follin.login + '(user)', type='user')
            g.add_edge(user.login + '(user)', follin.login + '(user)',
                    type='following')
            for f in follin.get_followers():
                g.add_node(f.login + '(user)', type='user')
                g.add_edge(f.login + '(user)', follin.login + '(user)',
                        type='follows')
            for fi in follin.get_following():
                g.add_node(fi.login + '(user)', type='user')
                g.add_edge(follin.login + '(user)', fi.login + '(user)',
                        type='following')
        nx.write_gpickle(g, filename)
    return g
  

if __name__ == "__main__":
    g = get_data('Z-0ne')
    print nx.info(g)

    print sorted([n for n in g.degree_iter()], key=itemgetter(1), reverse=True)[:10]
    h = g.copy()

    dc = sorted(nx.degree_centrality(h).items(),
            key=itemgetter(1), reverse=True)
    print "Degree Centrality"
    print dc[:10]
    print "*" * 15

    bc = sorted(nx.betweenness_centrality(h).items(),
            key=itemgetter(1), reverse=True)
    print "Betweenness Centrality"
    print bc[:10]
    print "*" * 15

    cc = sorted(nx.closeness_centrality(h).items(),
            key=itemgetter(1), reverse=True)
    print "Closeness Centrality"


    # d = json_graph.node_link_data(G)
    # son.dump(d, open('graph.json', 'w'))


    # nx.write_graphml(G, "z0ne.graphml")

    # viz_file = 'graph.html'

    # display(IFrame(viz_file, '100%', '600px'))




# with open("grahp.json", 'w') as f:
#     data = json_graph.tree_data(G, root=1)
#     json.dump(data, f, indent=4)
# print dir(user)

