import gradio as gr
import subprocess

# 開 MoonTV 服務
subprocess.Popen(["npm", "start"])

# 用 gradio proxy 出嚟
demo = gr.Interface(lambda: "MoonTV Running", inputs=[], outputs="text")
demo.launch(server_port=7860)
