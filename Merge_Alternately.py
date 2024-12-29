from itertools import zip_longest

def mergedAlternativelyVerbose1(word1, word2):
    pairs = list(zip_longest(word1,word2,fillvalue=''))
    print(f"Pairs : {pairs}")
    merged = []
    for a,b in pairs:
        if b:
            merged.append(a+b)
        else:
            merged.append(a)
    print(f"Merged step-by-step: {merged}")
    return "".join(merged)

def mergeAlternativelyVerbose2(word1,word2):
    merged = ''.join(a+b if b else a for a,b in zip_longest(word1,word2,fillvalue=""))
    return "".join(merged)

#Test
print(mergedAlternativelyVerbose1("abc","pqrxyz"))
print(mergeAlternativelyVerbose2("hiedfred",'bhuvi'))