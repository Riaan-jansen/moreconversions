""" """
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def normalise(data, norm_val):
    norm = []
    for i in data:
       norm.append(float(i) * float(norm_val))
    return norm


def calc_err_abs(res, err):
    i = 0
    abs_err = []
    while i < len(res):
        abs_err.append(res[i]*float(err[i]))
        i=i+1
    return abs_err

def calc_bin_width(bins):
    """ """
    bw = []
    # 1st bin is its own width
    bw.append(bins[0])
    i = 1
    while i < len(bins):
        width = float(bins[i]) - float(bins[i-1])
        bw.append(width)
        i = i + 1
    bw = np.asarray(bw)
    return bw


def plot_raw_spectra(data, fname, title):
    plt.clf()
    plt.title("Neutron energy spectra full model " + title)
    plt.xlabel("Energy (MeV)")
    plt.ylabel("flux n/cm2/proton/bin")
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(data.eng, data.result)
    plt.savefig(fname)


def plot_spectra(data, fname, title):

    bw = calc_bin_width(data.eng)
    plt.clf()
    plt.title("Neutron energy spectra full model " + title)
    plt.xlabel("Energy (MeV)")
    plt.ylabel("flux n/cm2/MeV/proton")
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(data.eng, np.asarray(data.result)/bw)
    plt.savefig(fname)

def plot_spectra_ratio(data1, data2, fname, title):
    plt.clf()
    plt.title("Comparison of " + title)
    plt.xlabel("Energy (MeV)")
    plt.ylabel("ratio")
    plt.xscale('log')
    plt.plot(data1.eng, np.asarray(data1.result)/np.asarray(data2.result))
    plt.savefig(fname)


def plot_run_comp(data, err, fname, title):
    plt.clf()
    title = "Comparison of several runs for full model Cu option at " + title
    plt.title(title)
    plt.xlabel("Run #")
    plt.ylabel("Dose Rate microSv/h")
    x = [1,2,3,4,5,6]
    plt.xlim(xmin=0, xmax=7)
    plt.errorbar(x, data, yerr=err, fmt='o')

    plt.savefig(fname)