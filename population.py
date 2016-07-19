# coding=utf-8

#import collections as collections
import network as network

class Population:

    def __init__(self,pop_size=100, network_shape=[8,8,8,2]):
        # how many networks are created
        self.pop_size = pop_size
        self.networks = [ network.Network(network_shape)]*pop_size
        self.scores = [0]*pop_size

    def evaulate_network(self, network_id, input):
        return self.networks[network_id].evaluate(input)

    def set_score(self, network_id, new_score):
        (self.scores[network_id])=new_score

    def breed(self):
        return 0
