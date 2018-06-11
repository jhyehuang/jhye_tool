#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import datetime

import pytz


tz = pytz.timezone('Asia/Shanghai')
current_time = datetime.datetime.now(tz)

gdbt_param = {'max_depth':15, 'eta':.02, 'objective':'binary:logistic', 'verbose':0,
         'subsample':1.0, 'min_child_weight':50, 'gamma':0,
         'nthread': 16, 'colsample_bytree':.5, 'base_score':0.16, 'seed': 999}

def parse_args(check=True):
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dir', type=str, default='/home/zhijie.huang/github/output/',
                        help='path to save log and checkpoint.')
    
    parser.add_argument('--train_set_path', type=str, default='/home/zhijie.huang/github/kaggle-avazu/avazu_data/',
                        help='path to save train test and .')

    parser.add_argument('--tmp_data_path', type=str, default='/tmp/',
                        help='path to QuanSongCi.txt')

    parser.add_argument('--train_job_name', type=str, default='trian_job',
                        help='number of time steps of one sample.')

    parser.add_argument('--sample_pct', type=float, default=1,
                        help='batch size to use.')

    parser.add_argument('--xgb_n_trees', type=int, default=300,
                        help='xgb_n_trees')

    parser.add_argument('--reverse_dictionary', type=str, default='reverse_dictionary.json',
                        help='path to reverse_dictionary.json.')

    parser.add_argument('--learning_rate', type=float, default=0.001,
                        help='learning rate')
    
    parser.add_argument('--rf_feature_list', type=list, default=['C1', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'banner_pos', 'device_type', 'device_conn_type'],
                        help='rf_feature_list ')
    
    parser.add_argument('--n_trees', type=int, default=300,
                        help='n_trees ')
    
    parser.add_argument('--gbdt_param', type=dict, default=gdbt_param,
                        help='gdbt_param ')
    
    FLAGS, unparsed = parser.parse_known_args()

    return FLAGS, unparsed


if __name__ == '__main__':
    FLAGS, unparsed = parse_args()

    for x in dir(FLAGS):
        print(getattr(FLAGS, x))
