


from unidecode import unidecode


class CommonUtils():
    def __init__(self) -> None:
        pass
    
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
            f.write(CommonUtils.translit_to_eng(i))
            f.write('\n')  
