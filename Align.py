from metric import Correct_Rate, Accuracy, Align
from jiwer import wer
import pandas as pd



#Align ref_our, human_our, ref_human

test = pd.read_csv("./test.csv")
f = open("./ref_human_detail", 'a')
cor_cnt = 0
sub_cnt = 0
ins_cnt = 0
del_cnt = 0
for i in range(len(test)):
    # f.write("000" + str(test['Path'][i]) + " ")
    path = test['Path'][i]
    path = str(path)
    seq1 = test['Canonical'][i]
    seq2 = test['Transcript'][i]
    seq1, seq2 = Align(seq1.split(" "), seq2.split(" "))
    REF = ''
    HYP = ''
    OP = ''
    cor = 0
    sub = 0
    ins = 0
    dell = 0
    for i in range(len(seq1)):
        REF = REF  + seq1[i] + " "
        HYP = HYP  + seq2[i] + " "
        if seq1[i]!="<eps>" and seq2[i]=="<eps>":
            OP = OP + "D" + " "
            dell = dell + 1
            del_cnt +=1
        elif seq1[i] == "<eps>" and seq2[i]!="<eps>" :
            OP = OP + "I" + " "
            ins = ins + 1
            ins_cnt+=1
        elif (seq1[i]!=seq2[i]) and seq2[i]!="<eps>" and seq1[i]!="<eps>":
            OP = OP + "S" + " "
            sub = sub + 1
            sub_cnt+=1
        else:
            OP = OP + "C" + " "
            cor = cor + 1
            cor_cnt+=1
    # print(REF)
    # print(HYP)
    # print(OP)
    cor = str(cor)
    sub = str(sub)
    ins = str(ins)
    dell = str(dell)
    
    # print(cor)
    # print(sub)
    # print(ins)
    # print(dell)
    f.write(path + " " + "ref" + " " + REF + "\n")
    f.write(path + " " + "hyp" + " " + HYP + "\n")
    f.write(path + " " + "op" + " " + OP + "\n")
    f.write(path + " " + "#csid" + " " + cor + " " + sub + " " + ins + " " + dell + "\n")

print(cor_cnt)
print(sub_cnt)
print(ins_cnt)
print(del_cnt)