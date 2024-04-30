from my_info import get_playlist, get_experience

with open('TEMPLATE.md') as file_in:
    text = file_in.read()

playlist = get_playlist()

if playlist:
    text = text.replace("/playlist", '\n'.join(get_playlist()))

text = text.replace("/experience", str(get_experience()))

with open("README.md", "w") as file_out:
    file_out.write(text)
