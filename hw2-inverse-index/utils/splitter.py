import jieba

class Splitter:
    
    def __init__(self, data_path='./model'):
        jieba.set_dictionary(data_path+'/dict.txt')

    def _set_user_dict(self, user_dict):
        jieba.load_userdict(user_dict)

    def split(self, sentences, user_dict=None):
        if user_dict:
            self._set_user_dict(user_dict)
        return jieba.cut(sentences)
