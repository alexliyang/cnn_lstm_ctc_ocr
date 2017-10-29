import argparse
import pprint
import numpy as np
import pdb
import sys
import os.path


this_dir = os.path.dirname(__file__)
sys.path.insert(0, this_dir + '/..')

from lstm.utils.config import  cfg, cfg_from_file, get_output_dir, get_log_dir
from lstm.networks.factory import get_network
from easydict import EasyDict as edict
from train import train_net



def parse_args():
    parser = argparse.ArgumentParser(description='Train a lstm network')
    parser.add_argument('--gpu', dest='gpu_id',
                        help='GPU device id to use [0]',
                        default=0, type=int)
    parser.add_argument('--iters', dest='max_iters',
                        help='number of iterations to train',
                        default=100, type=int)
    parser.add_argument('--cfg', dest='cfg_file',
                        help='optional config file',
                        default=None, type=str)
    parser.add_argument('--pre_train', dest='pre_train',
                        help='pre trained model',
                        default=None, type=str)
    parser.add_argument('--network', dest='network_name',
                        help='name of the network',
                        default=None, type=str)
    parser.add_argument('--restore', dest='restore',
                        help='restore or not',
                        default=0, type=int)
    if len(sys.argv) == 1:
        parser.print_help()
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    print('Called with args:')
    print(args)
    if args.cfg_file is not None:
        cfg_from_file(args.cfg_file)
    print('Using config:')
    pprint.pprint(cfg)


    output_network_name=args.network_name.split('_')[-1]

    imgdb = edict({'path':'F:/tensorflowenv/tensorflow/ocr/ifrecordtrain/train_4_6.tfrecords','name':'lstm_'+output_network_name,
                   'val_path':'F:/tensorflowenv/tensorflow/ocr/ifrecordtest/val_4_6.tfrecords' })

    output_dir = get_output_dir(imgdb, None)
    log_dir = get_log_dir(imgdb)
    print(('Output will be saved to `{:s}`'.format(output_dir)))
    print(('Logs will be saved to `{:s}`'.format(log_dir)))

    device_name = '/gpu:{:d}'.format(args.gpu_id)
    print(device_name)

    network = get_network(args.network_name)
    print(('Use network `{:s}` in training'.format(args.network_name)))

    train_net(network, imgdb,
              pre_train=args.pre_train,
              output_dir=output_dir,
              log_dir=log_dir,
              max_iters=args.max_iters,
              restore=bool(int(args.restore)))
