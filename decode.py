import base64

MESSAGE = '''
F0YRHAIHDAAeRklWTEYFGwQFHVRBQU4PAw0ODAADHBZKQVNMSwQRHQQBBBYJRkVMSwQEDw4WHQBK QVNMSwgMChMBDRoPDQxLQEFFCAIMABYbBAQJAhVFSVtETgYDDQYPBwQGTk1ETgEMAwsFGBJFSVtE TgAMBwxLQEFFDw4LTlNXQU4bBQ9DThw=
'''

KEY = 'labiadismail'  # username

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print ''.join(result)

"""
credits : https://gist.github.com/jacquerie/cfb8a56636e2b9e12f51
"""
