import numpy as np
train_dataset=np.load("UNSWNB_labelall_train_dataset.npz")
test_dataset=np.load("UNSWNB_labelall_test_dataset.npz")

train_x,train_y,train_attact_label,train_attack_examples=train_dataset["data"],train_dataset["label"],train_dataset["attack_cat_label"],train_dataset["attack_cat_examples"]
test_x,test_y,test_attact_label,test_attack_examples=test_dataset["data"],test_dataset["label"],test_dataset["attack_cat_label"],test_dataset["attack_cat_examples"]
print(train_x.shape,train_y.shape,train_attact_label.shape,train_attack_examples)
print(test_x.shape,test_y.shape,test_attact_label.shape,test_attack_examples)
print(train_y[:10],train_attact_label[:10])
print(train_attact_label[:20])
# print(train_attack_examples,test_attack_examples)
'''examples=np.unique(train_attack_examples)
print(examples[2])
np.savez("./UNSWNB_labelall_train_dataset.npz",data=train_x,label=train_y,attack_cat_label=train_attact_label,attack_cat_examples=examples)
np.savez("./UNSWNB_labelall_test_dataset.npz",data=test_x,label=test_y,attack_cat_label=test_attact_label,attack_cat_examples=examples)'''
print(train_attack_examples[train_attact_label[1]][0])