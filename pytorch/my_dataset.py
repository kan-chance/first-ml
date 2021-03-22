import pandas as pd
import torch
from torch.utils.data import DataLoader, Dataset
from PIL import Image
from torchvision import transforms

class my_dataset(Dataset):
    def __init__(self, csv_path,transform=None):
        #csvファイル読み込み。
        df = pd.read_csv(csv_path)
        path1 = df['image1']
        path2 = df['image2']
        image_paths = [path1, path2]
        labels = df['answer']

        self.image_paths = image_paths
        self.labels = labels
        self.transform = transform
        print('x')


    def __getitem__(self, index):
        path1 = self.image_paths[0]
        path2 = self.image_paths[1]

        #画像読み込み。
        img1 = Image.open(path1[index])
        img2 = Image.open(path2[index])

        print(path1[index], path2[index])
        #transform事前処理実施
        if self.transform is not None:
            img1 = self.transform(img1)
            img2 = self.transform(img2)
        label=self.labels[index]
        print(label)
        return img1,img2,label

    # def __getitem__(self, i: int):
    #     x1, t1 = super().__getitem__(i)
    #     r = np.random.randint(len(self))
    #     print('train ', r)
    #
    #     x2, t2 = super().__getitem__(r)
    #
    #     return x1, x2, (1.0 if t1 > t2 else 0.0 if t1 < t2 else 0.5)

    def __len__(self):
        #データ数を返す
        return len(self.image_paths)

if __name__ == '__main__':
    #transformで32x32画素に変換して、テンソル化。
    # transform = transforms.Compose([transforms.Resize((32,32)), transforms.ToTensor()])
    #データセット作成
    def transform(x):
        return np.expand_dims(np.asarray(x, dtype=np.float32), 0) / 255
    dataset = my_dataset("./data/train.csv",transform)
    print('a')
    #dataloader化
    dataloader = DataLoader(dataset, batch_size=4)
    print('b')

    #データローダの中身確認
    print(dataloader)
    # for img,label ,image_path in dataloader:
    #     print('label=',label)
    #     print('image_path=',image_path)
    #     print('img.shape=',img.shape)
