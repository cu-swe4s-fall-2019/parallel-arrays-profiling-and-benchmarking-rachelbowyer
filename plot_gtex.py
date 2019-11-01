import data_viz
import gzip
import sys
import matplotlib
import argparse
matplotlib.use('Agg')
import matplotlib.pylab as plt
sys.path.insert(1, "./hash-tables-rachelbowyer")
import hash_tables as ht
import hash_functions as hf
import numpy as np


def linear_search(key, L):
    """does a linear search"""
    hit = -1
    for i in range(len(L)):
        curr = L[i]
        if key == curr:
            return i
    return -1


def binary_search(key, D):
    """does a binary search"""
    lo = -1
    hi = len(D)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == D[mid][0]:
            return D[mid][1]

        if (key < D[mid][0]):
            hi = mid
        else:
            lo = mid

    return -1

def main():
    """main function"""
    data_file_name = args.gzfile
    sample_info_file_name = args.txtfile
    group_col_name = args.group_type
    gene_name = args.gene

    sample_id_col_name = 'SAMPID'

    samples = []
    sample_info_header = None
    for l in open(sample_info_file_name):
        if sample_info_header is None:
            sample_info_header = l.rstrip().split('\t')
        else:
            samples.append(l.rstrip().split('\t'))

    group_col_idx = linear_search(group_col_name, sample_info_header)
    sample_id_col_idx = linear_search(sample_id_col_name, sample_info_header)

    groups = []
    members = []

    names = []
    for row_idx in range(len(samples)):
        sample = samples[row_idx]
        sample_name = sample[sample_id_col_idx]
        curr_group = sample[group_col_idx]
        names = names + [curr_group]

        curr_group_idx = linear_search(curr_group, groups)

        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            members.append([])

        members[curr_group_idx].append(sample_name)

    nameset = list(dict.fromkeys(names).keys())

    version = None
    dim = None
    data_header = None

    gene_name_col = 1

    group_counts = [[] for i in range(len(groups))]
    
    Table1 = ht.ChainedHash(len(nameset),hf.h_rolling)
    
    for l in gzip.open(data_file_name, 'rt'):
        if version is None:
            version = l
            continue

        if dim is None:
            dim = [int(x) for x in l.rstrip().split()]
            continue

        if data_header is None:
            data_header = []
            i = 0
            for field in l.rstrip().split('\t'):
                data_header.append([field, i])
                i += 1
            data_header.sort(key=lambda tup: tup[0])

            continue

        A = l.rstrip().split('\t')

        if A[gene_name_col] == gene_name:
            for group_idx in range(len(groups)):
                for member in members[group_idx]:
                    member_idx = binary_search(member, data_header)
                    if member_idx != -1:
                        group_counts[group_idx].append(int(A[member_idx]))
                        Table1.add(groups[group_idx],int(A[member_idx]))
            break
    
    group_counts = [[] for i in range(len(groups))]
    i = 0
    for key in np.unique(Table1.keys):
        group_counts[i].append(Table1.search(key))
        i = i + 1
        
    print(Table1.search('Blood'))

    g = data_viz.boxplot(
        group_counts, sorted(nameset), group_col_name, gene_name, args.outfile)
    
def mainp():
    """main function"""
    data_file_name = args.gzfile
    sample_info_file_name = args.txtfile
    group_col_name = args.group_type
    gene_name = args.gene

    sample_id_col_name = 'SAMPID'

    samples = []
    sample_info_header = None
    for l in open(sample_info_file_name):
        if sample_info_header is None:
            sample_info_header = l.rstrip().split('\t')
        else:
            samples.append(l.rstrip().split('\t'))

    group_col_idx = linear_search(group_col_name, sample_info_header)
    sample_id_col_idx = linear_search(sample_id_col_name, sample_info_header)

    groups = []
    members = []

    names = []
        
    MemTable = ht.ChainedHash(30,hf.h_rolling)
    for row_idx in range(len(samples)):
        sample = samples[row_idx]
        sample_name = sample[sample_id_col_idx]
        curr_group = sample[group_col_idx]
        names = names + [curr_group]

        curr_group_idx = linear_search(curr_group, groups)

        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            members.append([])
        #print(sample_name)
        MemTable.add(curr_group, sample_name)
        members[curr_group_idx].append(sample_name)
    
    #print(MemTable.search('Blood'))
    #print(members[0])
    nameset = list(dict.fromkeys(names).keys())

    version = None
    dim = None
    data_header = None

    gene_name_col = 1

    group_counts = [[] for i in range(len(groups))]

    Table1 = ht.ChainedHash(len(nameset),hf.h_rolling)
    for l in gzip.open(data_file_name, 'rt'):
        if version is None:
            version = l
            continue

        if dim is None:
            dim = [int(x) for x in l.rstrip().split()]
            continue

        if data_header is None:
            data_header = []
            i = 0
            for field in l.rstrip().split('\t'):
                data_header.append([field, i])
                i += 1
            data_header.sort(key=lambda tup: tup[0])

            continue

        A = l.rstrip().split('\t')
        #print(A)
        
        if A[gene_name_col] == gene_name:
            for group_idx in range(len(groups)):
                print(members[group_idx])               
                for member in members[group_idx]:
                    print(member)
                    member_idx = binary_search(member, data_header)
                    if member_idx != -1:
                        group_counts[group_idx].append(int(A[member_idx]))
                        Table1.add(groups[group_idx],int(A[member_idx]))
            break
            
#             i = 0
#             for key in np.unique(MemTable.keys):
#                 # print(key)
                
#             print(MemTable.search('Vagina'))
#             print(members[8])
            
#                 for num in MemTable.search(key):
#                     print(num)
#                    member_idx = binary_search(num, data_header)
#                     if member_idx != -1:
#                         group_counts[i].append(int(A[member_idx]))
#                         Table1.add(key,int(A[member_idx]))
#                         i = i + 1
#            break
                
    
#     L = []
#     for key in np.unique(Table1.keys):
#     #for key in groups:
#         L.append(Table1.search(key))

        
#     g = data_viz.boxplot(
#         group_counts, nameset, group_col_name, gene_name, args.outfile)
#     #print(group_counts)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Specify for gene dist")
    parser.add_argument('gzfile', type=str, help='specify input .gz file')
    parser.add_argument('txtfile', type=str, help='specify input .txt file')
    parser.add_argument('gene', type=str, help='specify gene')
    parser.add_argument('group_type', type=str, help='specify SMTS or SMTSD')
    parser.add_argument('outfile', type=str, help='file name of plot produced')
    args = parser.parse_args()
    main()
