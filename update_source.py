import argparse
import os
import shutil
from time import strftime, gmtime


def get_args():
    parser = argparse.ArgumentParser(description='Update the mod source files')
    parser.add_argument('source_dir', type=str, help='Directory of the mod where it has been updated')
    parser.add_argument('target_dir', type=str, help='Directory of the mod where the source will be updated')
    return parser.parse_args()


def list_file_to_copy(target_mod_dir):
    res = []
    for root, _, files in os.walk(target_mod_dir):
        for file in files:
            res.append(os.path.join(root, file))
    return res


def main(args):
    for file in list_file_to_copy(args.target_dir):
        source = file.replace(args.target_dir, args.source_dir)
        if os.path.exists(source):
            shutil.copyfile(source, file)
        else:
            print(f'{source} not found')


if __name__ == '__main__':
    main(get_args())
