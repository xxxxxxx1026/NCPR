from RL.env_dialogue import DialogueEnv
from utils import *
from itertools import count
from RL_model import Agent,ReplayMemory
import argparse
from zlx_socket import ServerSocket
from EmotionalAnalysis.emotional_analysis import EmotionalAnalysis

class Server():
    #初始化模型和环境
    def __init__(self, server_socket):
        self.udp_server_socket = server_socket
        self.emotional_model = EmotionalAnalysis()

    def _welcome(self, name, addr):
        msg = f"welcome {name} join in !"
        self.udp_server_socket.udp_handle_send(addr, msg)

    def _pos_reply(self, name, addr):
        msg = f"{name}, 希望你能一直保持这种积极的态度！"
        self.udp_server_socket.udp_handle_send(addr, msg)

    def _neg_reply(self, name, addr):
        msg = f"{name}, 为什么这么消极呢？"
        self.udp_server_socket.udp_handle_send(addr, msg)

    def _mid_reply(self, name, addr):
        msg = f"抱歉{name},以我现在的能力还不能理解你说话的艺术。。。"
        self.udp_server_socket.udp_handle_send(addr, msg)

    def _user_leave(self, name, addr):
        pass

    def run(self):
        while True:
            raw_json, addr = self.udp_server_socket.listen()
            #代表新用户进入
            if raw_json['type'] == 1:
                self._welcome(raw_json['name'], addr)
            elif raw_json['type'] == 0:
                emotional_flag = self.emotional_model.get_score(raw_json['message'])['items'][0]['sentiment']
                if emotional_flag == 1:
                    self._mid_reply(raw_json['name'], addr)
                elif emotional_flag == 0:
                    self._neg_reply(raw_json['name'], addr)
                else:
                    self._pos_reply(raw_json['name'], addr)
            else:
                continue



if __name__ == '__main__':
    server_socket = ServerSocket(8888,'127.0.0.1', 'udp')
    model = Server(server_socket)
    model.run()
