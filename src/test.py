import argparse
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights-ww', type=str, default=ROOT / 'yolov5s.pt', help='initial weights path')
    parser.add_argument('--cfg', type=str, default='', help='model.yaml path')
    parser.add_argument('--rect', action='store_true', help='rectangular training')

    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == "__main__":
    # opt = parse_opt(False)
    # print(opt)
    # print('rect', opt.rect)
    # print('weights', opt.weights_ww)
    # known = True
    # res = 1 if known else 2
    # print(res)

    my_path = Path(ROOT).joinpath('source')
    print(my_path)
