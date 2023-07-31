from mmagic.apis import MMagicInferencer
sd_inferencer = MMagicInferencer(model_name='stable_diffusion')
text_prompts = 'A panda is having dinner at KFC'
result_out_dir = 'predict_outputs/sd_res.png'
sd_inferencer.infer(text=text_prompts, result_out_dir=result_out_dir)
