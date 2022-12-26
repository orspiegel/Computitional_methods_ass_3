import scipy.io
import numpy as np

def load_mat_as_dict(file):
    mat = scipy.io.loadmat(file)
    mat = {k: v for k, v in mat.items() if k[0] != '_'}
    return mat['lfp']

def subtract_means(X):
    regularized_X = np.array([])
    for feature in X.T:
        mean = np.mean(feature)
        feature = feature - mean
        regularized_X.vstack([])
    return regularized_X.T

def create_cov_mat(X):
    return np.cov(X)

# Press the green button in the gutter to run the script.
if name == '__main__':
    #print(len(load_mat_as_dict('HW3_1.mat')))
    X = load_mat_as_dict('HW3_1.mat')
    X_reg = subtract_means(X)
    cov_mat = create_cov_mat(X_reg)
    print(len(cov_mat))