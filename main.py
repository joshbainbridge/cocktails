from torch import Generator
from PIL import Image
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline

#init_path = "input.png"
#init_image = Image.open(init_path).convert("RGB")
#init_image = init_image.resize((768, 512))

prompt = '''
The consolation of rain. Figures. Oil painting.
'''

device = "mps"
model_id_or_path = "./stable-diffusion-v1-4"

#pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id_or_path)
pipe = StableDiffusionPipeline.from_pretrained(model_id_or_path)
pipe = pipe.to(device)

def dummy(images, **kwargs):
	return images, False

pipe.safety_checker = dummy

generator = Generator().manual_seed(2147483647)

#images = pipe(prompt=prompt, init_image=init_image, strength=0.75,
#              guidance_scale=7.5).images

images = pipe(prompt, guidance_scale=7.5, height=512, width=768,
              num_images_per_prompt=1, generator=generator).images

images[0].save("output.png")
