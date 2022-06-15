unswnb15数据集信息

[toc]

# 数据集文件介绍

## 最全的数据集

以后应该就用这个数据集了吧.

```
UNSWNB_labelall_train_dataset.npz : 训练集
UNSWNB_labelall_test_dataset.npz : 测试集
```

字典关键词为:

```
data:数据部分,np数组,[batch,64]
label:按照0为正常,1为异常做的标签
attack_cat_label:按照各种攻击种类的编码做的标签.
attack_cat_examples:list,种类,也是按照这个顺序编的码['Analysis' 'Backdoor' 'DoS' 'Exploits' 'Fuzzers' 'Generic' 'Normal''Reconnaissance' 'Shellcode' 'Worms']
```

attact_cat_label的编码对应的顺序:

```
0  :  Analysis,1  :  Backdoor,2  :  DoS,3  :  Exploits,4  :  Fuzzers,5  :  Generic,6  :  Normal,7  :  Reconnaissance,8  :  Shellcode,9  :  Worms
```



# 之前做的二分类的数据集

特征[,64]
字典是label和data

```
UNSWNB_label01_train_dataset.npz : 所有训练集
UNSWNB_labelnormal_train_dataset.npz : 标签为normal即0 的训练集
UNSWNB_label01_test_dataset.npz : 所有测试集
```



# 攻击种类

训练集:
Normal            56000
Generic           40000
Exploits          33393
Fuzzers           18184
DoS               12264
Reconnaissance    10491
Analysis           2000
Backdoor           1746
Shellcode          1133
Worms               130
Name: attack_cat, dtype: int64

测试集:
Normal            37000
Generic           18871
Exploits          11132
Fuzzers            6062
DoS                4089
Reconnaissance     3496
Analysis            677
Backdoor            583
Shellcode           378
Worms                44
Name: attack_cat, dtype: int64