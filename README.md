# Family Feud

<img src="https://github.com/trajonwa/familyfeud-python/blob/main/images/git_familyfeud.PNG" width=250><br>

This is a game that simulates an American television game show created by Mark Goodson in which two families compete to name the most popular answers to survey questions in order to win cash and prizes.


### User Stories


#### REQUIRED 
- [X] The game should have a menu of functions
- [X] Option 1 - Instructions
- [X] Option 2 - Play game
      - [X] The game will prompt for the name of both teams
      - [X] Team #1 will be shown the total number of correct answers and receive the first question
      - [X] The user (representing the whole team) will give an answer to the question
          - [X] If correct, the user will be 
             - [X] Notified of the correct answer
             - [X] Be shown the “board” 
             - [X] Prompted to provide another answer
        - If incorrect
            - [X] The user will be informed the answer is incorrect
            - [X] The user will be shown the number of incorrect answers to that question so far
            - If this is the first or second incorrect answer
               - [X] Be asked to provide another answer
        - If this is the third incorrect answer  
            - [X] Team #2 will have an opportunity to guess one of the remaining answers   
                - [X] If they guess correctly they win that round and get the total number of points on “the board”    
                - [X] If they guess incorrectly, team #1 will win the round and get the total number of points on “the board”     
      - [X] For the next round, the opposite team will go first
      - After two questions       
         - [X] The score should be displayed      
         - [X] The user should be asked if they want to play another round                           
            - [ ] If yes, repeat above steps                                       
            - [X] If not, display the final score, the winner and go back to the start menu                                              
- [X] Option 3 - Add New Cards
      - [X] The user should be able to add the questions, answers, points and any other relevant data to the application.                                                        
      - [ ] The game should confirm the user’s input has been added and show the last 3 cards that have been added to the system   
- [ ] Total points for a question is 100
- [X] There are usually four to eight answers per question                                                                                         
- [X] There should be at least 10 questions saved that are randomly presented to the user                                                                              
     - [X] There should never be the same question in one “game”        


### App Walkthough GIF
<img src="https://github.com/trajonwa/familyfeud-python/blob/main/images/familyfeud_gif.gif" width=250><br>
