import numpy as np


def normalize_2d_array_to_range(data, new_min=0.2, new_max=0.5):
    # 计算最小值和最大值
    min_val = np.min(data)
    max_val = np.max(data)

    # 归一化到指定范围
    normalized_data = (data - min_val) * (new_max - new_min) / (max_val - min_val) + new_min

    return normalized_data


