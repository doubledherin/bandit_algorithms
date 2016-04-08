import random

class EpsilonGreedy():
    def __init__(self, epsilon, counts, values):
        self.epsilon = epsilon
        self.counts = counts
        self.values = values

    def initialize(self, n_arms):
        self.counts = [0 for i in xrange(n_arms)]
        self.values = [0 for i in xrange(n_arms)]

    def choose_arm(self):
        if random.random() > self.epsilon:
            return get_index_of_max(self.values)
        else:
            return random.randrange(len(self.values))

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        count = self.counts[chosen_arm]
        value = self.values[chosen_arm]
        new_value = ((count - 1) / float(count)) * value + (1 / float(count)) * reward
        self.values[chosen_arm] = new_value


class BernoulliArm():
    def __init__(self, p):
        self.p = p

    def draw(self):
        return 0.0 if random.random() > self.p else 1.0

def get_index_of_max(value_list):
    m = max(value_list)
    return value_list.index(m)


def test_algorithm(algo, arms, num_sims, horizon):
    total = num_sims * horizon
    chosen_arms = [0.0 for i in xrange(total)]
    rewards = [0.0 for i in xrange(total)]
    cumulative_rewards = [0.0 for i in xrange(total)]
    sim_nums = [0.0 for i in xrange(total)]
    times = [0.0 for i in xrange(total)]

    for sim in xrange(num_sims):
        algo.initialize(len(arms))

        for t in xrange(1, horizon+1):
            index = (sim - 1) * horizon + t - 1
            sim_nums[index] = sim
            times[index] = t
            chosen_arm = algo.choose_arm()
            chosen_arms[index] = chosen_arm
            reward = arms[chosen_arms[index]].draw()
            rewards[index] = reward

            if t == 1:
                cumulative_rewards[index] = reward
            else:
                cumulative_rewards[index] = cumulative_rewards[index-1] + reward
            algo.update(chosen_arm, reward)
    return [sim_nums, times, chosen_arms, rewards, cumulative_rewards]

