def split_with_length(str, length):
    split_list = []
    ele = ""
    for i in range(len(str)):
        ele += str[i]
        if ((i+1) % length) == 0:
            split_list.append(ele)
            ele = ""
    
    if ele != "": split_list.append(ele)
    return split_list

def get_rank_list(sub_list):
    rank_list = []
    old_list = sub_list.copy()
    sub_list.sort()
    for i in old_list:
        rank_list.append(sub_list.index(i))
    return rank_list

def substi_list(split_list, rank_list):
    substied_list = []
    substied_ele = ""
    for section in split_list:
        for i in range(len(section)):
            substied_ele += section[rank_list[i]]
        substied_list.append(substied_ele)
        substied_ele = ""
    return substied_list

def print_enc_text(substied_list):
    result = ""
    for i in range(len(substied_list[0])):
        for j in range (len(substied_list)):
            result += substied_list[j][i]
    print("enc_text:",result)

# plaintext = input("input plaintext: \n").replace(" ","")
# key = input("input key: \n").replace(" ","")

plaintext = "attackbeginsatfive"
key = "cipher"

length = len(key)
print("substitute length == ", length)

split_list = split_with_length(plaintext, length)
sub_list = [ord(i) for i in key]
rank_list = get_rank_list(sub_list)
substied_list = substi_list(split_list, rank_list)

print(split_list)
print(sub_list)
print(rank_list)
print(substied_list)
print_enc_text(substied_list)
