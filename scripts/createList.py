import json
import ast


class CreateImageLabelList:
    def __init__(self, filename):
        self.filename = filename
        fid = open(self.filename, "r")
        self.json_dict = json.load(fid)

    def create_dataset(self, grp):
        image_list = []
        label_list = []
        image_label_list = self.json_dict[grp]
        for _ in image_label_list:
            image_list.append(_["image"])
            label_list.append(_["label"])
        return image_list, label_list


class CreateImagefromJson:
    def __init__(self, J):
        self.list = J

    def create_dataset(self):
        image_list = []
        if isinstance(self.list, dict):
            self.list = [self.list]
        for _ in self.list:
            image_list.append(_["image"])
        return image_list