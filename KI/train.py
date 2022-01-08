import numpy as np
from agent import Agent
from plotter import plotLearning
from environment import Environment
import gym as gym





if __name__ == '__main__':
    agent = Agent(alpha=0.0005,  gamma=0.99,n_actions=3)
    env = Environment(['msft', 'goog'], 500)
    
    score_history = []
    num_episodes = 2000

    for i in range(num_episodes):
        done = False
        score = 0
        observation = env.reset()
        
        actions = []
        observations = []
        rewards = []
        
        while not done:
            action = agent.choose_action(observation.values)
            
            actions.append(action)
            observations.append(observation)
            
            observation_, rewards, done, info = env.step(actions)
            if(rewards != None):
                agent.store_transition(observations, actions, rewards)
                actions = []
                observations = []
                rewards = []
                score += sum(rewards)
            observation = observation_
        score_history.append(score)

        agent.learn()
        avg_score = np.mean(score_history[-100:])
        print('episode: ', i,'score: %.1f' % score,
            'average score %.1f' % avg_score)

    filename = 'trade.png'
    plotLearning(score_history, filename=filename, window=100)
