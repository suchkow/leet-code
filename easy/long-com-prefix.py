def longestCommonPrefix(strs: list) -> str:
    prefix = str()

    for i in zip(*strs): # where * unpacks list: [str0, str1, str2] -> str0, str1, str2
        if len(set(i)) == 1: # set removes dublicates; all letters same -> len() = 1
            prefix += i[0] # takes 1st value ih the tuple "i"
        else: 
            return prefix
    return prefix


case_1 = ["flower","flow","flight"]
case_2 = ["dog","racecar","car"]

print(longestCommonPrefix(case_1))