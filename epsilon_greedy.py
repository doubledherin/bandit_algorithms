import random

class EpsilonGreedy():
    def __init__(self, epsilon, counts, values):
        self.epsilon = epsilon
        self.counts = counts
        self.values = values

    def initialize(self, n_arms):
        self.counts = [0 for i in xrange(n_arms)]
        self.values = [0 for i in xrange(n_arms)]

    def get_index_of_max(self, value_list):
        m = max(value_list)
        return value_list.index(m)

    def choose_arm(self):
        if random.random() > self.epsilon:
            return self.get_index_of_max(self.values)
        else:
            return random.randrange(len(self.values))

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        count = self.counts[chosen_arm]
        value = self.values[chosen_arm]
        new_value = ((n - 1) / float(count)) * value + (1 / float(count)) * reward
        self.values[chosen_arm] = new_value

if __name__ == "__main__":
    greed = EpsilonGreedy(1.0, [], [])
    greed.initialize(2)
    print greed.counts
    print greed.values