# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:57:38 2023

@author: veoni
"""
import numpy as np
def mypseudorandrange(array_mean, array_sd, nitms, critmean, critsd, my_rangeLow, my_rangeHigh, nsamples):
    # critmean is the maximal distance between outcome mean and expected mean (0 = outcome very close to expected value)
    # critsd is the maximal distance between outcome variance and expected variance (0 = outcome very close to expected value)
    # my_range is the range
    if array_sd == 0:
        zevalues = np.tile(array_mean, (nsamples, nitms))
    else:
        pass_count = 0
        dumcount = 0
        zevalues = np.zeros((0, nitms))
        while pass_count < nsamples:
            dumcount += 1
            values = array_mean + array_sd * np.random.randn(nitms, 10000)  # generate 10000 samples
            out = np.sum((values < my_rangeLow) + (values > my_rangeHigh), axis=0) > 0
            not_out = ~out
            if np.any(not_out):
                values = values[:, not_out]
                distsd = np.abs(np.std(values,axis=0) - array_sd)  # distance between the sample statistics and expected statistics
                distmean = np.abs(np.mean(values,axis=0) - array_mean)
                zecrit = (distsd < critsd) & (distmean < critmean)  # criterion
                if np.any(zecrit):
                    pass_count += np.sum(zecrit)
                    zevalues = np.vstack((zevalues, values[:, zecrit].T))
                    if zevalues.shape[0] > nsamples:
                        zevalues = zevalues[:nsamples, :]
        # Save for distribution statistics
        # n = n + 1
        # zestds = np.append(zestds, np.std(zevalues))
        # zemeans = np.append(zemeans, np.mean(zevalues))
    # You can add code here for any additional processing or analysis you need.
    return zevalues

m_range = mypseudorandrange(.8,.1,8,.001,.001,.1,.9,100)

#m_range = mypseudorandrange(127.50,5,8,.1,1,0,255,100)