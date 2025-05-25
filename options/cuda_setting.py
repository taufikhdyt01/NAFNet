import torch

# Set device ke GPU 2
device = torch.device("cuda:2" if torch.cuda.is_available() else "cpu")

# Contoh penggunaan device ini saat membuat tensor atau model
x = torch.tensor([1.0, 2.0, 3.0]).to(device)

# Jika kamu punya model, pindahkan juga ke device ini
# model.to(device)
