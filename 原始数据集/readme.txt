UNSW_NB15_testing-set.csv
UNSW_NB15_training-set.csv
这两个是官方文档

数据集有特点,label只有异常和正常(0和1),实际类别应该看attack_cat属性
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

Data columns (total 45 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   id                 82332 non-null  int64
 1   dur                82332 non-null  float64
 2   proto              82332 non-null  object
 3   service            82332 non-null  object
 4   state              82332 non-null  object
 5   spkts              82332 non-null  int64
 6   dpkts              82332 non-null  int64
 7   sbytes             82332 non-null  int64
 8   dbytes             82332 non-null  int64
 9   rate               82332 non-null  float64
 10  sttl               82332 non-null  int64
 11  dttl               82332 non-null  int64
 12  sload              82332 non-null  float64
 13  dload              82332 non-null  float64
 14  sloss              82332 non-null  int64
 15  dloss              82332 non-null  int64
 16  sinpkt             82332 non-null  float64
 17  dinpkt             82332 non-null  float64
 18  sjit               82332 non-null  float64
 19  djit               82332 non-null  float64
 20  swin               82332 non-null  int64
 21  stcpb              82332 non-null  int64
 22  dtcpb              82332 non-null  int64
 23  dwin               82332 non-null  int64
 24  tcprtt             82332 non-null  float64
 25  synack             82332 non-null  float64
 26  ackdat             82332 non-null  float64
 27  smean              82332 non-null  int64
 28  dmean              82332 non-null  int64
 29  trans_depth        82332 non-null  int64
 30  response_body_len  82332 non-null  int64
 31  ct_srv_src         82332 non-null  int64
 32  ct_state_ttl       82332 non-null  int64
 33  ct_dst_ltm         82332 non-null  int64
 34  ct_src_dport_ltm   82332 non-null  int64
 35  ct_dst_sport_ltm   82332 non-null  int64
 36  ct_dst_src_ltm     82332 non-null  int64
 37  is_ftp_login       82332 non-null  int64
 38  ct_ftp_cmd         82332 non-null  int64
 39  ct_flw_http_mthd   82332 non-null  int64
 40  ct_src_ltm         82332 non-null  int64
 41  ct_srv_dst         82332 non-null  int64
 42  is_sm_ips_ports    82332 non-null  int64
 43  attack_cat         82332 non-null  object
 44  label              82332 non-null  int64
dtypes: float64(11), int64(30), object(4)
memory usage: 28.3+ MB

进程已结束,退出代码0

