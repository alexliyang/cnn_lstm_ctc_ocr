"""Factory method for easily getting imdbs by name."""

from .LSTM_train import LSTM_train
from .LSTM_test import LSTM_test


def get_network(name):
    """Get a network by name."""
    if name.split('_')[0] == 'LSTM':
        if name.split('_')[1] == 'train':
            return LSTM_train()
        elif name.split('_')[1] == 'test':
            return LSTM_test()
        else:
            raise KeyError('Unknown dataset: {}'.format(name))



