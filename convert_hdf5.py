import h5py
import os

def convert_hdf5(output_file, input_list):
    with h5py.File(output_file, 'w') as f:
        data = f.create_group('data')
        i = 0
        for file in input_list:
            with h5py.File(input_dir + '/' + file, 'r') as h5py_file:
                hand_actions = h5py_file['data']['demo_0']['actions']
                front_image_1 = h5py_file['data']['demo_0']['obs']['front_image_1']

                demo_i = data.create_group('demo_' + str(i))
                demo_i.create_dataset('action', data=hand_actions[1:, 2:])

                obs = demo_i.create_group('obs')
                obs.create_dataset('image', data=front_image_1[:-1,:,:,:])
                obs.create_dataset('agent_pos', data=hand_actions[:-1, 2:])

                next_obs = demo_i.create_group('next_obs')
                next_obs.create_dataset('image', data=front_image_1[1:,:,:,:])
                next_obs.create_dataset('agent_pos', data=hand_actions[1:, 2:])
            
            i += 1

output_file = 'target.hdf5'
input_dir = 'input_dir'
input_list = os.listdir(input_dir)

convert_hdf5(output_file, input_list)