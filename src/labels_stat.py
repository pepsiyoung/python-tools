from matplotlib import pyplot as plt
from pathlib import Path
from tqdm import tqdm

values_cnt = {}
labels = ['虚焊', '裂纹/裂片', '短路', '空串']
for index, label in enumerate(labels):
    values_cnt[str(index)] = 0

txt_paths = Path("/Users/pepsiyoung/Project/CSI/收集数据/有效样本").glob('**/*.txt')
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
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.show()
