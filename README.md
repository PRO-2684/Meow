# Meow
## Introduction
This project is intended to classify faces of cats at USTC, which shall also work for other cats.

## Train
`python train.py -i ./ustc -o ./model`

## Evaluate
`python evaluate.py -m ./model -e ./ustc_eval`

## Recognize
`python recognize.py *image_paths`

_Remember to modify `cats` to respective cat names._

Special thanks to the owner of [this repository](https://github.com/gao329700254/mnist_practise), who gave me the idea of solving recurring bugs.
