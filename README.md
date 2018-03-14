# My Kaggle Camera Model Identification 

A transfer learning for camera model classification

This code is modified on [Andres Torrubia'repo](https://github.com/antorsae/sp-society-camera-model-identification)

his work is awesome!

## Requirements
TensorFlow 1.2

Keras 2.1.4

CUDA9 cuDNN7

## Running
I tried several models which has released by [fchollet](https://github.com/fchollet/deep-learning-models/releases)

My parameters 

    python train-densenet.py -g 1 -b 8 -cs 224 -cm densenet -l 1e-4 -uiw -x
    python train.py -g 1 -b 16 -cs 512 -cm ResNet50 -x -l 1e-4 -uiw
    python train.py -g 1 -b 4 -cs 512 -cm InceptionResNetV2 -l 1e-4 -uiw -x
    
I use the addtional dataset by [Gleb Posobin](https://www.kaggle.com/c/sp-society-camera-model-identification/discussion/47235)
