from PIL import Image
import argparse

# 解析参数
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", dest="file", help="输入文件")
parser.add_argument("-o", "--output", dest="output", help="输出文件")
parser.add_argument("--width", dest="width", type=int, default=80, help="输出图片宽")
parser.add_argument("--height", dest="height", type=int, default=80, help="输出图片高")
args = parser.parse_args()
print(args)
IMAGE = args.file
OUTPUT = args.output
WIDTH = args.width
HEIGHT = args.height

# 定义RGB图片对应的数字
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return " "
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    im = Image.open(IMAGE)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += "\n"
    print(txt)
    if OUTPUT:
        with open(OUTPUT, "w") as f:
            f.write(txt)
    else:
        with open("output.txt", "w") as f:
            f.write(txt)
