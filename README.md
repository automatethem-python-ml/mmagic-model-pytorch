# mmagic-model-pytorch

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

## Image super-resolution

```
python demo/mmagic_inference_demo.py \
        --model-name esrgan \
        --img predict_inputs/bbb.png \
        --result-out-dir predict_outputs/ccc.png \
        --device cpu
```

## Video super-resolution

Video super-resolution  
https://github.com/open-mmlab/mmagic/blob/main/docs/en/user_guides/inference.md#video-super-resolution

```
BasicVSR / BasicVSR++ / IconVSR / RealBasicVSR
```
```
python demo/mmagic_inference_demo.py \
        --model-name iconvsr \
        --video predict_inputs/narrator_speech.mp4 \
        --result-out-dir predict_outputs/narrator_speech_2x.mp4 \
        --device cpu
```
