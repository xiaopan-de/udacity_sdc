
from importlib.resources import path
from posixpath import basename
import glob


from utils import get_data
import matplotlib.pyplot as plt
import os
from PIL import Image
from matplotlib.patches import Rectangle


def viz(ground_truth, predictions):
    """
    create a grid visualization of images with color coded bboxes
    args:
    - ground_truth [list[dict]]: ground truth data
    """
    # IMPLEMENT THIS FUNCTION
    paths = glob.glob('data/images/*')
    print(len(paths))

    # mapping to access data faster
    gt_dic = {}
    for gt in ground_truth:
        gt_dic[gt['filename']] = gt

    # mapping to access data faster
    pred_dic = {}
    for pred in predictions:
        pred_dic[pred['filename']] = pred

    # print(len(gt_dic))
    # color mapping of classes
    color_map = {1: [1, 0, 0], 2: [0, 1, 0], 4: [0, 0, 1]}

    fig, ax = plt.subplots(4, 5, figsize=(20, 10))
    for i in range(20):
        x = i % 4
        y = i % 5
        file_name = os.path.basename(paths[i])
        img = Image.open(paths[i])
        ax[x, y].imshow(img)

        boxes = gt_dic[file_name]['boxes']
        classes = gt_dic[file_name]['classes']

        for cl, bb in zip(classes, boxes):
            y1, x1, y2, x2 = bb
            rec = Rectangle((x1, y2), x2-x1, y2-y1, facecolor='none', edgecolor=color_map[cl])
            ax[x, y].add_patch(rec)

        if file_name in pred_dic.keys():
            pred_boxes = pred_dic[file_name]['boxes']
            pred_classes = pred_dic[file_name]['classes']

            for cl, bb in zip(pred_classes, pred_boxes):
                y1, x1, y2, x2 = bb
                rec = Rectangle((x1, y2), x2-x1, y2-y1, facecolor='none', edgecolor=color_map[cl], linestyle='dashed')
                ax[x, y].add_patch(rec)

        ax[x, y].axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    ground_truth, predictions = get_data()
    viz(ground_truth, predictions)
