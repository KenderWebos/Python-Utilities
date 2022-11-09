# print(open("input.txt", "r").read())

main_text = open("input.txt", "r")

for e in main_text.read().split():
    print(f'<li><a href="{e}" target="_blank"> Sunset_Mission </a></li>')

main_text.close()
input()