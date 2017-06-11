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
D:.
│   Play.py
│   README.md
│   server.py
│   test.py
│   Train_TicTacToe_NW.py
│   __init__.py
│
├───data
│   │   0dataGenerator - Copy.py
│   │   dataGenerator.py
│   │   prepareData.py
│   │   test.txt
│   │   training.txt
│   │   __init__.py
│   │
│   └───__pycache__
│           dataGenerator.cpython-35.pyc
│           prepareData.cpython-35.pyc
│           __init__.cpython-35.pyc
│
├───model
│       checkpoint
│       model.ckpt.data-00000-of-00001
│       model.ckpt.index
│       model.ckpt.meta
│
├───static
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

