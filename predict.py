from tensorflow import keras
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('model', help='current format for model name:\
                my_model_bsX_epsY, where bs is batch size and eps is epochs')



model = keras.models.load_model(parser.model)
