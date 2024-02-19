# LLama69's 3D HeadGen

![Screenshot 2023-11-27 at 10 38 50 am](https://github.com/Code-Bullet/RickAndMortai/assets/584141/1e9f2b8f-aa1e-415c-a5c5-b40a748c9701)

A text-to-3D asset pipeline I built for the [AI Rick and Morty TV show](https://supernova996.substack.com) to generate 3D characters.

 1. Generates 4x candidate images (.png's) in parallel using [Stable Diffusion XL](https://stablediffusionxl.com), with prompt/antiprompt/reference image configured. 
 2. Feeds these 4x images to a [DreamGaussian](http://dreamgaussian.github.io) model, generating 4x 3D models in parallel (.obj, .mtl)
 3. Downloads .zip containing 3D model (.obj) and textures (.mtl, .png)
 4. Live imports into Unity and rigs them onto a generic human model https://github.com/liamzebedee/unity-runtime-obj-importer and custom code.


## 2D image pipeline.

|                     |         |   |   |   |
|---------------------|---------|---|---|---|
| **Prompt**          |    `{character_name}`'s face, facing camera (0° angle), headshot, cartoon colours, gta v style, hyperrealism, a photorealistic painting, hyper realistic face, (clear white background:5)     |   |   |   |
| **Negative prompt** |    text, multicolored, black and white, signature, sig, (merged hands:1.3), (merged arms:1.3), merged, legs, merged bodyparts, BadDream, (UnrealisticDream:1.2), bad_prompt_version2, bad-artist bad-artist-anime, EasyNegative , longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, multiple people     |   |   |   |
| **Input image**     |    ![](https://i.imgur.com/F13wrbW.png)     |   |   |   |
| **Style image**     | _Empty_ |   |   |   |

## Performance.

### 3D stage.

120s (cold boot) + 30s (first run) + 120s (gen/inference) = 270s per generation. This is based on Nvidia A40 (Large) GPU. Trialed with Nvidia A100 (80GB) GPU which gave run times of 109.5s and 130.25s.

## Usage.

Sign up for the [Replicate](https://replicate.com) service.

```sh
export REPLICATE_API_KEY=...
pipenv install
python headshot/server.py

# Then run an inference for "mario".
curl -X POST -H "Content-Type: application/json" -d '{"character": "mario"}' http://0.0.0.0:10001/v1/character-heads/generate
```

### Demos.

A 3D donald trump generated at runtime:

![image](https://github.com/Code-Bullet/RickAndMortai/assets/584141/1e3b6919-ef48-443c-bd8d-3ea322743892)

Sam altman telling codebullet about AGI 

![Screenshot 2023-11-27 at 5 12 54 pm](https://github.com/Code-Bullet/RickAndMortai/assets/584141/8c9c5f56-2548-4c70-a2ed-3dbc15dda746)

Gordon Ramsey and Dutch guys:

![Screenshot 2023-11-27 at 10 38 50 am](https://github.com/Code-Bullet/RickAndMortai/assets/584141/1e9f2b8f-aa1e-415c-a5c5-b40a748c9701)

The new character voting chamber:

![image](https://github.com/Code-Bullet/RickAndMortai/assets/584141/3f7c327e-40d8-4cd4-92fd-b53a475b1fea)

The saved files and scenes written to disk:

![Screenshot 2023-11-28 at 4 01 44 pm](https://github.com/Code-Bullet/RickAndMortai/assets/584141/3dddff1a-9d99-4670-8791-0fc1b06209bf)

![Screen Shot 2023-11-01 at 3 51 59 pm](https://github.com/Code-Bullet/RickAndMortai/assets/584141/506b2489-66ea-46ea-b5d0-c13f5dc0621c)

## the 3d generation server (python)

Filesystem layout:

![Screenshot 2023-11-05 at 4 08 28 pm](https://github.com/Code-Bullet/RickAndMortai/assets/584141/73644c36-9af7-433b-abe8-e6050954b876)

The boys:

![Screen Shot 2023-10-23 at 6 21 14 pm](https://github.com/Code-Bullet/RickAndMortai/assets/584141/82f33aaf-a56f-433e-aaab-e13bc6feed83)

CLI view:

![Screenshot 2023-11-27 at 3 14 39 pm](https://github.com/Code-Bullet/RickAndMortai/assets/584141/95992b4c-6cd1-4ac2-a412-3f5502ab4f6e)
