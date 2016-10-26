from github import Github
import networkx as nx
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


print nx.info(G)

with open("grahp.json", 'w') as f:
    json.dump(data, f, indent=4)
# print dir(user)

