class Node:
    def __init__(self, feature_index=None, threshold=None, left=None, right=None, inf_gain=None, value=None):
        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left
        self.right = right
        self.inf_gain = inf_gain
        self.value = value