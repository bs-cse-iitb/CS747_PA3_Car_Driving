from importlib.resources import path
from gym_driving.assets.car import *
from gym_driving.envs.environment import *
from gym_driving.envs.driving_env import *
from gym_driving.assets.terrain import *

import time
import pygame, sys
from pygame.locals import *
import random
import math
import argparse

# Do NOT change these values
TIMESTEPS = 1000#1000
FPS = 30# 30
NUM_EPISODES = 10  #10

class Task1():

    def __init__(self):
        """
        Can modify to include variables as required
        """

        super().__init__()

    def next_action(self, state):
        """
        Input: The current state
        Output: Action to be taken
        TO BE FILLED
        """

        # Replace with your implementation to determine actions to be taken
        #action_steer = None
        #action_acc = None
        action_steer = 1
        action_acc = 2

        #print(state)

        action = np.array([action_steer, action_acc])  

        return action

    def controller_task1(self, config_filepath=None, render_mode=False):
        """
        This is the main controller function. You can modify it as required except for the parts specifically not to be modified.
        Additionally, you can define helper functions within the class if needed for your logic.
        """
    
        ######### Do NOT modify these lines ##########
        pygame.init()
        fpsClock = pygame.time.Clock()

        if config_filepath is None:
            config_filepath = '../configs/config.json'

        simulator = DrivingEnv('T1', render_mode=render_mode, config_filepath=config_filepath)

        time.sleep(3)
        ##############################################



        def rotation(state,x_,y_):
            x = state[0]
            y = -state[1]   #(x,y) positive in fourth coordinate
            theta = state[3]
            
            theta_rad = math.atan((y_-y)/(x_-x))
            
            #theta_rad = math.atan((math.pi*(y_-y/(x_-x))/180))
            theta_ = (180*theta_rad)/math.pi
            if theta_<=0:
                theta_=abs(theta_)
            else:
                theta_=360-theta_
            
            #step = round(abs((theta - theta_)/3))
            return theta_

        def rotate(state,theta_):
            theta = state[3]
            # if ((abs(theta-theta_)<=4)):

            if ((abs(theta-theta_)<=3) or (abs(theta-theta_)>=357)):    
                action = [1,4]
            elif(theta<theta_):
                action = [2,2]
            else:
                action = [0,2]

            return action

        def get_action(state):
            theta_ =rotation(state,350,-25)
            return rotate(state,theta_)


        # e is the number of the current episode, running it for 10 episodes
        for e in range(NUM_EPISODES):
        
            ######### Do NOT modify these lines ##########
            
            # To keep track of the number of timesteps per epoch
            cur_time = 0

            # To reset the simulator at the beginning of each episode
            state = simulator._reset()

            
            # Variable representing if you have reached the road
            road_status = False
            ##############################################
    

            # # co-ordinate of target is (350, -25) not (350,0)
            # y_= -25  # 25
            # x_=350

            

            # # print("state:",state)
            # # print("theta, theta_, step",theta,theta_,step)

            # # The following code is a basic example of the usage of the simulator
            for t in range(TIMESTEPS):
        
            #     # Checks for quit
            #     if render_mode:
            #         for event in pygame.event.get():
            #             if event.type == QUIT:
            #                 pygame.quit()
            #                 sys.exit()
            #     #print(t+1)
            #     #print(state)
            #     if t==0:
            #         action = [1,2] # 
            #     elif t==1:
            #         x = state[0]
            #         # co-ordinate system position is different
            #         # e.g x and y is positive in fourth coordinate 
            #         y = -state[1]   #(x,y) positive in fourth coordinate
            #         theta = state[3]
            #         theta_rad = math.atan((y_-y)/(x_-x))
            #         #theta_rad = math.atan((math.pi*(y_-y/(x_-x))/180))
            #         theta_ = (180*theta_rad)/math.pi
            #         if theta_<0:
            #             theta_=abs(theta_)
            #         else:
            #             theta_=360-theta_
                    
            #         step = round(abs((theta - theta_)/3))

            #         #print("theta, theta_, step",theta,theta_,step)

            #     elif t > 1:

            #         if t<step+2:
            #             if theta_>theta:
            #                 action = [2,2]
            #             else:
            #                 action = [0,2]

            #         else:
            #             #print(theta_,state[3])
            #             action = [1,4]


                
                action = get_action(state)

                state, reward, terminate, reached_road, info_dict = simulator._step(action)
                fpsClock.tick(FPS)

                cur_time += 1

                if terminate:
                    road_status = reached_road
                    break

            # Writing the output at each episode to STDOUT
            print(str(road_status) + ' ' + str(cur_time))
        
            #print("state:",state)
            #print("theta, theta_, step",theta,theta_,step)
        


