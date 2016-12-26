"""
TD method solves a simplified version of the card game "Sette e Mezzo"

Assumptions:
* Game is played 1v1 dealer vs player;
* By the end of each match, player either wins +1 or loses -1;
* At each state, player can either hit (new card) or stand;
* Dealer has perfect knowledge of the final score of the player;
(This is a significant advantage vs the real game, in reality the dealer might 
just stand at 6.0 or higher - this can be modified in the code)
* Dealer hits until either gets the same score as the player or goes bust;
* Dealer wins ties;
* Deck is continuously reshuffled. 

The below implementation assigns a specific value to each of the player's 
possible (state, action) pair. 
A GTO strategy can be derived from the resulting (state, action) table.

@author: Riccardo Rossi
"""

# Game parameters
MAX_EPISODES = int(1e7)

# Import basic libraries
import numpy as np
import time
np.random.seed(int(time.time()))
start = time.time()


"""
Implementation of the Game
"""
class SetteMezzo():
    
    def __init__(self, winValue=1.0, bustValue=7.5):
        self.winValue = winValue
        self.loseValue = -self.winValue
        self.bustValue = bustValue
        
    
    def reset(self):
        self.playerScore = self.hitCard()
        self.dealerScore = self.hitCard()
        self.playerHand = []
        return (self.playerScore)
        
    def hitCard(self):
        value = np.random.random_integers(1, 10)
        if value > 7:
            value = 0.5
        return (value)
    
    def step(self, stand):
        playerLost = playerWon = False
        self.playerHand.append([self.playerScore, stand])
        
        if not stand:
            self.playerScore += self.hitCard()

            if self.playerScore > self.bustValue:
                playerLost = True      
        
        if stand:
            # Change here if you wish to hard-code a goal for the Dealer
            while self.dealerScore < self.playerScore:
                self.dealerScore += self.hitCard()
                
            if (self.dealerScore > self.bustValue or 
                self.dealerScore < self.playerScore):  # Currently redundant
                playerWon = True
            else:
                playerLost = True
                
        return (self.playerScore, 
                self.winValue * playerWon + self.loseValue * playerLost, 
                (playerLost or stand))
            

"""
Agent learns via the below updating formula:
    Q(s, a) <- Q(s, a) + ALPHA * [ reward + GAMMA * max_a Q(S_t+1, a) +
                                   - Q(S_t, a_t) ]
Note the formula is somewhat in between the TD method and Q-learning
"""
class Agent():

    def __init__(self, maxValue=7.5, Delta=0.5):

        # Initialization of useful variables and constants
        self._GAMMA = 1.0
        self._ALPHA = 0.05
        self._INITIAL_STATE_VALUE = 1.0
        self._EPSILON = 0.1
        self.maxValue = maxValue
        self.Delta = Delta
        
        self.state_action = self._INITIAL_STATE_VALUE * np.ones([
                                                int(maxValue/Delta), 
                                                2])
                                                
    def getIndex(self, obs):
        return (int((obs - self.Delta) / self.Delta))
        
    def act(self, obs):

        index = self.getIndex(obs)
        if np.random.random() > self._EPSILON:
            action = np.argmax(self.state_action[index])
        else:
            action = np.random.random_integers(0, 1)
        return (action)
    
    
    def train(self, playerHand, nextValue):
        
        while playerHand:
            score, choice = playerHand.pop()
            index = self.getIndex(score)
            self.state_action[index, choice] += self._ALPHA * (
                self._GAMMA * nextValue - self.state_action[index, choice]
                )
            
            nextValue = self.state_action[index].max()
    
    
    def close(self):
        
        rows, col = self.state_action.shape
        col += 1
        
        result = np.zeros([rows, col])        
        result[:, 0] = np.array([0.5 * (i+1) for i in range(15)])
        result[:, 1:] = self.state_action.astype(float)
        
        formattedResult = np.zeros([rows, col])
        for i in range(rows):
            for j in range(col):
                formattedResult[i, j] = '{:03.2f}'.format(result[i, j])

        print ('State-Action Value Table \n')
        print ('Reward is +1 if player wins, -1 if player loses \n')
        print ('__ Value_Hit___Stand')            
        print (formattedResult)
        
        
"""
Main loop 
"""
if __name__== "__main__":

    # Initialization of the game and the agent
    env = SetteMezzo()
    agent = Agent()
     
    
    # Start the game loop
    for episode in range(1, MAX_EPISODES + 1):
        obs, done = env.reset(), False
        
        while not done:
            
            # Decide next action and feed the decision to the environment         
            action = agent.act(obs)
            obs, reward, done = env.step(action)  
          
        agent.train(env.playerHand, reward)
        
    # Save info and shut activities
    agent.close()
    print ('The process took', round(time.time() - start, 1), 'seconds')
    
    