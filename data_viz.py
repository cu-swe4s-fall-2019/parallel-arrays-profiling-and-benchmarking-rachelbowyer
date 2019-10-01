import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def boxplot(L, nameset, group_col_name, gene_name, out_file_name):
    """generates boxplot of data"""
    fig = plt.figure(figsize=(10, 3), dpi=300)

    ax = fig.add_subplot(1, 1, 1)

    ax.boxplot(L)
    ax.set_xticklabels(nameset, rotation=90)
    ax.set_xlabel(group_col_name)
    ax.set_title(gene_name)
    ax.set_ylabel('Gene Read Counts')

    plt.savefig(out_file_name, bbox_inches='tight')
    plt.close()

    return out_file_name


def histogram(L, out_file_name):
    """generates histogram of data"""

    fig_hist = plt.figure(figsize=(3, 3), dpi=300)
    histax = fig_hist.add_subplot(1, 1, 1)
    histax.hist(L)
    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)
    histax.set_title('mean=%s, stdev=%s' % (mean, stdev))
    histax.set_xlabel('Value')
    histax.set_ylabel('Frequency')
    fig_hist.savefig(out_file_name, bbox_inches='tight')
    plt.close()

    return out_file_name


def combo(L, out_file_name):
    """generates histogram and boxplot of data"""
    fig_c = plt.figure()
    ax1 = fig_c.add_subplot(1, 2, 1)
    ax1.boxplot(L)
    ax1.set_ylabel('Value')

    ax0 = fig_c.add_subplot(1, 2, 2)
    ax0.hist(L)
    ax0.set_xlabel('Value')
    ax0.set_ylabel('Frequency')

    fig_c.tight_layout()
    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)
    fig_c.suptitle('mean=%s, stdev=%s' % (mean, stdev))
    fig_c.savefig(out_file_name, bbox_inches='tight')
    plt.close()

    return out_file_name
