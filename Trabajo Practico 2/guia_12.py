import fashion_classifier
import torch
import torch.optim as optim
from torch import nn
from torch.nn import functional as F
from torch.utils.data import Dataset, DataLoader, Subset, random_split
from torchvision import datasets
from torchvision import transforms
from torchvision.io import read_image
from torchvision.transforms import ToTensor, Lambda, Compose
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import scipy as sp
import scipy.linalg as linalg
#import dill
import json
from collections import defaultdict
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor, as_completed, ThreadPoolExecutor
import copy 
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def train_model(params, t_dataset, v_dataset):
    logging.debug(f"Starting training with params: {params}")
    """ 
    Trains and verifies a fashion_mnist classifier model with the given parameters

    Returns:
    - train_loss
    - train_accuracy
    - valid_loss
    - valid_accuracy
    """
    lr = params['learning_rate']
    dropout = params['dropout']
    n1 = params['n1']
    n2 = params['n2']
    epochs = params['epochs']
    batches_size = params['batches_size']
    train_loader = DataLoader(t_dataset,batch_size=batches_size, shuffle=True)
    valid_loader = DataLoader(v_dataset,batch_size=batches_size, shuffle=True)

    # create the model
    model = fashion_classifier.FashionMNISTClassifier(n1,n2,dropout)

    # create the optimizer
    optimizer = optim.SGD(model.parameters(), lr=lr)

    # create the loss function
    criterion = nn.CrossEntropyLoss()

    # train the model
    train_loss, train_accuracy, valid_loss, valid_accuracy = fashion_classifier.train_fashionMNIST_classifier(model, train_loader, valid_loader, optimizer, criterion, epochs)

    return model, train_loss, train_accuracy, valid_loss, valid_accuracy

# get the MNIST dataset from pytorch
transformer = transforms.ToTensor()
fashion_dataset = datasets.FashionMNIST(root='./data/fashion/',train=True, download=True, transform=transformer)
validation_dataset = datasets.FashionMNIST(root='./data/fashion/',train=False, download=True, transform=transformer)

# define the parameters for the different configurations
train_configurations = {
    "conf_1": {
        "learning_rate": 1e-3,
        "dropout": 0.2,
        "n1": 128,
        "n2": 64,
        "epochs": 30,
        "batches_size": 100
    },
    "conf_2": {
        "learning_rate": 1e-3,
        "dropout": 0.2,
        "n1": 128,
        "n2": 64,
        "epochs": 40,
        "batches_size": 100
    },
    "conf_3": {
        "learning_rate": 1e-3,
        "dropout": 0.5,
        "n1": 128,
        "n2": 64,
        "epochs": 50,
        "batches_size": 100
    }
}

# train the 3 different configurations
for conf_name, conf_params in train_configurations.items():
    print(f"Training configuration: {conf_name}")
    print(f"Parameters: {conf_params}")
    
    model, train_loss_inc, train_loss, valid_loss, train_acc_inc, train_acc, valid_acc = train_model(conf_params, fashion_dataset, validation_dataset)

    # save the model and the results
    model_path = f"./models/{conf_name}.pt"
    torch.save(model, model_path)
    results = {
        "train_loss_inc": train_loss_inc,
        "train_loss": train_loss,
        "valid_loss": valid_loss,
        "train_acc_inc": train_acc_inc,
        "train_acc": train_acc,
        "valid_acc": valid_acc
    }
    results_path = f"./results/{conf_name}_results.json"
    with open(results_path, 'w') as f:
        json.dump(results, f)