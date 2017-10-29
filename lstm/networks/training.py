import tensorflow as tf
import re

from lstm.utils.config import cfg
import numpy as np


# 解码中文字符
def decode_sparse_tensor(sparse_tensor):
    #print("sparse_tensor = ", sparse_tensor)
    decoded_indexes = list()
    current_i = 0
    current_seq = []
    for offset, i_and_index in enumerate(sparse_tensor[0]):
        i = i_and_index[0]
        if i != current_i:
            decoded_indexes.append(current_seq)
            current_i = i
            current_seq = list()
        current_seq.append(offset)
    decoded_indexes.append(current_seq)
    #print("decoded_indexes = ", decoded_indexes)
    result = []
    for index in decoded_indexes:
        #print("index = ", index)
        result.append(decode_a_seq(index, sparse_tensor))
        #print(result)
    return result
    
def decode_a_seq(indexes, spars_tensor):
      decoded = []
      for m in indexes:
          str =spars_tensor[1][m] #DIGITS[spars_tensor[1][m]]
          decoded.append(str)
      return decoded




def accuracy_calculation(original_seq,decoded_seq,ignore_value=0,isPrint = True):
    
    original_list = decode_sparse_tensor(test_targets)
    if len(decoded_list [0])==0:
        print("decoded_list is empty") 
        return
    detected_list = decode_sparse_tensor(decoded_list)
    true_numer = 0   
    if len(original_list) != len(detected_list):
        print("len(original_list)", len(original_list), "len(detected_list)", len(detected_list),
              " test and detect length desn't match")
        return
    print("or/de: or(length) ---- de(length)")
    for idx, number in enumerate(original_list):
        detect_number = detected_list[idx]
        hit = (number == detect_number)
        print('-------T/F{}--------'.format(hit))
        print(number, "(", len(number), ")") 
        print(detect_number, "(", len(detect_number), ")")
        if hit:
            true_numer = true_numer + 1
    print("Test Accuracy:", true_numer * 1.0 / len(original_list))

