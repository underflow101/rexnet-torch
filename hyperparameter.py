#####################################################################
# hyperparameter.py
#
# Dev. Dongwon Paek
# Description: PyTorch model file of ReXNet
#####################################################################

CLASSES = ('others', 'phoneWithHand', 'writing', 'sleep')

EPOCHS = 20
BATCH_SIZE = 4
NUM_CLASSES = 4
IMG_SIZE = 224
IN_CHANNELS = 3

LEARNING_RATE = 0.5
DECAY = 1e-5
MOMENTUM = 0.9

NUM_WORKERS = 12

class CONFIG():
    # dataset info
    input_channels = 3
    num_classes = 4

    # training settings
    lr = 0.5
    momentum = 0.9
    weight_decay = 1e-5
    num_epochs = 20
    batch_size = 4
    pretrained_model = None

    # misc
    mode = 'train'
    use_gpu = True
    use_tensorboard = False

    # dataset
    data_path = '/home/bearpaek/data/datasets/lplSmall/'
    train_data_path = '/home/bearpaek/data/datasets/lplSmall/train/'
    test_data_path = '/home/bearpaek/data/datasets/lplSmall/validation/'

    # path
    log_path = './logs'
    model_save_path = './models'

    # epoch step size
    loss_log_step = 1
    model_save_step = 1
    train_eval_step = 1
    def __init__(self):
        super().__init__()