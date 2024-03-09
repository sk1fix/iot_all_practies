from commonUtils import CommonUtils


class SlugConverter(CommonUtils):
    def __init__(self) -> None:
        super().__init__()
        self.file_name = input()
        self.slug_list = []
        self.run()

    def run(self):
        while (True):
            a = input()
            if not a:
                break
            self.slug_list.append(a)
        CommonUtils.add_to_file(self.file_name, self.slug_list)
        