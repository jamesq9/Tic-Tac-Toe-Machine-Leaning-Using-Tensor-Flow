# Tic-Tac-Toe-Machine-Leaning-Using-Tensor-Flow
Ticky is a Tensor Flow Model for playing Tic Tac Toe, which is trained to chose an optimal best move at any state of the board.

## Dependecies
  TensorFlow
  Flask
  numpy

## How to Run
  sudo python3 ./server.py
  
Note: might want to change the port in server.py

## List of Files and folders
.
│   README.md
│   server.py -> starts a webservice to play tic tac toe
│   test.py -> ignore       
│   Train_TicTacToe_NW.py -> Trains the model
│   __init__.py 
│
├───data
│   │   dataGenerator.py -> generates training and test data
│   │   prepareData.py  -> fetches training and testing data that can be consumed by the model.
│   │   test.txt  -> test data
│   │   training.txt  -> training data
│   │   __init__.py
│   │
│
├───model -> contains the saved model
│       checkpoint
│       model.ckpt.data-00000-of-00001
│       model.ckpt.index
│       model.ckpt.meta
│
├───static  -> contains static fies
│   ├───css
│   │       bootstrap.css
│   │       style.css
│   │
│   └───js
│           jquery.js
│           main.js
│
└───templates
        index.html
