import random
import gym
import numpy as np


class Agent:
    def __init__(self, learning_rate=0.1, discount_factor=0.7, max_exploration_rate=1,
                 min_exploration_rate=0.05, exploration_decay=0.005):
        self.qtable = None
        self.rewards = []
        self.eval_rewards = []
        self.penalties = []
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = max_exploration_rate
        self.max_exploration_rate = max_exploration_rate
        self.min_exploration_rate = min_exploration_rate
        self.exploration_decay = exploration_decay

    def epsilon_greedy_policy(self, env, state):
        if random.uniform(0, 1) < self.exploration_rate:
            action = env.action_space.sample()
        else:
            action = np.argmax(self.qtable[state])
        return action

    def qlearn(self, env: gym.Env, n_games=10000, max_steps=1000, eval_freq=100, eval_len=10):
        self.qtable = np.zeros((env.observation_space.n, env.action_space.n))

        for i in range(n_games):
            reward_sum = 0
            state, _ = env.reset()
            done = False
            step = 0
            while not done and step < max_steps:
                # choose action according to policy
                action = self.epsilon_greedy_policy(env, state)

                # take chosen action
                next_state, reward, done, _, _ = env.step(action)

                # update qtable
                new_val = ((1 - self.learning_rate) * self.qtable[state][action]
                           + self.learning_rate * (reward + self.discount_factor * np.max(self.qtable[next_state])))
                self.qtable[state][action] = new_val

                reward_sum += reward

                state = next_state
                step += 1

            self.penalties.append(1 if reward == -10 else 0)
            self.rewards.append(reward_sum)

            # update exploration_rate
            if self.exploration_decay:
                self.exploration_rate = (self.min_exploration_rate +
                                         (self.max_exploration_rate - self.min_exploration_rate)
                                         * np.exp(-self.exploration_decay*i))
            
            if i % eval_freq == 0:
                cur_eval_rew = []
                for _ in range(eval_len):
                    cur_eval_rew.append(self.eval_game(env, max_steps))
                self.eval_rewards.append(cur_eval_rew)

    def eval_game(self, env, max_steps=1000):
        done = False
        reward_sum = 0
        step = 0
        state, _ = env.reset()

        while not done and step < max_steps:
            action = np.argmax(self.qtable[state])
            next_state, reward, done, _, _ = env.step(action)
            reward_sum += reward
            state = next_state
            step += 1
        
        return reward_sum

    def play_visual(self, env):
        done = False
        state, _ = env.reset()

        while not done:
            env.render()
            action = np.argmax(self.qtable[state])
            next_state, _, done, _, _, = env.step(action)
            state = next_state
        env.render()
        return states, actions


if __name__ == "__main__":
    environment = gym.make('Taxi-v3')
    agent = Agent()
    agent.qlearn(environment, n_games=1000)
    for i in range(10):
        environment = gym.make('Taxi-v3', render_mode="human")
        agent.play_visual(environment)
