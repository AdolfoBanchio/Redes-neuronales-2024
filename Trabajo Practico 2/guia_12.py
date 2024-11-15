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
from concurrent.futures import ThreadPoolExecutor, as_completed
import copy 

def train_model(params, t_dataset, v_dataset):
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
        "epochs": 5,
        "batches_size": 100
    },
    "conf_2": {
        "learning_rate": 1e-2,
        "dropout": 0.5,
        "n1": 256,
        "n2": 128,
        "epochs": 10,
        "batches_size": 100
    },
    "conf_3": {
        "learning_rate": 5e-4,
        "dropout": 0.3,
        "n1": 64,
        "n2": 31,
        "epochs": 15,
        "batches_size": 100
    }
}

# train the 3 different configurations in parallel
models = {}
results = {}

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = {executor.submit(train_model, params, fashion_dataset, validation_dataset): name for name, params in train_configurations.items()}
    for future in as_completed(futures):
        name = futures[future]
        try:
            model, train_loss, train_accuracy, valid_loss, valid_accuracy = future.result()
            models[name] = model
            results[name] = {
                "params": train_configurations[name],
                "train_loss": train_loss,
                "train_accuracy": train_accuracy,
                "valid_loss": valid_loss,
                "valid_accuracy": valid_accuracy
            }
        except Exception as e:
            print(f"Configuration {name} failed with error: {e}")
        
        # save the results
        model_path = f"./models/{name}_model.pth"
        torch.save(model, model_path)

        results_path = f"./results/{name}_results.json"
        with open(results_path, 'w') as f:
            json.dump(results[name], f)

