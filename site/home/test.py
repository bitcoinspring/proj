with open('whatever', 'r') as f:
    codes = f.read().splitlines()
    print codes
    code = codes[0]
    del codes[0]
    codes = '\n'.join(codes)
    f.close()

with open('whatever', 'w') as f:
    f.write(codes)
    f.close()
