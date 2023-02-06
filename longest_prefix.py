def longest_common_prefix(strs):
    strs1 = min(map(lambda x: len(x), strs))
    ans = ""
    counter = 0
    while strs1:
        if all(x[counter] == strs[0][counter] for x in strs):
            ans = ans + strs[0][counter]
            counter = counter + 1
            strs1 = strs1 - 1
        else:
            return ans
    return ans


string1 = ["flower", "flow", "flourish"]

result = longest_common_prefix(string1)

print(result)
