import h5py

# add attributes to the 'data' group
def add_attributes_to_hdf5(input_file, attribute_list):
    with h5py.File(input_file, 'a') as f:
        group = f['data']
        for attr_pair in attribute_list:
            group.attrs[attr_pair[0]] = attr_pair[1]

input_file = 'target.hdf5'
# attribute pairs [name, value]
attribute_list = [['a','b'], ['c','d']]

add_attributes_to_hdf5(input_file, attribute_list)