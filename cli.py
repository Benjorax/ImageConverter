import argparse
from converter import ImageConverter

def main():
    parser = argparse.ArgumentParser(description="Конвертер изображений")
    parser.add_argument("-i", "--input", required=True, help="Файл или папка для конвертации")
    parser.add_argument("-o", "--output", required=True, help="Выходной файл или папка")
    parser.add_argument("-f", "--format", help="Формат вывода (PNG, JPEG, BMP и т.д.)")
    args = parser.parse_args()

    converter = ImageConverter()

    import os
    if os.path.isfile(args.input):
        converter.convert(args.input, args.output, args.format)
    elif os.path.isdir(args.input):
        converter.batch_convert(args.input, args.output, args.format)
    else:
        print("Входной путь не найден")

if __name__ == "__main__":
    main()