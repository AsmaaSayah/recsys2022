import numpy as np 
import pandas as pd
import scipy.sparse as sps
import os

files_directory="/content/drive/MyDrive/dressipi_recsys2022_mapped"
#Currently URM doesn't contain bought item
def get_ICM():
    df_icm = pd.read_csv(filepath_or_buffer=os.path.join(files_directory,'simplified_features.csv'), sep=',', header=0, dtype={'item_id': int, 'feature_idx': int})
            
    item_id_list = df_icm['item_id'].values
    feat_id_list = df_icm['feature_idx'].values
    rating_id_list = np.ones_like(feat_id_list)
    ICM_matrix = sps.csr_matrix((rating_id_list, (item_id_list, feat_id_list)))
    return ICM_matrix


#Canonical URM 
def get_URM(normalized=False):
    df_URM = pd.read_csv(filepath_or_buffer=os.path.join(files_directory,'train_sessions.csv'), sep=',', header=0, dtype={'session_id': int, 'item_id': int})7
    df_URM["count"]=1
    df_URM=df_URM.grouby(["session_id","item_id"])["count"].sum().reset_index()
    #TODO add something to divide train and test sessions
    session_id_list = df_URM['session_id'].values
    item_id_list = df_URM['item_id'].values
    if not normalized:
        rating_id_list = df_URM['count'].values
    else:
        rating_id_list = np.ones_like(session_id_list)

    URM_matrix_session_item_count = sps.csr_matrix((rating_id_list, (session_id_list, item_id_list)))
    return URM_matrix_session_item_count


# Additional possible URM
def get_URM_session_feature(normalized=False):
    df_URM = pd.read_csv(filepath_or_buffer=os.path.join(files_directory,'simplified_features.csv'), sep=',', header=0, dtype={'session_id': int, 'feature_idx': int,'count': int})
    #TODO add something to divide train and test sessions
    session_id_list = df_URM['session_id'].values
    feat_id_list = df_URM['feature_idx'].values
    if not normalized:
        rating_id_list = df_URM['count'].values
    else:
        rating_id_list = np.ones_like(session_id_list)

    URM_matrix_session_feature = sps.csr_matrix((rating_id_list, (session_id_list, feat_id_list)))
    return URM_matrix_session_feature