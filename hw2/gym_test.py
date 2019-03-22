"""

@author: Nisar Ahamed K
Created On 3/21/2019
"""

import gym


env = gym.make('SpaceInvaders-v0')
env.reset()

for i in range(100):
    env.render()
    env.step(env.action_space.sample())

env.close()