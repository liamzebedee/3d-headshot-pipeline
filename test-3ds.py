import replicate

# deployment = replicate.deployments.get("liamzebedee/test-3ds")
# prediction = deployment.predictions.create(
#   input={"input_image": "https://i.ibb.co/YDdkzZy/new.png"}
# )
# prediction.wait()
# print(prediction.output)
# # ['https://replicate.delivery/pbxt/MaQ13I1IOtqFGlferNvv0QOe3fjR1Z3PEGvX0xeD1Wsgt1BTC/gradio_output.mp4', 'https://replicate.delivery/pbxt/GtO0wDUFdFbFDFe3Ay4PxTEMjjEtA0w9nIOIYvacfT7utOYSA/gradio_output.ply']

# ply_file_url = prediction.output[1]

ply_file_url = "https://replicate.delivery/pbxt/98gQNZS6VlbFJtwV9JVapqfVXcPnSnxAzR6qCRpkp5yQXHMJA/gradio_output.ply"

deployment = replicate.deployments.get("liamzebedee/testplyglb")
prediction = deployment.predictions.create(
  input={"ply_file_url": ply_file_url}
)
prediction.wait()
print(prediction.output)

