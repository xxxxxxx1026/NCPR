import json


class ConvHis():
    def __init__(self):
        self.user = None
        self.target_item = None
        self.asked_list = []
        self.candidate_list = []
        self.user_list = []
        self.convhis_vector = []

    def init_conv(self, user, target_item):
        self.convhis_vector.append(self.user_list)
        self.user_list = []
        self.user = user
        self.target_item = target_item
        # print("hhhhhhhhhhhhhhhhhhhhhhh")

    def update_asked_list(self, p):
        if p not in self.asked_list:
            self.asked_list.append(p)

    def update_candidate_list(self, item_list):
        self.candidate_list = item_list

    def update_user_list(self):
        tmp_dict = {
            'user':self.user,
            'item':self.target_item,
            'asked_list':self.asked_list,
            'candidate_list':self.candidate_list,
        }
        self.user_list.append(tmp_dict)

    def write_to_file(self):
        with open('./conhis.txt','w') as f:
            f.write(json.dumps(self.convhis_vector))
