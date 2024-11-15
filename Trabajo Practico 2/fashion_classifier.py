import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from tqdm import tqdm

class FashionMNISTClassifier(nn.Module):
  def __init__(self, n1,n2, dropout_val=0.2):
    super(FashionMNISTClassifier, self).__init__()
    self.flatten = nn.Flatten()
    self.full_connected_1 = nn.Linear(28*28,n1)
    self.full_connected_2 = nn.Linear(n1,n2)
    self.output = nn.Linear(n2,10)

    # define activation funtion and dropout
    self.relu = nn.ReLU()
    self.dropout = nn.Dropout(dropout_val)

  def forward(self, x):
    # first flatten the input image
    x = self.flatten(x)

    # forward to the first hidden layer
    x = self.relu(self.full_connected_1(x))
    x = self.dropout(x)

    # forward to the second hidden layer
    x = F.relu(self.full_connected_2(x))
    x = self.dropout(x)

    # forward to the output layer
    x = self.output(x)
    return x


def train_batches_fashionMNIST_classifier(model, train_loader, optimizer, criterion):
  """
  Trains the model for all the batches in train_loader

  Returns:
  - avg entropy loss
  - avg accuracy
  """
  model.train()
  num_samples = len(train_loader.dataset)
  num_batches = len(train_loader)
  train_total_entropy_loss = 0
  train_total_accuracy = 0
  
  for images, labels in train_loader:
    optimizer.zero_grad()
    pred = model(images)
    loss = criterion(pred, labels)
    loss.backward()
    optimizer.step()

    train_total_entropy_loss += loss.item()
    
    train_total_accuracy += (pred.argmax(1) == labels).type(torch.float).sum().item()

  avg_entropy_loss = train_total_entropy_loss/num_batches
  avg_accuracy = train_total_accuracy/num_samples
  return avg_entropy_loss, avg_accuracy


def valid_batches_fashionMNIST_classifier(model, valid_loader, criterion):
  validation_entropy_loss = 0
  validation_accuracy = 0

  num_samples = len(valid_loader.dataset)
  num_batches = len(valid_loader)

  model.eval()
  with torch.no_grad():
    for images, labels in valid_loader:
      pred = model(images)
      loss = criterion(pred, labels)
      validation_entropy_loss += loss.item()
      validation_accuracy += (pred.argmax(1) == labels).type(torch.float).sum().item() # calculate the accuracy of batch

  avg_entropy_loss = validation_entropy_loss/num_batches
  avg_accuracy = validation_accuracy/num_samples
  return avg_entropy_loss, avg_accuracy


def train_fashionMNIST_classifier(model, train_loader, valid_loader, optimizer, criterion, epochs):
  train_entropy_loss_incorrect = []
  train_entropy_loss = []
  train_accuracy_incorrect = []
  train_accuracy = []
  
  valid_entropy_loss = []
  valid_accuracy = []
  for epoch in tqdm(range(epochs)):

    # train one epoch
    train_entropy_inc, train_acc_inc = train_batches_fashionMNIST_classifier(model, train_loader, optimizer, criterion)
    train_entropy_loss_incorrect.append(train_entropy_inc)
    train_accuracy_incorrect.append(train_acc_inc)

    # check avg loss and accuracy for incorrect predictions
    train_entropy, train_acc = valid_batches_fashionMNIST_classifier(model, train_loader, criterion)
    train_entropy_loss.append(train_entropy)
    train_accuracy.append(train_acc)

    # validate the epoch
    valid_entropy, valid_acc = valid_batches_fashionMNIST_classifier(model, valid_loader, criterion)
    valid_entropy_loss.append(valid_entropy)
    valid_accuracy.append(valid_acc)

  return train_entropy_loss_incorrect, train_entropy_loss, valid_entropy_loss, train_accuracy_incorrect, train_accuracy, valid_accuracy