class Task2():

    def __init__(self):
        """
        Can modify to include variables as required
        """

        self.flag =0

        super().__init__()

    def next_action(self, state):
        """
        Input: The current state
        Output: Action to be taken
        TO BE FILLED

        You can modify the function to take in extra arguments and return extra quantities apart from the ones specified if required
        """

        # Replace with your implementation to determine actions to be taken
        action_steer = None
        action_acc = None

        action_steer = 2
        action_acc = 4

        action = np.array([action_steer, action_acc])  

        return action
    
    def controller_task2(self, config_filepath=None, render_mode=False):
        """
        This is the main controller function. You can modify it as required except for the parts specifically not to be modified.
        Additionally, you can define helper functions within the class if needed for your logic.
        """
        
        ################ Do NOT modify these lines ################
        pygame.init()
        fpsClock = pygame.time.Clock()

        if config_filepath is None:
            config_filepath = '../configs/config.json'

        time.sleep(3)
        ##########################################################
        def coordinate(x,y):
            ls = []
            y=-y
            ls.append([x-50,y-50])
            ls.append([x+50,y-50])
            ls.append([x+50,y+50])
            ls.append([x-50,y+50])
            #print(ls)
            return ls

        def rotation(state,x_,y_):
            x = state[0]
            y = -state[1]   #(x,y) positive in fourth coordinate
            theta = state[3]
            
            theta_rad = math.atan((y_-y)/(x_-x))
            
            #theta_rad = math.atan((math.pi*(y_-y/(x_-x))/180))
            theta_ = (180*theta_rad)/math.pi
            if theta_<=0:
                theta_=abs(theta_)
            else:
                theta_=360-theta_
            
            step = round(abs((theta - theta_)/3))
            return theta_
        def rotate(state,theta_):
            theta = state[3]
            # if ((abs(theta-theta_)<=4)):

            if ((abs(theta-theta_)<=3) or (abs(theta-theta_)>=357)):
              
                if (state[1] < 25 and state[1] > -75):
                    self.flag = 1


                action = [1,4]
            elif(theta<theta_):
                action = [2,2]
            else:
                action = [0,2]

            return action
        def get_action(state):
            if state[1] < 25 and state[1] > -75:
                theta_ =rotation(state,350,-25)
                #print(theta,theta_)
                return rotate(state,theta_)
                #theta_ = 0
            else:
                theta_ = theta_up
            #print(f"This is theta_ : {theta_}")
            #print(f"This is theta : {theta}\n")

            return rotate(state,theta_)

        def check_obstacle(state,obs1,obs2,obs3,obs4):
            y = -state[1]
            x = state[0]
            y_mistake =-25
            limit =20
            
            #first quardant
            if y>=y_mistake and x>0:    
                if x>obs1[0][0]-limit and x< obs1[1][0]+limit:
                    #print("test")
                    if y > obs1[2][1]:    
                        return True
            # second quardant 
            elif (y>y_mistake and x<0):
                if x>obs2[0][0]-limit and x< obs2[1][0]+limit:
                    if y > obs2[2][1]:
                        return True
            #third quardant
            elif(y<y_mistake and x<0):
                if x>obs3[0][0]-limit and x< obs3[1][0]+limit:
                    if y < obs3[2][1]:
                        return True
            #fourth quardant
            elif(y<y_mistake  and x>0):
                if x>obs4[0][0]-limit and x< obs4[1][0]+limit:
                    if y < obs4[2][1]:
                        return True
            return False
        # e is the number of the current episode, running it for 10 episodes
        for e in range(NUM_EPISODES):

            ################ Setting up the environment, do NOT modify these lines ################
            # To randomly initialize centers of the traps within a determined range
            ran_cen_1x = random.randint(120, 230)
            ran_cen_1y = random.randint(120, 230)
            ran_cen_1 = [ran_cen_1x, ran_cen_1y]

            ran_cen_2x = random.randint(120, 230)
            ran_cen_2y = random.randint(-230, -120)
            ran_cen_2 = [ran_cen_2x, ran_cen_2y]

            ran_cen_3x = random.randint(-230, -120)
            ran_cen_3y = random.randint(120, 230)
            ran_cen_3 = [ran_cen_3x, ran_cen_3y]

            ran_cen_4x = random.randint(-230, -120)
            ran_cen_4y = random.randint(-230, -120)
            ran_cen_4 = [ran_cen_4x, ran_cen_4y]

            ran_cen_list = [ran_cen_1, ran_cen_2, ran_cen_3, ran_cen_4]            
            eligible_list = []


            #my code
            obs1 = coordinate(ran_cen_1x, ran_cen_1y)
            obs2 = coordinate(ran_cen_2x, ran_cen_2y)
            obs3 = coordinate(ran_cen_3x, ran_cen_3y)
            obs4 = coordinate(ran_cen_4x, ran_cen_4y)

            #print(obs1,obs2,obs3,obs4)
            # To randomly initialize the car within a determined range
            for x in range(-300, 300):
                for y in range(-300, 300):

                    if x >= (ran_cen_1x - 110) and x <= (ran_cen_1x + 110) and y >= (ran_cen_1y - 110) and y <= (ran_cen_1y + 110):
                        continue

                    if x >= (ran_cen_2x - 110) and x <= (ran_cen_2x + 110) and y >= (ran_cen_2y - 110) and y <= (ran_cen_2y + 110):
                        continue

                    if x >= (ran_cen_3x - 110) and x <= (ran_cen_3x + 110) and y >= (ran_cen_3y - 110) and y <= (ran_cen_3y + 110):
                        continue

                    if x >= (ran_cen_4x - 110) and x <= (ran_cen_4x + 110) and y >= (ran_cen_4y - 110) and y <= (ran_cen_4y + 110):
                        continue

                    eligible_list.append((x,y))

            simulator = DrivingEnv('T2', eligible_list, render_mode=render_mode, config_filepath=config_filepath, ran_cen_list=ran_cen_list)
        
            # To keep track of the number of timesteps per episode
            cur_time = 0

            # To reset the simulator at the beginning of each episode
            state = simulator._reset(eligible_list=eligible_list)
            ###########################################################
            #time.sleep(30)
            # The following code is a basic example of the usage of the simulator
            road_status = False
            initial_state = state
            if initial_state[1] > -25:
                theta_up = 270
            else:
                theta_up = 90
            #theta_up = rotation(state,initial_state[0]-0.00001,-25)
            #print(state[0],state[1])
            for t in range(TIMESTEPS):
                theta =state[3]
                # Checks for quit
                if render_mode:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()

                
                        

    
                if (check_obstacle(state,obs2,obs4,obs3,obs1)):
                    action=rotate(state,0)
                else:  
                    if self.flag==1:
                        action = [1,4] 
                    else:
                        action = get_action(state)
                    #print(action)


                
                state, reward, terminate, reached_road, info_dict = simulator._step(action)
                fpsClock.tick(FPS)

                cur_time += 1
                #time.sleep(.1)

                if terminate:
                    road_status = reached_road
                    break

            print(str(road_status) + ' ' + str(cur_time))
        
            self.flag =0

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="config filepath", default=None)
    parser.add_argument("-t", "--task", help="task number", choices=['T1', 'T2'])
    parser.add_argument("-r", "--random_seed", help="random seed", type=int, default=0)
    parser.add_argument("-m", "--render_mode", action='store_true')
    parser.add_argument("-f", "--frames_per_sec", help="fps", type=int, default=30) # Keep this as the default while running your simulation to visualize results
    args = parser.parse_args()

    config_filepath = args.config
    task = args.task
    random_seed = args.random_seed
    render_mode = args.render_mode
    fps = args.frames_per_sec

    FPS = fps

    random.seed(random_seed)
    np.random.seed(random_seed)

    if task == 'T1':
        
        agent = Task1()
        agent.controller_task1(config_filepath=config_filepath, render_mode=render_mode)

    else:

        agent = Task2()
        agent.controller_task2(config_filepath=config_filepath, render_mode=render_mode)
