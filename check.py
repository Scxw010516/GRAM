import torch
import torch_ema
from torch.distributed.checkpoint import load_state_dict

context = 'Pre_train_model/CelebA'
generator = torch.load('pretrained_models/CARLA_default/ema.pth')
# generator = torch.load('Output/EarOutputDir3/EarOutputDir3/ema.pth')
# discriminator = torch.load(context + '/discriminator.pth')
print(generator)
# print(discriminator)
