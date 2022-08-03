first_string=input()
subsequence=input()
subseq_index=0
for char in first_string:
    if char==subsequence[subseq_index]:
        subseq_index += 1
        if subseq_index==len(subsequence):
            break
if subseq_index==len(subsequence):
    print("Yes")
else:
    print("No")