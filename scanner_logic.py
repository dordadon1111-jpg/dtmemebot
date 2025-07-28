
def analyze_token(token):
    return token.get("volume", 0) > 500 and token.get("hype", False)
