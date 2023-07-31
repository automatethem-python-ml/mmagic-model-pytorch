# mmagic-model

https://github.com/open-mmlab/mmagic

https://github.com/open-mmlab/mmagic/blob/main/docs/en/user_guides/inference.md


## 설치

```
conda create -n mmagic-model-pytorch python=3.10.9
conda activate mmagic-model-pytorch
```

```
pip install -r requirements.txt
conda install --file requirements_conda_pytorch.txt -c pytorch -y
```

```
pip3 install openmim
mim install 'mmcv>=2.0.0'
mim install 'mmengine'
mim install 'mmagic'
```

## Video super-resolution

Video super-resolution  
https://github.com/open-mmlab/mmagic/blob/main/docs/en/user_guides/inference.md#video-super-resolution
```
import os
from mmagic.apis import MMagicInferencer
from mmengine import mkdir_or_exist

# Create a MMagicInferencer instance and infer
video = './resources/input/video_interpolation/b-3LLDhc4EU_000000_000010.mp4'
result_out_dir = './resources/output/video_super_resolution/tutorial_video_super_resolution_basicvsr_res.mp4'
mkdir_or_exist(os.path.dirname(result_out_dir))
editor = MMagicInferencer('basicvsr')
results = editor.infer(video=video, result_out_dir=result_out_dir)
```
