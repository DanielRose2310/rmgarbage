import re
import numpy as np
import string

def rle(message):
    encoded_string = np.array([])
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1): 
            if (message[j] == message[j + 1]): 
                count = count + 1
                j = j + 1
            else: 
                break
        encoded_string = np.append(encoded_string,count)
        i = j + 1
    return encoded_string


def rmg_toolong(x,length = 20):
    if len(x)>=length:
        return True
    else:
        return False

def rmg_bad_alnum_ratio(x,threshold = 0.5):
    str_len = len(x)

    nchar_alphanum = len(re.findall("[a-zA-Z0-9]", x))

    if (nchar_alphanum / str_len) <=threshold:
        return True
    else:
        return False

def rmg_consecutive_four_identical(x, n = 4):


    inds = rle(x)
    
    if any(inds > n):
        return True
    else:
        return False

def rmg_bad_consonant_vowel_ratio(x, ratio = 0.1):

    str_len = len(x)
    alpha_count = len(re.findall("[a-zA-Z]", x))

    vowel_count  = len(re.sub("[^aeiouy]","", x.lower()))
    consonant_count = alpha_count - vowel_count

    if(consonant_count >= 0 & vowel_count >= 0):
        vc_ratio = vowel_count / consonant_count
        
        if (vc_ratio < ratio or vc_ratio > 10):
            return True
        else:
            return False

def rmg_has_two_distinct_puncts_inside(x):

    out1 = x[1:-1]
    
    out2 = len(out1) - len(out1.translate(str.maketrans('', '', string.punctuation)))

    if (out2 >= 2):
        return True
    else:
        return False


def rmg_has_uppercase_within_lowercase(x):
    
    out1 = x.translate(str.maketrans('', '', string.punctuation))
    
    uc_indices = [c.isupper() for c in list(out1)]
    if any(uc_indices) and not all(uc_indices):
        return True
    else:
        return False

def rmg_uppercase_lowercase_ratio(x):
    
    out1 = x.translate(str.maketrans('', '', string.punctuation))
    
    str_len = len(out1)
    
    uppers_n = len([c for c in list(x) if c.isupper()])
    
    if uppers_n>int(str_len)/2 and uppers_n<str_len:
        return True
    else:
        return False
    
    

def rmgarbage(x):
    if any([
      rmg_bad_alnum_ratio(x),
      rmg_bad_consonant_vowel_ratio(x),
      rmg_consecutive_four_identical(x),
      rmg_has_two_distinct_puncts_inside(x),
      rmg_has_uppercase_within_lowercase(x),
      rmg_toolong(x),
      rmg_uppercase_lowercase_ratio(x)
    ]):
        return True
    else:
        return False


