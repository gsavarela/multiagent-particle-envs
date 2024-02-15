from make_env import make_env
import logging
import time
import numpy as np
logger = logging.getLogger(__name__)


def _game_loop(env, render):
    """Simple episode loop"""
    obs = env.reset()
    done = False
    i = 0
    episode_return = 0
    if render:
        env.render()
        time.sleep(0.5)

    while not done:
        actions = [int(act) for act in env.action_space.sample()]

        nobs, nreward, ndone, _ = env.step(actions)
        print(nreward)
        episode_return += sum(nreward)


        if render:
            env.render()
            time.sleep(0.5)

        done = all(ndone) or i >= 25
        i += 1 
    print(episode_return)


def main(game_count=1, render=True):

    env = make_env('simple_spread')

    obs = env.reset()

    for _ in range(game_count):
        _game_loop(env, render)


if __name__ == '__main__':
    main()
