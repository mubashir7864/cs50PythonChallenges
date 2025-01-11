# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
imagefile = ["gif","jpg","jpeg","png"]

inp = input("give me a file: ").lower()

filename,extension = inp.split(".",1)

if extension in imagefile:
    print(f"image/{extension}")
elif extension == "pdf" or extension == "txt":
    print(f"document/{extension}")
elif extension == "zip":
    print(f"file is zip format")
else:
    print("give a correct file")