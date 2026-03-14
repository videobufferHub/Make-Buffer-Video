import os

folder = "/storage/emulated/0/Download/MakeBufferVideo"
glitch = os.path.join(folder, "glitch.mp4")

if not os.path.exists(glitch):
    print("❌ glitch.mp4 is gone!")
    exit()

video = input("Enter your file name to create a video buffer: ")

if not os.path.exists(video):
    print("❌Your Video Not Found!")
    exit()

listfile = os.path.join(folder, "list.txt")

with open(listfile, "w") as f:
    f.write(f"file '{video}'\n")
    f.write(f"file '{glitch}'\n")

output = os.path.join(folder, "Results.mp4")

os.system(f'ffmpeg -f concat -safe 0 -i "{listfile}" -c copy "{output}"')

print("✅Your Video Buffer has been successfully created!")
