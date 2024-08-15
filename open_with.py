class WordsFinder:
    file_names = []
    def __init__(self, *files):
        self.file_names = list(files)
    
    def get_all_words(self):
        all_words = {}
        signs = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
        for file_name in self.file_names:
            words = []
            with open(file_name) as file:
                for line in file:
                    line = str(line).lower()
                    for sign in signs:
                        str(line).replace(sign, "")
                    words.extend(line.split())   
            all_words[file_name] = words
            return all_words
    
    def find(self, word):
        dict = {}
        all_words = self.get_all_words().items()
        for key, value in all_words:
            if str(word).lower() in value:
                dict[key] = value.index(str(word).lower())+1
        return dict
    
    def count(self, word):
        dict = {}
        for key, value in self.get_all_words().items():
            if str(word).lower() in value:
                dict[key] = value.count(str(word).lower())
        return dict
        

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего