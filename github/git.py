#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
File Name: git.py
Description: 
Created_Time: 2016-11-08 11:35:47
Last modified: 2016-11-09 16时43分25秒
'''

_author = 'arron'
_email = 'fsxchen@gmail.com'

import json

from github import Github
import networkx as nx
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt

from IPython.display import IFrame
from IPython.core.display import display
from networkx.readwrite import json_graph


G = nx.DiGraph()


username = "fsxchen"
password = raw_input("please input password:")
g = Github(username, password)

user = g.get_user("Z-0ne")

G.add_node(user.login + '(user)', type='user')

followers = user.get_followers()


following = user.get_following()

for fols in followers:
    G.add_node(fols.login + '(user)', type='user')
    G.add_edge(fols.login + '(user)', user.login + '(user)', type='gazes')
    for f in fols.get_followers():
        G.add_node(f.login + '(user)', type='user')
        G.add_edge(f.login + '(user)', fols.login + '(user)', type='gazes')
    for fi in fols.get_following():
        pass

for follin in following:
    G.add_node(follin.login + '(user)', type='user')
    G.add_edge(user.login + '(user)', follin.login + '(user)', type='gazes')
    for f in follin.get_followers():
        G.add_node(f.login + '(user)', type='user')
        G.add_edge(f.login + '(user)', follin.login + '(user)', type='gazes')
    for fi in follin.get_following():
        pass
    

# print nx.info(G)

d = json_graph.node_link_data(G)
json.dump(d, open('graph.json', 'w'))

viz_file = 'graph.html'

display(IFrame(viz_file, '100%', '600px'))




# with open("grahp.json", 'w') as f:
#     data = json_graph.tree_data(G, root=1)
#     json.dump(data, f, indent=4)
# print dir(user)

