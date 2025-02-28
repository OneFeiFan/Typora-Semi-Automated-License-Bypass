# -*- coding:utf-8 -*-
import argparse
from os import path

from loguru import logger as log


def modify_file(file_path):
    # 需要查找的特征字节
    target_patterns = [
        (bytearray([0x21, 0x64, 0x6F, 0x63, 0x75, 0x6D, 0x65, 0x6E, 0x74, 0x2E,
                    0x71, 0x75, 0x65, 0x72, 0x79, 0x53, 0x65, 0x6C, 0x65, 0x63,
                    0x74, 0x6F, 0x72]), b'\x20'),
        (bytearray([0x05, 0x01, 0x1C, 0x52, 0x65, 0x2E, 0x60, 0x66, 0xC8,
                    0x0F]), b'\x00')
    ]

    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        modified = False
        for pattern, replacement in target_patterns:
            index = data.find(pattern)
            if index != -1:
                data = data[:index] + replacement + data[index + 1:]
                modified = True

        if modified:
            # 创建备份文件
            backup_path = file_path + ".bak"
            import shutil
            shutil.copyfile(file_path, backup_path)
            log.info(f"Original file backed up to: {backup_path}")

            # 写入修改后的内容
            with open(file_path, 'wb') as f:
                f.write(data)
            log.success("File modified successfully.")
        else:
            log.warning("Pattern not found in the file.")

    except FileNotFoundError:
        log.error(f"File not found: {file_path}")
    except Exception as e:
        log.error(f"An error occurred: {e}")


def main():
    argParser = argparse.ArgumentParser(
        description="[extract and decryption / pack and encryption] app.asar file from [Typora].",
        epilog="If you have any questions, please contact [ MasonShi@88.com ]")
    argParser.add_argument("asarPath", type=str, help="app.asar file path/dir [input/ouput]")

    args = argParser.parse_args()

    # 检查文件是否存在
    if not path.isfile(args.asarPath):
        log.error(f"The provided path is not a valid file: {args.asarPath}")
        return

    # 直接调用 modify_file
    modify_file(args.asarPath)


if __name__ == '__main__':
    main()
