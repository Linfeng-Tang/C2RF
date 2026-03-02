# C2RF
This is official Pytorch implementation of "[C2RF: Bridging Multi-modal Image Registration and Fusion via Commonality Mining and Contrastive Learning (IJCV 2025)](https://link.springer.com/article/10.1007/s11263-025-02427-1)"
 - 
```
@article{Tang2024C2RF,
	title={C2RF: Bridging Multi-modal Image Registration and Fusion via Commonality Mining and Contrastive Learning}, 
	author={Tang, Linfeng and Yan, Qinglong and Xiang, Xinyu and Fang, Leyuan and Ma, Jiayi},
	journal={International Journal of Computer Vision}, 
	year={2025},
  	volume={133},
  	pages={5262–5280},
}
```
## ✨ News  
- **[2026-02-21]** Our paper *[VideoFusion: A Spatio-Temporal Collaborative Network for Multi-modal Video Fusion](https://arxiv.org/abs/2503.23359)* of **[M3SVD](https://github.com/Linfeng-Tang/M3SVD)**  has been officially accepted by **The IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026)**!  [[Paper](https://arxiv.org/abs/2503.23359)] [[Code](https://github.com/Linfeng-Tang/VideoFusion)]
- **[2025-09-18]** Our paper *[ControlFusion: A Controllable Image Fusion Framework with Language-Vision Degradation Prompts](https://arxiv.org/pdf/2503.23356?)* has been officially accepted by **Advances in Neural Information Processing Systems (NeurIPS 2025)**! [[Paper](https://arxiv.org/pdf/2503.23356?)] [[Code](https://github.com/Linfeng-Tang/ControlFusion)]  

- **[2025-09-10]** Our paper *[Mask-DiFuser: A Masked Diffusion Model for Unified Unsupervised Image Fusion](https://ieeexplore.ieee.org/document/11162636)* has been officially accepted by **IEEE Transactions on Pattern Analysis and Machine Intelligence (IEEE TPAMI)**! [[Paper](https://ieeexplore.ieee.org/document/11162636)] [[Code](https://github.com/Linfeng-Tang/Mask-DiFuser)]  

- **[2025-03-15]** Our paper *[C2RF: Bridging Multi-modal Image Registration and Fusion via Commonality Mining and Contrastive Learning](https://github.com/Linfeng-Tang/C2RF)* has been officially accepted by the **International Journal of Computer Vision (IJCV)**! [[Paper](https://link.springer.com/article/10.1007/s11263-025-02427-1)] [[Code](https://github.com/Linfeng-Tang/C2RF)]  

- **[2025-02-11]** We released a large-scale dataset for infrared and visible video fusion: *[M3SVD: Multi-Modal Multi-Scene Video Dataset](https://github.com/Linfeng-Tang/M3SVD)*.
  
## 1. Recommended Environment
 - [ ] torch  1.10.2+cu102
 - [ ] torchvision 0.8.2 
 - [ ] kornia 0.5.2

## 2. Framework
The framework of the proposed C2RF for multi-modal image registration and fusion.
![The framework of the proposed C2RF for multi-modal image registration and fusion.](https://github.com/QinglongYan-hub/C2RF/blob/main/C2RF/Framework.png)

## 3. Pretrained Weights
Please download the pretrained weights at the link below, and then place them into the folder ./checkpoint/
- The pretrained weights for the Roadscene dataset is at [Google Drive](https://drive.google.com/drive/folders/1wOSVg9CsqZBJkHWYMGD1kCER9tThSxYk?usp=sharing).

- The pretrained weights for the PET-MRI dataset is at [Google Drive](https://drive.google.com/drive/folders/1M99NDvcnk71iZUVC6BlYyRvAKIZlUIK6?usp=sharing).

## 4. To Test
### Registration and Fusion 
#### RoadScene dataset    
    python test.py --dataset=RoadScene 
#### PET-MRI dataset
    python test.py --dataset=PET-MRI

## 5. To Train
### Training the fusion model 
#### RoadScene dataset
    python train_Fu.py --dataset=RoadScene
#### PET-MRI dataset
    python train_Fu.py --dataset=PET-MRI

### Training the registration model 
#### RoadScene dataset
    python train_Reg.py --dataset=RoadScene
#### PET-MRI dataset
    python train_Reg.py --dataset=PET-MRI
