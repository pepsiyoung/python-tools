# from matplotlib import pyplot as plt
import argparse
from pathlib import Path
from tqdm import tqdm


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, required=True, help='labels存放的位置')
    parser.add_argument('--labels', type=str, nargs='+', default=['xuhan1', 'xuhan2', 'liewen', 'duanlu'])
    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == "__main__":
    opt = parse_opt(True)
    source = opt.source
    labels = opt.labels

    values_cnt = {}
    for index, label in enumerate(labels):
        values_cnt[str(index)] = 0

    txt_paths = Path(source).glob('**/*.txt')
    for txt_path in tqdm(list(txt_paths)):
        with open(txt_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                value = line[0]
                values_cnt[value] = values_cnt.get(value, 0) + 1

    data = values_cnt.values()
    print(data)

    # # 显示数据标签
    # for x, y in zip(range(len(data)), data):
    #     plt.text(x, y, '%.0f' % y, ha='center', va='bottom', )
    #
    # plt.bar(range(len(data)), data, tick_label=labels)
    # # 字体设置
    # plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    # plt.show()
