# Compute a (simplified) Pig Latin version of a word.

###################################################
# Pig Latin formula
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    vowels = ["a","e","i","o","u"]
    if word[0] in vowels:
        return word+"way"
    else:
        return word[1:]+word[0]+"ay"
    
    # Student should complete function on the next lines.



###################################################
# Tests
# Student should not change this code.

def test(word):
    """Tests the pig_latin function."""
    
    print pig_latin(word)
    
test("pig")
test("owl")
test("python")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#igpay
#owlway
#ythonpay
