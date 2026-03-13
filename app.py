import os

# Folder aplikasi
folder = "/storage/emulated/0/MakeBufferVideo"
os.makedirs(folder, exist_ok=True)

# Clip bawaan
glitch = os.path.join(folder, "glitch.mp4")

# Cek glitch.mp4
if not os.path.exists(glitch):
    print("❌ glitch.mp4 is missing!")
    exit()

# Video user
video = input("Enter the name of the file you want to use as a video buffer: ")
if not os.path.exists(video):
    print("❌file Not Found!")
    exit()

# Hasil gabungan
output = os.path.join(folder, "results.mp4")

# Buat list file untuk concat ffmpeg
list_file = os.path.join(folder, "list.txt")
with open(list_file, "w") as f:
    f.write(f"file '{video}'\n")   # video user di awal
    f.write(f"file '{glitch}'\n")  # glitch di akhir

# Gabung video dengan ffmpeg
os.system(f"ffmpeg -f concat -safe 0 -i {list_file} -c copy {output}")
print(f"✅ Video buffer successfully created!: {output}")
