from agent import Agent
import numpy as np
import gym
from matplotlib import pyplot as plt
from IPython.display import clear_output
from time import sleep


def show_agent_behaviour(agent, environment: gym.Env, wait_s):
    state, _ = environment.reset()
    done = False
    while not done:
        print(environment.render())
        action = np.argmax(agent.qtable[state])
        next_state, _, done, _, _ = environment.step(action)  # Execute the action and get the next state
        clear_output(wait=True)
        sleep(wait_s)
        state = next_state
    clear_output(wait=True)
    print(environment.render())

def plot_rewards():
    agent = Agent()
    env = gym.make('Taxi-v3')
    agent.qlearn(env, n_games=1000)
    plt.title("Rewards")
    plt.xlabel("Game count")
    plt.ylabel("Avg reward per 10 games")
    v = []
    for i in range(0, len(agent.rewards), 10):
        group = agent.rewards[i:i+10]
        v.append(sum(group)/10)

    plt.plot(list(range(0, 1000, 10)), v)
    plt.show()

def plot_penalties():
    agent = Agent()
    env = gym.make('Taxi-v3')
    agent.qlearn(env, n_games=1000)
    plt.title("Penalties")
    plt.xlabel("Game count")
    plt.ylabel("Count of penalties per 10 games")
    v = []
    for i in range(0, len(agent.penalties), 10):
        group = agent.penalties[i:i+10]
        v.append(sum(group))

    plt.plot(list(range(0, 1000, 10)), v)
    plt.show()

def plot_evaluations():
    agent = Agent()
    env = gym.make('Taxi-v3')
    agent.qlearn(env, n_games=10000)
    plt.title("Evaluations")
    plt.xlabel("Game count")
    plt.ylabel("Avg reward in each evaluation")
    v = [sum(element)/len(element) for element in agent.eval_rewards]
    plt.plot(list(range(0, 10000, 100)), v)
    plt.show()