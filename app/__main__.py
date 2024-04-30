from my_info import get_playlist, get_experience

with open('TEMPLATE.md') as file_in:
    text = file_in.read()

playlist = get_playlist()
experience, datetimenow = get_experience()

if playlist:
    text = text.replace("/playlist", '\n'.join(playlist))

text = text.replace("/experience", str(experience))
text = text.replace("/datetimenow", datetimenow)

with open("README.md", "w") as file_out:
    file_out.write(text)
