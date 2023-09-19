import torch
import torch.multiprocessing as multiprocessing
from torch.multiprocessing import queue
d = queue.Queue(ctx=multiprocessing.get_context())
#e = queue.Queue()
