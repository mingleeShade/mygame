import csv
import sys,os

class FieldDesc:
    def __init__(self) -> None:
        self.name = ""
        self.type = "unknown type"

class ClassDesc:
    def __init__(self) -> None:
        self.name = ""
        self.field_list = []

def parse_header(field_str, type_str):
    field_list = field_str.split(",")
    type_str = type_str.split(",")

def read_csv(config_path):
    file = open(config_path, "r")
    line_num = 0
    field_str = file.readline()
    type_str = file.readline()
    file_name_ext = os.path.basename(config_path)
    file_name = os.path.splitext(file_name_ext)[0]
    parse_header(field_str, type_str)

def read_csvs(config_list, class_desc_list):
    for config in config_list:
        desc = ClassDesc()
        read_csv(config)

def main() -> int:
    config_list = []
    for path, dir_list, file_list in os.walk("csv"):
        #print("path: %s" %path)
        for file_name in file_list:
            #print(os.path.splitext(file_name)[-1])
            if os.path.splitext(file_name)[-1] != ".csv":
                continue
            full_path = os.path.join(path, file_name)
            print("full_path:%s"%full_path)
            config_list.append(full_path)

    class_desc_list = []
    read_csvs(config_list, class_desc_list)
    return 0

if __name__ == "__main__":
    sys.exit(main());
