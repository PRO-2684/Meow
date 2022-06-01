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

Special thanks to [`mnist_practise` repository](https://github.com/gao329700254/mnist_practise), which gave me the inspiration of how to solve recurring bugs, and [`CatFace` repository](https://github.com/El-Chiang/CatFace), whose our model is based on.
