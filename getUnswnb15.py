import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

'''
readme:
这版本写的很好用.train_normal指的是训练集中所有label为normal的样本.
'''
df_test = pd.read_csv("../data/UNSWNB15/UNSW_NB15_training-set.csv")  # 82332
df_train = pd.read_csv("../data/UNSWNB15/UNSW_NB15_testing-set.csv")

# 获得各种攻击类型
attack_cat_train=df_train["attack_cat"]
attack_cat_test=df_test["attack_cat"]
attack_cat_examples=["Normal","Generic","Exploits","Fuzzers","DoS",
                 "Reconnaissance","Analysis","Backdoor","Shellcode","Worms"]
# print(attack_train.value_counts())
# print(attack_test.value_counts())

# print("proto有这么多种", df_train["proto"].value_counts().shape)  # proto 有133种,就不要了吧
# df_train=df_train.drop(df_train[df_train["label"]==1])
print(df_train["label"].value_counts())
df_train = df_train.drop(["label", "id"], axis=1)
df_test = df_test.drop(["label", "id"], axis=1)
list_train = []
list_test = []

def toLabel(df_train, df_test, onehot_encoder=False,examples=None):
    # print(df_train.shape,df_test.shape)#175341,) (82332,)\
    le = LabelEncoder()
    # LabelEncoder有个问题,那就是他编号的时候是按照类别在数据集出现的先后顺序编的号.我们要想按照自己的需求编号,
    # 可以把我们的类别写在examples里面,但是要写全哦
    if examples is None:
        df = pd.concat([df_train, df_test], axis=0)
        # print("df",df.shape)#(257673,)
        le.fit(df)
    else:
        print(f"按照我们写的顺序编号:{examples}")
        le.fit(examples)
    df_train = le.transform(df_train).reshape([-1, 1])
    df_test = le.transform(df_test).reshape([-1, 1])
    df = np.concatenate([df_train, df_test], axis=0)
    if onehot_encoder:
        ohe = OneHotEncoder()
        ohe.fit(df)
        df_train = ohe.transform(df_train).toarray()
        df_test = ohe.transform(df_test).toarray()
    # print("onehot:", df_train.shape, df_test.shape)
    '''
proto
onehot: (175341, 1) (82332, 1)
service
onehot: (175341, 13) (82332, 13)
state
onehot: (175341, 11) (82332, 11)
attack_cat
onehot: (175341, 10) (82332, 10)
    '''
    return df_train, df_test

#对数据集进行编码
for i in df_train.select_dtypes(include="object").columns:
    print(i)
    series_train = df_train[i]
    series_test = df_test[i]
    series_train, series_test = toLabel(series_train, series_test, True and i != "proto")
    list_train.append(series_train)  # z这个列表的结构是怎么样的,以后看,不用看了就是几个宽度不同的数组横向拼起来
    list_test.append(series_test)
# 对供给种类进行编码,不需要独热.
attack_cat_train,attack_cat_test=toLabel(attack_cat_train,attack_cat_test,
                         onehot_encoder=False,examples=attack_cat_examples)

# 出去attack_cat其他都要
categorical_train = np.concatenate(list_train[:-1], axis=1)
categorical_test = np.concatenate(list_test[:-1], axis=1)
# print(categorical_train.shape)

# 从attack_cat出发反onehot编码得到label,normal从6变成0,其他为1
label_train = list_train[-1]
label_test = list_test[-1]
# print(label_train[:10])
label_train = np.argmax(label_train, axis=1)  # 妙啊,用argmax将其从独热码转化为之前的标签码
label_test = np.argmax(label_test, axis=1)
label_train = np.where(label_train == 6, 0, 1)
label_test = np.where(label_test == 6, 0, 1)
# print(label_train[115930])#是1,成了

#删掉原始df里的object列
df_train=df_train.drop(df_train.select_dtypes(include="object").columns,axis=1).to_numpy()
df_test=df_test.drop(df_test.select_dtypes(include="object").columns,axis=1).to_numpy()
#得到处理好特征的数据
data_train=np.concatenate([df_train,categorical_train],axis=1)
data_test=np.concatenate([df_test,categorical_test],axis=1)
# print(data_train.shape,data_test.shape)#(175341, 64) (82332, 64)
# print(label_train.shape,label_test.shape)#(175341,) (82332,)
def double_sided_log(x):
    return np.sign(x) * np.log(1 + np.abs(x))
def sigmoid(x):
    return np.divide(1, (1 + np.exp(np.negative(x))))
#归一化(175341, 64) (82332, 64)
data_train=double_sided_log(sigmoid(data_train))
data_test=double_sided_log(sigmoid(data_test))

np.savez("./UNSWNB_labelall_train_dataset.npz",data=data_train,label=label_train,attack_cat_label=attack_cat_train,attack_cat_examples=attack_cat_examples)
np.savez("./UNSWNB_labelall_test_dataset.npz",data=data_test,label=label_test,attack_cat_label=attack_cat_test,attack_cat_examples=attack_cat_examples)

'''dataset_train=np.load("./UNSWNB_label01_train_dataset.npz")
x_train,y_train=dataset_train["data"],dataset_train["label"]
dataset_test=np.load("./UNSWNB_label01_test_dataset.npz")
x_test,y_test=dataset_test["data"],dataset_test["label"]
print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)'''

# np.savez("./UNSWNB_labelnormal_train_dataset.npz",data=data_normal,label=label_normal)