import csv

class Map:
    def __init__(self) -> None:
        self.id = 0
        self.desc = ""
        self.name = ""
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0

map_loader_mgr = {}

def load_config(config_file):
    f = open(config_file, "r")
    reader = csv.reader(f)
    field_head = next(reader)
    type_head = next(reader)
    line_no = 0
    for row in reader:
        o = Map()
        o.id = int(row[0])
        pass
    f.close()


def test_csv():
    f = open("../csv/map.csv", "r")
    reader = csv.reader(f)
    field_head = next(reader)
    type_head = next(reader)
    line_no = 0
    print()
    for row in reader:
        print("{}:{}, {}:{}, {}:{}, {}:{}".format(field_head[0],row[0],field_head[1],row[1],field_head[2],row[2],field_head[3],row[3]))
    f.close()

if __name__ == "__main__":
    test_csv()
