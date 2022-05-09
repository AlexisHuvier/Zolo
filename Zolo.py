from utils.zolo import Zolo
import os


os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.system("title Zolo")

z = Zolo()
z.launch()
