import csv
import numpy as np
from torch.utils.data import Dataset, DataLoader, SubsetRandomSampler
import pandas as pd


class SimpleDataset(Dataset):
    """SimpleDataset [summary]
    
    [extended_summary]
    
    :param path_to_csv: [description]
    :type path_to_csv: [type]
    """
    def __init__(self, path_to_csv, transform=None):
        ## TODO: Add code to read csv and load data. 
        ## You should store the data in a field.
        # Eg (on how to read .csv files):

        # self.dataset = {}
        # with open('path/to/.csv', 'r') as f:
        #    csvreader = csv.reader(f)
        #    for row in csvreader:
        #         x = row[0]
        #         y = row[1]
        #         dataset[x] = y
        #is this right? storing x y as dictionary

        ## Look up how to read .csv files using Python. This is common for datasets in projects.
        
        #or use this? 
        self.dataset = pd.read_csv(path_to_csv)

        #checkout pytorch data loaders

        self.transform = transform
        #pass

    def __len__(self):
        """__len__ [summary]
        
        [extended_summary]
        """
        ## TODO: Returns the length of the dataset.
        return len(self.dataset)
        #pass

    def __getitem__(self, index):
        """__getitem__ [summary]
        
        [extended_summary]
        
        :param index: [description]
        :type index: [type]
        """
        ## TODO: This returns only ONE sample from the dataset, for a given index.
        ## The returned sample should be a tuple (x, y) where x is your input 
        ## vector and y is your label
        ## Before returning your sample, you should check if there is a transform
        ## sepcified, and pply that transform to your sample
        # Eg:
        x = dataset.iloc[index, 0]
        y = dataset.iloc[index, 1]
        if self.transform:
           sample = self.transform(sample)
        return x, y
        ## Remember to convert the x and y into torch tensors.
        #how do i do this? 
        

       # pass


def get_data_loaders(path_to_csv, 
                     transform_fn=None,
                     train_val_test=[0.8, 0.2, 0.2], 
                     batch_size=32):
    """get_data_loaders [summary]
    
    [extended_summary]
    
    :param path_to_csv: [description]
    :type path_to_csv: [type]
    :param train_val_test: [description], defaults to [0.8, 0.2, 0.2]
    :type train_val_test: list, optional
    :param batch_size: [description], defaults to 32
    :type batch_size: int, optional
    :return: [description]
    :rtype: [type]
    """
    # First we create the dataset given the path to the .csv file
    dataset = SimpleDataset(path_to_csv, transform=transform_fn)

    # Then, we create a list of indices for all samples in the dataset.
    dataset_size = len(dataset)
    indices = list(range(dataset_size))

    ## TODO: Rewrite this section so that the indices for each dataset split
    ## are formed.

    ## BEGIN: YOUR CODE
    #0.7*dataset_size
    train_indices = []
    val_indices = []
    test_indices = []
    
    for i in range(train_val_test[0]*dataset_size):
        train_indices.append(i)
    # is this right? 



    ## END: YOUR CODE

    # Now, we define samplers for each of the train, val and test data
    train_sampler = SubsetRandomSampler(train_indices)
    train_loader = DataLoader(dataset, batch_size=batch_size, sampler=train_sampler)

    val_sampler = SubsetRandomSampler(val_indices)
    val_loader = DataLoader(dataset, batch_size=batch_size, sampler=val_sampler)

    test_sampler = SubsetRandomSampler(test_indices)
    test_loader = DataLoader(dataset, batch_size=batch_size, sampler=test_sampler)

    return train_loader, val_loader, test_loader
