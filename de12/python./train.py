from train import Agent

class RandomAgent(Agent):

    def act(self, state):
        return self.env.action_space.sample()
        import gym

env = gym.make('CartPole-v0')
agent = RandomAgent(env=env)
scores = agent.train(episodes=100)
scores = agent.train(episodes=100, render=True)
scores = agent.test(episodes=10)
scores = agent.test(episodes=10, render=True)
pip install train
git clone https://github.com/marella/train.git
cd train
pip install -e .
pip install -e .[examples]
cd examples
python PPO.py
