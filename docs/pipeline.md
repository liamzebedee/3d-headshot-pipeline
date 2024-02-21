

## 2D image pipeline.

### Input.

|                     |         |   |   |   |
|---------------------|---------|---|---|---|
| **Prompt**          |    `{character_name}`'s face, facing camera (0° angle), headshot, cartoon colours, gta v style, hyperrealism, a photorealistic painting, hyper realistic face, (clear white background:5)     |   |   |   |
| **Negative prompt** |    text, multicolored, black and white, signature, sig, (merged hands:1.3), (merged arms:1.3), merged, legs, merged bodyparts, BadDream, (UnrealisticDream:1.2), bad_prompt_version2, bad-artist bad-artist-anime, EasyNegative , longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, multiple people     |   |   |   |
| **Input image**     |    ![](https://i.imgur.com/F13wrbW.png)     |   |   |   |
| **Style image**     | _Empty_ |   |   |   |

### Output.

![ex 1](./demo-assets/2d/walter%20white/22kaecdbrd73vfq5bjmvgl2h5m.png) ![ex 2](./demo-assets/2d/walter%20white/fprlb4dbkpb46b6cr7grl33nom.png)

![ex 3](./demo-assets/2d/walter%20white/toqy4clbb5ox3lfto7xkbt3olq.png) ![ex 4](./demo-assets/2d/walter%20white/tqeytkdb3s3he6md7vseg362vm.png)


## 3D model pipeline.

### Input.

Same as outputs from 2D above.

### Output.

<video autoplay loop controls src="./demo-assets/3d/walter%20white/qswmc33bww76mxfe5eho6goyqe_video.mp4"></video> 

<video autoplay loop controls src="./demo-assets/3d/walter%20white/y3rch2tbdbxfbx6reprjqfmbka_video.mp4"></video>

See [./demo-assets/3d/walter%20white/](./demo-assets/3d/walter%20white/) for the mp4's, and raw 3D object outputs and textures.

## Performance.

### 3D stage - DreamFusion.

120s (cold boot) + 30s (first run) + 120s (gen/inference) = 270s per generation. This is based on Nvidia A40 (Large) GPU. Trialed with Nvidia A100 (80GB) GPU which gave run times of 109.5s and 130.25s.