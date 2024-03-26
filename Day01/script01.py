# Find all permutations of a text field

def permutation(text):
    # base case
    if len(text) == 1:
        return text
    
    permu_tation = permutation(text[1:])
    first_char = text[0]
    mutations = []

    for mutation in permu_tation:
        for i in range(len(mutation)+ 1):
            mutations.append(mutation[:i] + first_char + mutation[i:])
    return mutations

text = "abc"
print(permutation(text))

# Output : ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
