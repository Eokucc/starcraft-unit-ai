import population as pop

#create network socket to communicate with Starcraft

#create base population
p = pop.Population(100, network_shape=[3,2,3,4])

p.evaulate_network(0,[1,2,3])
p.set_score(0,12)
p.evaulate_network(55,[1,2,3])

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
