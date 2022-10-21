from PIL import Image
from diffusers import StableDiffusionImg2ImgPipeline

url = "input.png"
prompt = "Floating heads surrounding a cocktail drink"

device = "mps"
model_id_or_path = "./stable-diffusion-v1-4"

pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id_or_path)
pipe = pipe.to(device)

def dummy(images, **kwargs):
	return images, False

pipe.safety_checker = dummy

init_image = Image.open(url).convert("RGB")
init_image = init_image.resize((768, 512))

images = pipe(prompt=prompt, init_image=init_image, strength=0.75, guidance_scale=7.5).images
images[0].save("output.png")
