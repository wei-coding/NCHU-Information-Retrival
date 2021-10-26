from ckiptagger import construct_dictionary, WS
import os

class Splitter:
    
    def __init__(self, data_path='./model', cuda=True):
        self.USING_CUDA = cuda
        if cuda:
            self._enable_gpu()
        self.ws = None
        self._load_model(data_path)

    def _enable_gpu(self):
        os.environ['CUDA_ViSIBLE_DEVICES'] = '0'
        self.USING_CUDA = True

    def _load_model(self, path):
        self.ws = WS(path, disable_cuda=not self.USING_CUDA)

    def _set_user_dict(self, user_dict):
        """
        user_dict be like...
        {"中文字": 1, "其他詞": 2}
        eg. words to importance pairs
        """
        return construct_dictionary(user_dict)

    def split(self, sentences, user_dict=None):
        if user_dict:
            self._set_user_dict(user_dict)
        ws_list = self.ws(sentences)
        return ws_list
