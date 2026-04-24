#################################
# Prepared by Muhammad Humayoun #
#################################
from sentiment import clean_text

def pprint(b):
    if b:
        return "Passed!"
    else:
        return "Failed!"

def test_clean_text():
    test = pprint(clean_text('') == [])
    print("Test 1: clean_text('') == []\t", test)
    
    test = pprint(clean_text('   ') == [])
    print("Test 2: clean_text('   ') == []\t", test)
    
    test = pprint(clean_text('This is a simple sentence') == ['this', 'is', 'a', 'simple', 'sentence'])
    print("Test 3: clean_text('This is a simple sentence') == ['this', 'is', 'a', 'simple', 'sentence']\t", test)
    
    test = pprint(clean_text('I told you!') == ['i', 'told', 'you'])
    print("Test 4: clean_text('I told you!') == ['i', 'told', 'you']\t", test)

    test = pprint(clean_text('The 10 little chicks') == ['the', 'little', 'chicks'])
    print("Test 5: clean_text('The 10 little chicks') == ['the', 'little', 'chicks']\t", test)

    test = pprint(clean_text('15th anniversary') == ['th', 'anniversary'])
    print("Test 6: clean_text('15th anniversary') == ['th', 'anniversary']\t", test)
    
    test = pprint(clean_text('He is in the room, she said.') == ['he', 'is', 'in', 'the', 'room', 'she', 'said'])
    print("Test 7: clean_text('He is in the room, she said.') == ['he', 'is', 'in', 'the', 'room', 'she', 'said']\t", test)

    test = pprint(clean_text('He earns in $$$.') == ['he', 'earns', 'in'])
    print("Test 8: clean_text('He earns in $$$.') == ['he', 'earns', 'in']\t", test)

    test = pprint(clean_text('12+12=24.') == [])
    print("Test 9: clean_text('12+12=24.') == []\t", test)

test_clean_text()