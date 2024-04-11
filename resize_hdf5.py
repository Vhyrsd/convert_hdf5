import h5py
from PIL import Image
import numpy as np

# 打开hdf5文件
with h5py.File('target.hdf5', 'r+') as f:
    for i in range(len(f['data'])):
        view_list = []
        for view in f['data']['demo_'+str(i)]['obs']['agentview_image']:
            img = Image.fromarray(view, 'RGB')
            resized_img = img.resize((84, 84))
            view_list.append(np.array(resized_img))
        del f['data']['demo_'+str(i)]['obs']['agentview_image']
        f['data']['demo_'+str(i)]['obs']['agentview_image'] = view_list

        view_list = []
        for view in f['data']['demo_'+str(i)]['next_obs']['agentview_image']:
            img = Image.fromarray(view, 'RGB')
            resized_img = img.resize((84, 84))
            view_list.append(np.array(resized_img))
        del f['data']['demo_'+str(i)]['next_obs']['agentview_image']
        f['data']['demo_'+str(i)]['next_obs']['agentview_image'] = view_list
    