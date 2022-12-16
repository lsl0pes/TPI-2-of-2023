#encoding: utf8

# YOUR NAME:
# YOUR NUMBER:

# COLLEAGUES WITH WHOM YOU DISCUSSED THIS ASSIGNMENT:
# - ...
# - ...

from semantic_network import *
from bayes_net import *
from constraintsearch import *


class MySN(SemanticNetwork):

    def __init__(self):
        SemanticNetwork.__init__(self)
        # ADD CODE HERE IF NEEDED
        pass

    def is_object(self,user,obj):
        # IMPLEMENT HERE
        pass

    def is_type(self,user,type):
        # IMPLEMENT HERE
        pass


    def infer_type(self,user,obj,xpto=xptoval):
        # IMPLEMENT HERE
        pass
 
    def infer_signature(self,user,assoc,xpto=xptoval):
        # IMPLEMENT HERE
        pass


class MyBN(BayesNet):

    def __init__(self):
        BayesNet.__init__(self)
        # ADD CODE HERE IF NEEDED
        pass

    def markov_blanket(self,var):
        # IMPLEMENT HERE
        pass


class MyCS(ConstraintSearch):

    def __init__(self,domains,constraints):
        ConstraintSearch.__init__(self,domains,constraints)
        # ADD CODE HERE IF NEEDED
        pass

    def propagate(self,domains,var):
        # IMPLEMENT HERE
        pass

    def higherorder2binary(self,ho_c_vars,unary_c):
        # IMPLEMENT HERE
        pass


