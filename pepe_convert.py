import argparse

from pepeline import read, save
import os
from tqdm.contrib.concurrent import process_map
from time import time


class Convert:
    def __init__(self):
        self.in_folder = ""
        self.out_folder = ""
        self.img_format = ""

    def __arg_parse(self) -> None:
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('-i', '--input', type=str,
                            help='Input_folder')
        parser.add_argument('-o', '--output', type=str,
                            help='Output_folder')
        parser.add_argument('-f', '--format', type=str,
                            help='Img out format')

        args = parser.parse_args()
        in_folder = args.input
        out_folder = args.output
        img_format = args.format if args.format else 'png'
        if not in_folder:
            in_folder = "INPUT"
        if not out_folder:
            out_folder = "OUTPUT"
        self.in_folder = in_folder
        self.out_folder = out_folder
        self.img_format = img_format
        if not os.path.exists(out_folder):
            os.makedirs(out_folder)
        if not os.path.exists(in_folder):
            raise print("no in folder")

    def convert(self, input_img: str):
        base_name = "".join(input_img.split(".")[:-1])
        out_folder = os.path.join(fr"{self.out_folder}/{base_name}.{self.img_format}")
        img = read(os.path.join(fr"{self.in_folder}/{input}"), 4)
        save(img, out_folder)

    def start_process(self):
        self.__arg_parse()
        list_image = [
            file
            for file in os.listdir(self.in_folder)
            if os.path.isfile(os.path.join(self.in_folder, file))
        ]
        start = time()
        process_map(self.convert, list_image)
        print(time() - start)


if __name__ == "__main__":
    Convert().start_process()
