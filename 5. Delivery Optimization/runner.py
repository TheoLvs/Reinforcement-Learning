import sys
sys.path.append("../")
from delivery import *
from delivery import run_episode,DeliveryQAgent,run_n_episodes
from Env import DeliveryEnvironment

env = DeliveryEnvironment(n_stops = 10,method = "time_window")
agent = DeliveryQAgent(env.observation_space,env.action_space)
run_n_episodes(env,agent,"training_100_stops_traffic.gif", n_episodes=1250)
env.render()
print('done')