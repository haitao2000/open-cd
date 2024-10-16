import os

if __name__ == '__main__':
    root_path = '../data/LEVIR-CD'
    list_from = os.path.join(root_path, 'train/A')
    list_to = os.path.join(root_path, 'train/B')
    for image in os.listdir(list_from):
        if image in os.listdir(list_to):
            continue
        else:
            print(image)