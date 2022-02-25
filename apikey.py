def get():
    with open('api_key') as f:
        lines = f.readlines()
    return lines[0] if lines else None