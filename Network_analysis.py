
# # Network Connectivity
# 
# In this assignment you will go through the process of importing and analyzing an internal email communication network between employees of a mid-sized manufacturing company. 
# Each node represents an employee and each directed edge between two nodes represents an individual email. The left node represents the sender and the right node represents the recipient.

# In[61]:


import networkx as nx
import pandas as pd

# This line must be commented out when submitting to the autograder
#!head email_network.txt


# ### Question 1
# 
# Using networkx, load up the directed multigraph from `email_network.txt`. Make sure the node names are strings.
# 
# *This function should return a directed multigraph networkx graph.*

# In[62]:


def answer_one():
    from networkx import convert_matrix
    #grphm=nx.convert_matrix.from_pandas_edgelist(grph)
    #multigrph=nx.read_edgelist('email_network.txt',nodetype=str,create_using=nx.MultiDiGraph())
    grph_mltg=nx.read_edgelist('email_network.txt', data=[('Time', int)], 
                         create_using=nx.MultiDiGraph())
    return grph_mltg# Your Answer Here
answer_one()


# ### Question 2
# 
# How many employees and emails are represented in the graph from Question 1?
# 
# *This function should return a tuple (#employees, #emails).*

# In[21]:


def answer_two():
        
    # Your Code Here
    
    return len([i for i in answer_one().nodes()]),len([i for i in answer_one().edges()])# Your Answer Here
answer_two()


# ### Question 3
# 
# * Part 1. Assume that information in this company can only be exchanged through email.
# 
#     When an employee sends an email to another employee, a communication channel has been created, allowing the sender to provide information to the receiver, but not vice versa. 
# 
#     Based on the emails sent in the data, is it possible for information to go from every employee to every other employee?
# 
# 
# * Part 2. Now assume that a communication channel established by an email allows information to be exchanged both ways. 
# 
#     Based on the emails sent in the data, is it possible for information to go from every employee to every other employee?
# 
# 
# *This function should return a tuple of bools (part1, part2).*

# In[22]:


def answer_three():
        
    # Your Code Here
    
    return (nx.is_strongly_connected(answer_one()),True)# Your Answer Here
answer_three()


# ### Question 4
# 
# How many nodes are in the largest (in terms of nodes) weakly connected component?
# 
# *This function should return an int.*

# In[32]:


def answer_four():
    
    return   len(max(nx.weakly_connected_components(answer_one()), key=len)) # Your Answer Here
answer_four()


# ### Question 5
# 
# How many nodes are in the largest (in terms of nodes) strongly connected component?
# 
# *This function should return an int*

# In[37]:


def answer_five():
        
    # Your Code Here
    
    return len(max(nx.strongly_connected_components(answer_one()), key=len))
answer_five()# Your Answer Here


# ### Question 6
# 
# Using the NetworkX function strongly_connected_component_subgraphs, find the subgraph of nodes in a largest strongly connected component. 
# Call this graph G_sc.
# 
# *This function should return a networkx MultiDiGraph named G_sc.*

# In[38]:


def answer_six():
    global G_sc
    G_sc=answer_one().subgraph([i for i in [i for i in nx.strongly_connected_components(answer_one()) if len(i)>1][0]])
     
    return G_sc
answer_six()


# ### Question 7
# 
# What is the average distance between nodes in G_sc?
# 
# *This function should return a float.*

# In[63]:


def answer_seven():
    
    # Your Code Here
    #eccent=[value for value in nx.eccentricity(answer_six()).values()]
    return nx.average_shortest_path_length(answer_six())# Your Answer Here
answer_seven()


# ### Question 8
# 
# What is the largest possible distance between two employees in G_sc?
# 
# *This function should return an int.*

# In[40]:


def answer_eight():
        
    # Your Code Here
    
    return max([value for value in nx.eccentricity(answer_six()).values()])
answer_eight()# Your Answer Here


# ### Question 9
# 
# What is the set of nodes in G_sc with eccentricity equal to the diameter?
# 
# *This function should return a set of the node(s).*

# In[41]:


def answer_nine():
       
    # Your Code Here
    
    return set(nx.periphery(answer_six()))# Your Answer Here
answer_nine()


# ### Question 10
# 
# What is the set of node(s) in G_sc with eccentricity equal to the radius?
# 
# *This function should return a set of the node(s).*

# In[42]:


def answer_ten():
        
    # Your Code Here
    
    return set(nx.center(G_sc))
answer_ten()


# ### Question 11
# 
# Which node in G_sc is connected to the most other nodes by a shortest path of length equal to the diameter of G_sc?
# 
# How many nodes are connected to this node?
# 
# 
# *This function should return a tuple (name of node, number of satisfied connected nodes).*

# In[82]:


def answer_eleven():
    this=nx.diameter(G_sc)
    global G_sc_tuples
    G_sc_tuples=[(i,[(k,v) for k,v in d.items() if d[str(k)]==this]) for i,d in nx.shortest_path_length(G_sc).items()]
    # Your Code Here
    
    return  [(a,len(b)) for a,b in G_sc_tuples if max([len(y) for x,y in G_sc_tuples])==len(b)][0]
answer_eleven()# Your Answer Here


# ### Question 12
# 
# Suppose you want to prevent communication from flowing to the node that you found in the previous question from any node in the center of G_sc, what is the smallest number of nodes you would need to remove from the graph (you're not allowed to remove the node from the previous question or the center nodes)? 
# 
# *This function should return an integer.*

# In[87]:


def answer_twelve():

    return nx.node_connectivity(G_sc,'97',nx.center(G_sc)[0])
answer_twelve()


# ### Question 13
# 
# Construct an undirected graph G_un using G_sc (you can ignore the attributes).
# 
# *This function should return a networkx Graph.*

# In[45]:


def answer_thirteen():
    G_un=nx.Graph()
    G_un.add_edges_from([i for i in G_sc.edges()])
    # Your Code Here
    
    return G_un# Your Answer Here
answer_thirteen() # Your Answer Here


# ### Question 14
# 
# What is the transitivity and average clustering coefficient of graph G_un?
# 
# *This function should return a tuple (transitivity, avg clustering).*

# In[68]:


def answer_fourteen():
        
    # Your Code Here
    
    return (nx.transitivity(answer_thirteen()),nx.average_clustering(answer_thirteen()))
answer_fourteen()

