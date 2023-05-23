from make_env import make_env
import logging
import time
import numpy as np

logger = logging.getLogger(__name__)


def _game_loop(env, render):
    """Simple episode loop"""
    obs = env.reset()
    done = False

    if render:
        env.render()
        time.sleep(0.5)

    while not done:
        actions = [int(act) for act in env.action_space.sample()]

        nobs, nreward, ndone, _ = env.step(actions)
        if sum(nreward) > 0:
            print(nreward)

        if render:
            env.render()
            time.sleep(0.5)

        done = all(ndone)
    print(env.players[0].score, env.players[1].score)


def main(game_count=1, render=True):

    env = make_env('simple_push')

    obs = env.reset()

    for _ in range(game_count):
        _game_loop(env, render)


if __name__ == '__main__':
    main()
