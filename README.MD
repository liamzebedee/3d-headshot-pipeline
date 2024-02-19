# LLama69's 3D HeadGen

![Screenshot 2023-11-27 at 10 38 50 am](https://github.com/Code-Bullet/RickAndMortai/assets/584141/1e9f2b8f-aa1e-415c-a5c5-b40a748c9701)

A text-to-3D asset pipeline I built for the [AI Rick and Morty TV show](https://supernova996.substack.com) to generate 3D characters.

 1. Generates 4x candidate images (.png's) in parallel using [Stable Diffusion XL](https://stablediffusionxl.com), with prompt/antiprompt/reference image configured. 
 2. Feeds these 4x images to a [DreamGaussian](http://dreamgaussian.github.io) model, generating 4x 3D models in parallel (.obj, .mtl)
 3. Downloads .zip containing 3D model (.obj) and textures (.mtl, .png)
 4. Live imports into Unity and rigs them onto a generic human model https://github.com/liamzebedee/unity-runtime-obj-importer and custom code.

## Usage.

Sign up for the [Replicate](https://replicate.com) service.

```sh
export REPLICATE_API_KEY=...
pipenv install
python headshot/server.py

# Then run an inference for "mario".
curl -X POST -H "Content-Type: application/json" -d '{"character": "mario"}' http://0.0.0.0:10001/v1/character-heads/generate
```

## Demos.

A 3D donald trump generated at runtime:

![image](https://github.com/Code-Bullet/RickAndMortai/assets/584141/1e3b6919-ef48-443c-bd8d-3ea322743892)

Sam altman telling codebullet about AGI 

![Screenshot 2023-11-27 at 5 12 54 pm](https://github.com/Code-Bullet/RickAndMortai/assets/584141/8c9c5f56-2548-4c70-a2ed-3dbc15dda746)

Gordon Ramsey and Dutch guys:

![Screenshot 2023-11-27 at 10 38 50 am](https://github.com/Code-Bullet/RickAndMortai/assets/584141/1e9f2b8f-aa1e-415c-a5c5-b40a748c9701)

## Internals.

Filesystem layout:

![Screenshot 2023-11-05 at 4 08 28 pm](https://github.com/Code-Bullet/RickAndMortai/assets/584141/73644c36-9af7-433b-abe8-e6050954b876)

The boys:

![Screen Shot 2023-10-23 at 6 21 14 pm](https://github.com/Code-Bullet/RickAndMortai/assets/584141/82f33aaf-a56f-433e-aaab-e13bc6feed83)

## Notice.

Copyright LLaMa69 Inc, 2023.