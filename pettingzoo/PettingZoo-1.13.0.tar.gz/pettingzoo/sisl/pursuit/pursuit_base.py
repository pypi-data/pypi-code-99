import glob
import os
from os.path import join
from subprocess import call

import numpy as np
import pygame
from gym import spaces
from gym.utils import seeding

from .utils import agent_utils, two_d_maps
from .utils.agent_layer import AgentLayer
from .utils.controllers import RandomPolicy, SingleActionPolicy

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'


class Pursuit():

    def __init__(self, **kwargs):
        """
        In evade purusit a set of pursuers must 'tag' a set of evaders
        Required arguments:
            x_size, y_size: World size
            local_ratio: proportion of reward allocated locally vs distributed among all agents
            n_evaders
            n_pursuers
            obs_range: how far each agent can see
        Optional arguments:
        pursuer controller: stationary policy of ally pursuers
        evader controller: stationary policy of opponent evaders

        tag_reward: reward for 'tagging' a single evader

        max_cycles: after how many frames should the game end
        n_catch: how surrounded evader needs to be, before removal
        freeze_evaders: toggle evaders move or not
        catch_reward: reward for pursuer who catches an evader
        urgency_reward: reward added in each step
        surround: toggles surround condition for evader removal
        constraint_window: window in which agents can randomly spawn
        """

        self.x_size = kwargs.pop('x_size', 16)
        self.y_size = kwargs.pop('y_size', 16)
        x_size = self.x_size
        y_size = self.y_size
        self.map_matrix = two_d_maps.rectangle_map(self.x_size, self.y_size)
        self.max_cycles = kwargs.pop("max_cycles", 500)
        self.seed()

        self.local_ratio = kwargs.pop('local_ratio', 1.0)

        self.n_evaders = kwargs.pop('n_evaders', 30)
        self.n_pursuers = kwargs.pop('n_pursuers', 8)
        self.num_agents = self.n_pursuers

        self.latest_reward_state = [0 for _ in range(self.num_agents)]
        self.latest_done_state = [False for _ in range(self.num_agents)]
        self.latest_obs = [None for _ in range(self.num_agents)]

        # can see 7 grids around them by default
        self.obs_range = kwargs.pop('obs_range', 7)
        # assert self.obs_range % 2 != 0, "obs_range should be odd"
        self.obs_offset = int((self.obs_range - 1) / 2)
        self.pursuers = agent_utils.create_agents(
            self.n_pursuers, self.map_matrix, self.obs_range, self.np_random)
        self.evaders = agent_utils.create_agents(
            self.n_evaders, self.map_matrix, self.obs_range, self.np_random)

        self.pursuer_layer = AgentLayer(x_size, y_size, self.pursuers)
        self.evader_layer = AgentLayer(x_size, y_size, self.evaders)

        self.n_catch = kwargs.pop('n_catch', 2)

        n_act_purs = self.pursuer_layer.get_nactions(0)
        n_act_ev = self.evader_layer.get_nactions(0)

        self.freeze_evaders = kwargs.pop('freeze_evaders', False)

        if self.freeze_evaders:
            self.evader_controller = kwargs.pop(
                'evader_controller', SingleActionPolicy(4))
            self.pursuer_controller = kwargs.pop(
                'pursuer_controller', SingleActionPolicy(4))
        else:
            self.evader_controller = kwargs.pop(
                'evader_controller', RandomPolicy(n_act_purs, self.np_random))
            self.pursuer_controller = kwargs.pop(
                'pursuer_controller', RandomPolicy(n_act_ev, self.np_random))

        self.current_agent_layer = np.zeros((x_size, y_size), dtype=np.int32)

        self.tag_reward = kwargs.pop('tag_reward', 0.01)

        self.catch_reward = kwargs.pop('catch_reward', 5.0)

        self.urgency_reward = kwargs.pop('urgency_reward', 0.0)

        self.ally_actions = np.zeros(n_act_purs, dtype=np.int32)
        self.opponent_actions = np.zeros(n_act_ev, dtype=np.int32)

        max_agents_overlap = max(self.n_pursuers, self.n_evaders)
        obs_space = spaces.Box(low=0, high=max_agents_overlap, shape=(
            self.obs_range, self.obs_range, 3), dtype=np.float32)
        act_space = spaces.Discrete(n_act_purs)
        self.action_space = [act_space for _ in range(self.n_pursuers)]

        self.observation_space = [obs_space for _ in range(self.n_pursuers)]
        self.act_dims = [n_act_purs for i in range(self.n_pursuers)]

        self.evaders_gone = np.array([False for i in range(self.n_evaders)])

        self.surround = kwargs.pop('surround', True)

        self.constraint_window = kwargs.pop('constraint_window', 1.0)

        self.surround_mask = np.array([[-1, 0], [1, 0], [0, 1], [0, -1]])

        self.model_state = np.zeros(
            (4,) + self.map_matrix.shape, dtype=np.float32)
        self.renderOn = False
        self.pixel_scale = 30

        self.frames = 0
        self.reset()
        assert not kwargs, f"gave arguments {list(kwargs.keys())} that are not valid pursuit arguments"

    def observation_space(self, agent):
        return self.observation_spaces[agent]

    def action_space(self, agent):
        return self.action_spaces[agent]

    def close(self):
        if self.renderOn:
            pygame.event.pump()
            pygame.display.quit()
            pygame.quit()
            self.renderOn = False

    #################################################################
    # The functions below are the interface with MultiAgentSiulator #
    #################################################################

    @property
    def agents(self):
        return self.pursuers

    def seed(self, seed=None):
        self.np_random, seed_ = seeding.np_random(seed)
        try:
            policies = [self.evader_controller, self.pursuer_controller]
            for policy in policies:
                try:
                    policy.set_rng(self.np_random)
                except AttributeError:
                    pass
        except AttributeError:
            pass

        return [seed_]

    def get_param_values(self):
        return self.__dict__

    def reset(self):
        self.evaders_gone.fill(False)

        x_window_start = self.np_random.uniform(0.0, 1.0 - self.constraint_window)
        y_window_start = self.np_random.uniform(0.0, 1.0 - self.constraint_window)
        xlb, xub = int(self.x_size * x_window_start), int(self.x_size * (x_window_start + self.constraint_window))
        ylb, yub = int(self.y_size * y_window_start), int(self.y_size * (y_window_start + self.constraint_window))
        constraints = [[xlb, xub], [ylb, yub]]

        self.pursuers = agent_utils.create_agents(self.n_pursuers, self.map_matrix, self.obs_range, self.np_random,
                                                  randinit=True, constraints=constraints)
        self.pursuer_layer = AgentLayer(self.x_size, self.y_size, self.pursuers)

        self.evaders = agent_utils.create_agents(self.n_evaders, self.map_matrix, self.obs_range, self.np_random,
                                                 randinit=True, constraints=constraints)
        self.evader_layer = AgentLayer(self.x_size, self.y_size, self.evaders)

        self.latest_reward_state = [0 for _ in range(self.num_agents)]
        self.latest_done_state = [False for _ in range(self.num_agents)]
        self.latest_obs = [None for _ in range(self.num_agents)]

        self.model_state[0] = self.map_matrix
        self.model_state[1] = self.pursuer_layer.get_state_matrix()
        self.model_state[2] = self.evader_layer.get_state_matrix()

        self.frames = 0
        self.renderOn = False

        return self.safely_observe(0)

    def step(self, action, agent_id, is_last):
        agent_layer = self.pursuer_layer
        opponent_layer = self.evader_layer
        opponent_controller = self.evader_controller

        # actual action application
        agent_layer.move_agent(agent_id, action)

        self.latest_reward_state = self.reward() / self.num_agents

        if is_last:
            ev_remove, pr_remove, pursuers_who_remove = self.remove_agents()

            for i in range(opponent_layer.n_agents()):
                # controller input should be an observation, but doesn't matter right now
                a = opponent_controller.act(self.model_state)
                opponent_layer.move_agent(i, a)

            self.latest_reward_state += self.catch_reward * pursuers_who_remove
            self.latest_reward_state += self.urgency_reward

        self.model_state[0] = self.map_matrix
        self.model_state[1] = self.pursuer_layer.get_state_matrix()
        self.model_state[2] = self.evader_layer.get_state_matrix()

        if is_last:
            global_val = self.latest_reward_state.mean()
            local_val = self.latest_reward_state
            self.latest_reward_state = self.local_ratio * local_val + (1 - self.local_ratio) * global_val
            self.frames = self.frames + 1

    def draw_model_state(self):
        # -1 is building pixel flag
        x_len, y_len = self.model_state[0].shape
        for x in range(x_len):
            for y in range(y_len):
                pos = pygame.Rect(
                    self.pixel_scale * x, self.pixel_scale * y, self.pixel_scale, self.pixel_scale)
                col = (0, 0, 0)
                if self.model_state[0][x][y] == -1:
                    col = (255, 255, 255)
                pygame.draw.rect(self.screen, col, pos)

    def draw_pursuers_observations(self):
        for i in range(self.pursuer_layer.n_agents()):
            x, y = self.pursuer_layer.get_position(i)
            patch = pygame.Surface(
                (self.pixel_scale * self.obs_range, self.pixel_scale * self.obs_range))
            patch.set_alpha(128)
            patch.fill((255, 152, 72))
            ofst = self.obs_range / 2.0
            self.screen.blit(
                patch, (self.pixel_scale * (x - ofst + 1 / 2), self.pixel_scale * (y - ofst + 1 / 2)))

    def draw_pursuers(self):
        for i in range(self.pursuer_layer.n_agents()):
            x, y = self.pursuer_layer.get_position(i)
            center = (int(self.pixel_scale * x + self.pixel_scale / 2),
                      int(self.pixel_scale * y + self.pixel_scale / 2))
            col = (255, 0, 0)
            pygame.draw.circle(self.screen, col, center, int(self.pixel_scale / 3))

    def draw_evaders(self):
        for i in range(self.evader_layer.n_agents()):
            x, y = self.evader_layer.get_position(i)
            center = (int(self.pixel_scale * x + self.pixel_scale / 2),
                      int(self.pixel_scale * y + self.pixel_scale / 2))
            col = (0, 0, 255)

            pygame.draw.circle(self.screen, col, center, int(self.pixel_scale / 3))

    def render(self, mode="human"):
        if not self.renderOn:
            if mode == "human":
                pygame.display.init()
                self.screen = pygame.display.set_mode(
                    (self.pixel_scale * self.x_size, self.pixel_scale * self.y_size))
            else:
                self.screen = pygame.Surface((self.pixel_scale * self.x_size, self.pixel_scale * self.y_size))

            self.renderOn = True
        self.draw_model_state()

        self.draw_pursuers_observations()

        self.draw_evaders()
        self.draw_pursuers()

        observation = pygame.surfarray.pixels3d(self.screen)
        new_observation = np.copy(observation)
        del observation
        if mode == "human":
            pygame.display.flip()
        return np.transpose(new_observation, axes=(1, 0, 2)) if mode == "rgb_array" else None

    def animate(self, act_fn, nsteps, file_name, rate=1.5, verbose=False):
        """
            Save an animation to an mp4 file.
        """
        # run sim loop
        o = self.reset()
        file_path = "/".join(file_name.split("/")[0:-1])
        temp_name = join(file_path, "temp_0.png")
        # generate .pngs
        self.save_image(temp_name)
        removed = 0
        for i in range(nsteps):
            a = act_fn(o)
            o, r, done, info = self.step(a)
            temp_name = join(file_path, "temp_" + str(i + 1) + ".png")
            self.save_image(temp_name)
            removed += info['removed']
            if done:
                break
        # use ffmpeg to create .pngs to .mp4 movie
        ffmpeg_cmd = "ffmpeg -framerate " + str(rate) + " -i " + join(
            file_path, "temp_%d.png") + " -c:v libx264 -pix_fmt yuv420p " + file_name
        call(ffmpeg_cmd.split())
        # clean-up by removing .pngs
        map(os.remove, glob.glob(join(file_path, "temp_*.png")))

    def save_image(self, file_name):
        self.render()
        capture = pygame.surfarray.array3d(self.screen)

        xl, xh = -self.obs_offset - 1, self.x_size + self.obs_offset + 1
        yl, yh = -self.obs_offset - 1, self.y_size + self.obs_offset + 1

        window = pygame.Rect(xl, yl, xh, yh)
        subcapture = capture.subsurface(window)

        pygame.image.save(subcapture, file_name)

    def reward(self):
        es = self.evader_layer.get_state_matrix()  # evader positions
        rewards = [
            self.tag_reward * np.sum(es[np.clip(
                self.pursuer_layer.get_position(
                    i)[0] + self.surround_mask[:, 0], 0, self.x_size - 1
            ), np.clip(
                self.pursuer_layer.get_position(i)[1] + self.surround_mask[:, 1], 0, self.y_size - 1)])
            for i in range(self.n_pursuers)
        ]
        return np.array(rewards)

    @property
    def is_terminal(self):
        # ev = self.evader_layer.get_state_matrix()  # evader positions
        # if np.sum(ev) == 0.0:
        if self.evader_layer.n_agents() == 0:
            return True
        return False

    def update_ally_controller(self, controller):
        self.ally_controller = controller

    def update_opponent_controller(self, controller):
        self.opponent_controller = controller

    def n_agents(self):
        return self.pursuer_layer.n_agents()

    def safely_observe(self, i):
        agent_layer = self.pursuer_layer
        obs = self.collect_obs(agent_layer, i)
        return obs

    def collect_obs(self, agent_layer, i):
        for j in range(self.n_agents()):
            if i == j:
                return self.collect_obs_by_idx(agent_layer, i)
        assert False, "bad index"

    def collect_obs_by_idx(self, agent_layer, agent_idx):
        # returns a flattened array of all the observations
        obs = np.zeros((3, self.obs_range, self.obs_range), dtype=np.float32)
        obs[0].fill(1.0)  # border walls set to -0.1?
        xp, yp = agent_layer.get_position(agent_idx)

        xlo, xhi, ylo, yhi, xolo, xohi, yolo, yohi = self.obs_clip(xp, yp)

        obs[0:3, xolo:xohi, yolo:yohi] = np.abs(self.model_state[0:3, xlo:xhi, ylo:yhi])
        return obs

    def obs_clip(self, x, y):
        xld = x - self.obs_offset
        xhd = x + self.obs_offset
        yld = y - self.obs_offset
        yhd = y + self.obs_offset
        xlo, xhi, ylo, yhi = (np.clip(xld, 0, self.x_size - 1), np.clip(xhd, 0, self.x_size - 1),
                              np.clip(yld, 0, self.y_size - 1), np.clip(yhd, 0, self.y_size - 1))
        xolo, yolo = abs(np.clip(xld, -self.obs_offset, 0)
                         ), abs(np.clip(yld, -self.obs_offset, 0))
        xohi, yohi = xolo + (xhi - xlo), yolo + (yhi - ylo)
        return xlo, xhi + 1, ylo, yhi + 1, xolo, xohi + 1, yolo, yohi + 1

    def remove_agents(self):
        """
        Remove agents that are caught. Return tuple (n_evader_removed, n_pursuer_removed, purs_sur)
        purs_sur: bool array, which pursuers surrounded an evader
        """
        n_pursuer_removed = 0
        n_evader_removed = 0
        removed_evade = []
        removed_pursuit = []

        ai = 0
        rems = 0
        xpur, ypur = np.nonzero(self.model_state[1])
        purs_sur = np.zeros(self.n_pursuers, dtype=bool)
        for i in range(self.n_evaders):
            if self.evaders_gone[i]:
                continue
            x, y = self.evader_layer.get_position(ai)
            if self.surround:
                pos_that_catch = self.surround_mask + \
                    self.evader_layer.get_position(ai)
                truths = np.array(
                    [np.equal([xi, yi], pos_that_catch).all(axis=1) for xi, yi in zip(xpur, ypur)])
                if np.sum(truths.any(axis=0)) == self.need_to_surround(x, y):
                    removed_evade.append(ai - rems)
                    self.evaders_gone[i] = True
                    rems += 1
                    tt = truths.any(axis=1)
                    for j in range(self.n_pursuers):
                        xpp, ypp = self.pursuer_layer.get_position(j)
                        tes = np.concatenate(
                            (xpur[tt], ypur[tt])).reshape(2, len(xpur[tt]))
                        tem = tes.T == np.array([xpp, ypp])
                        if np.any(np.all(tem, axis=1)):
                            purs_sur[j] = True
                ai += 1
            else:
                if self.model_state[1, x, y] >= self.n_catch:
                    # add prob remove?
                    removed_evade.append(ai - rems)
                    self.evaders_gone[i] = True
                    rems += 1
                    for j in range(self.n_pursuers):
                        xpp, ypp = self.pursuer_layer.get_position(j)
                        if xpp == x and ypp == y:
                            purs_sur[j] = True
                ai += 1

        ai = 0
        for i in range(self.pursuer_layer.n_agents()):
            x, y = self.pursuer_layer.get_position(i)
            # can remove pursuers probabilitcally here?
        for ridx in removed_evade:
            self.evader_layer.remove_agent(ridx)
            n_evader_removed += 1
        for ridx in removed_pursuit:
            self.pursuer_layer.remove_agent(ridx)
            n_pursuer_removed += 1
        return n_evader_removed, n_pursuer_removed, purs_sur

    def need_to_surround(self, x, y):
        """
            Compute the number of surrounding grid cells in x,y position that are open
            (no wall or obstacle)
        """
        tosur = 4
        if x == 0 or x == (self.x_size - 1):
            tosur -= 1
        if y == 0 or y == (self.y_size - 1):
            tosur -= 1
        neighbors = self.surround_mask + np.array([x, y])
        for n in neighbors:
            xn, yn = n
            if not 0 < xn < self.x_size or not 0 < yn < self.y_size:
                continue
            if self.model_state[0][xn, yn] == -1:
                tosur -= 1
        return tosur
