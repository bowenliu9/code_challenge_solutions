# 2020 Q4
T1 = "ABCCDEABAA"
S1 = "ABCDE"
T2 = "ABCDDEBCAB"
S2 = "ABA"
T = T2
S = S2
flag = False
for index in range(len(S)):
    new_s = S[index::]+S[0:index]
    if new_s in T:
        print(new_s)
        print("yes")
        flag = True
if not flag:
    print("no")