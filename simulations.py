execfile("epsilon_greedy.py")

import random

random.seed(1)
means = [0.1, 0.1, 0.1, 0.1, 0.9]
n_arms = len(means)
random.shuffle(means)
arms = map(lambda mu: BernoulliArm(mu), means)
print("Best arm is " + str(get_index_of_max(means)))

with open("standard_results.tsv", "wb") as f:
    for epsilon in [0.1, 0.2, 0.3, 0.4, 0.5]:
        algo = EpsilonGreedy(epsilon, [], [])
        algo.initialize(n_arms)
        results = test_algorithm(algo, arms, 5, 250)
        for i in xrange(len(results[0])):
            f.write(str(epsilon) + "\t")
            for j in xrange(len(results)):
                f.write("\t".join([str(results[j][i]) + "\n"]))
