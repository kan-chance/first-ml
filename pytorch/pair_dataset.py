from torchvision.datasets import MNIST
import numpy as np
import csv


class MNISTPairDataset(MNIST):
    def __getitem__(self, i: int):
        x1, t1 = super().__getitem__(i)
        r = np.random.randint(len(self))
        x2, t2 = super().__getitem__(r)
        # print('train ', r)
        # with open('./') as f:
        #     reader = csv.reader(f)
        #     header = next(reader)


        x2, t2 = super().__getitem__(r)

        return x1, x2, (1.0 if t1 > t2 else 0.0 if t1 < t2 else 0.5)

    # def __init__(self):
    #     with open ('./train.csv') as f:
    #         reader = csv.reader(f)
    #         header = next(reader)
    #
    #         train_data_list = []
    #         train_label_list = []
    #
    #         for row in reader:
    #             tain_data_list.append([row[0], row[1]])
    #             train_label_list.append(row[2])
    #
    #     with open ('./test.csv') as f2:
    #         reader = csv.reader(f2)
    #         header = next(reader)
    #
    #         test_data_list = []
    #         test_label_list = []
    #
    #         for row in reader:
    #             test_data_list.append([row[0], row[1]])
    #             test_label_list.append(row[2])
    #
    #         self.train_data = train_data_list
    #         self.test_data = test_data_list
    #
    #         self.train_labels = train_label_list
    #         self.train_label_set = set(self.train_labels.numpy())
    #         self.label_to_indices = {label: np.where(self.train_labels.numpy() == label)[0]
    #                                  for label in self.train_label_set}
    #
    #         self.test_labels = test_label_list
    #         self.test_label_set = set(self.test_labels.numpy())
    #         self.label_to_indices = {label: np.where(self.test_labels.numpy() == label)[0]
    #                                  for label in self.test_label_set}
    #
    #
    #
    # def __getitem__(self, index):
    #     if self.train:
    #         target = np.random.randint(0, 2)
    #
    #         # img1,label1は先に決めてしまう
    #         img1, label1 = self.train_data[index], self.train_labels[index].item()
    #         if target == 1:
    #             # positive pair
    #             # ラベルが同じとなるindexを選んでくる処理
    #             siamese_index = index
    #             while siamese_index == index:
    #                 siamese_index = np.random.choice(self.label_to_indices[label1])
    #         else:
    #             # negative pair
    #             # labelが異なるindexを選んでくる処理
    #             siamese_label = np.random.choice(list(self.train_label_set - set([label1])))
    #             siamese_index = np.random.choice(self.label_to_indices[siamese_label])
    #
    #         img2 = self.train_data[siamese_index]
    #     else:
    #         img1 = self.test_data[self.test_pairs[index][0]]
    #         img2 = self.test_data[self.test_pairs[index][1]]
    #         target = self.test_pairs[index][2]
    #
    #     img1 = Image.fromarray(img1.numpy(), mode='L')
    #     img2 = Image.fromarray(img2.numpy(), mode='L')
    #     if self.transform:
    #         img1 = self.transform(img1)
    #         img2 = self.transform(img2)
    #
    #     return (img1, img2), target  # metric learningのラベルは同一か否か
    #
    # def __len__(self):
    #     return len(self.dataset)
    #
