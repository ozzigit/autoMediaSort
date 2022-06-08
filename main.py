#!/usr/bin/env python3
import argparse
import os
import re
import pathlib



def valid_target_dir(path):
    path = pathlib.Path(path)
    try:
        if path.is_dir():
            return path
    except OSError:
        raise argparse.ArgumentTypeError('%s is not a valid directory' % (path,))


def valid_result_dir(path):
    path = pathlib.Path(path)
    try:
        if path.is_dir():
            return path
        else:
            try:
                os.mkdir(path)
            except OSError:
                raise argparse.ArgumentTypeError('%s is not a valid directory' % (path,))
    except OSError:
        raise argparse.ArgumentTypeError('%s is not a valid directory' % (path,))


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--withMonth', choices={"y", "n", "Y", "N"}, default="y")
    parser.add_argument('-t', '--targetPath', type=valid_target_dir, help='folder to sort', default='.')
    parser.add_argument('-r', '--resultPath', type=valid_result_dir, help='folder to save', default=f'./test')
    return parser.parse_args()
    # print(parser.parse_args())

def gerenerate_file_mask():
    FileTypes = ('.jpg', '.mp4')



def generate_list_of_edit_files(directory: pathlib.Path):
    file_list = []  # A list for storing files existing in directories
    for x in directory.iterdir():
        if x.is_file() and x.name :
            file_list.append(x)
        # else:
        # file_list.append(searching_all_files(directory / x))
    return file_list


# Piress the green button in the gutter to run the script.
if __name__ == '__main__':
    args = init_args()
    generate_list_of_edit_files(pathlib.Path(args.targetPath))
    print(args.__dict__)
