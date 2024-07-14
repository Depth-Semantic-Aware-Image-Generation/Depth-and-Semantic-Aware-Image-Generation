# Depth-and-Semantic-Aware-Image-Generation
Bachelor's thesis: [Depth and Semantic Aware Image Generation](data/Depth and Semantic Aware Image Generation.pdf). The 27th International Conference on Technologies and Applications of Artificial Intelligence (TAAI) 2022 Domestic Track (oral).

## Preparation and Process

This repository refers to [SPADE](https://github.com/NVlabs/SPADE).
Modify the model architecture of [SPADE](https://arxiv.org/abs/1903.07291) to our proposed two-stage model architecture.
1. First, use the official weight files provided in [monodepth2](https://github.com/nianticlabs/monodepth2) to predict the depth images of all training data as the ground truth for later use.
2. Train the original [SPADE architecture](https://github.com/NVlabs/SPADE) to output depth images instead of real images.
3. Next, train [our proposed model](data/Depth and Semantic Aware Image Generation.pdf), combining segmentation images and depth images as the input, with the output remaining the same as the original [SPADE](https://github.com/NVlabs/SPADE).
4. Combining these two models enables end-to-end prediction.

## Code and folder description
