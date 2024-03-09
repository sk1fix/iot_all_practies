from slugConverter import SlugConverter


from unidecode import unidecode


class CommonUtils(SlugConverter):
    def __init__(self, file_name, slug_list) -> None:
        super().__init__(file_name, slug_list)
    
    @staticmethod
    def translit_to_eng(s):
        slag = ''
        for i in s:
            if i == ' ':
                slag += '-'
            else:
                slag += unidecode(i).lower()
        return slag
    

    @staticmethod
    def add_to_file(file_name, slug_list):
        f=open(file_name, "w")
        for i in slug_list:
            f.write(translit_to_eng(i))
