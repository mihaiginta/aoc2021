
marr = np.convolve(arr, np.ones(3), 'valid')

dmarr=np.diff(marr)

msum = np.sum(np.array(dmarr) >= 0, axis=0)

print(msum)