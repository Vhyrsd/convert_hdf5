import h5py

with h5py.File('target.hdf5', 'r') as f:
    group = f['data']
    print(group)