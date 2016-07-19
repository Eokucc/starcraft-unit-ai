#!/usr/bin/python
# coding=utf-8

import population as pop
import tcp as tcp
import time
tcp_connect = tcp.TCPConnection()

p = pop.Population(100, network_shape=[3,2,3,4])
while True:
	#create network socket to communicate with Starcraft
	tcp_connect.accept()

	while tcp_connect.is_connected():
		m = tcp_connect.read()
		tcp_connect.send([1,1])
	print('Round over')
	#time.sleep(1)
	#create base population
	

	#p.evaulate_network(0,[1,2,3])
	#p.set_score(0,12)
	#p.evaulate_network(55,[1,2,3])

	#for number of generations:
	#    for i in range(p.pop_size):
		# play games and evaluate

		#while playing
		    #receive current state
		    # input = ....

		    #and evaluate
		    #pop.evaluate(i,input)
		# transmit score to population class
		# pop.set_score(i,new_score)

	#    pop.breed()

print("Completed")
