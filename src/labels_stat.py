from matplotlib import pyplot as plt
from pathlib import Path
from tqdm import tqdm

if __name__ == "__main__":
    source = r'E:\DataProcess\裂片'
    labels = ['xu_han', 'lie', 'duan_lu', 'kong']

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
    # 显示数据标签
    for x, y in zip(range(len(data)), data):
        plt.text(x, y, '%.0f' % y, ha='center', va='bottom', )

    plt.bar(range(len(data)), data, tick_label=labels)
    # 字体设置
    # plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.show()
