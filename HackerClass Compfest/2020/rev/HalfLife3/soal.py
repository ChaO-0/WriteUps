(lambda x: print('Congratz, here is your flag: COMPFEST12{' + x + '}') if (lambda a: int((lambda b: ''.join([chr((ord(i)-97+1+(1^2))%26+97) for i in b]))(a), 36) if all([i in __import__('string').ascii_lowercase[-1:]+__import__('string').ascii_lowercase[:-1] for i in a]) else -1)(x) == 16166842727364078278681384436557013 else print(x))(input().lower())
