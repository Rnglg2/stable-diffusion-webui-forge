import subprocess
subprocess.check_call(["/bin/bash", "./webui.sh", "--cuda-stream", "--pin-shared-memory", "--cuda-malloc", "--xformers", 
                       "--unet-in-bf16", "--vae-in-bf16", "--attention-split", "--disable-attention-upcast"])
