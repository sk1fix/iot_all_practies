class SlugConverter():
    def __init__(self) -> None:
        self.file_name = input()
        self.slug_list = []
        self.run()

    def run(self):
        while (True):
            a = input()
            if not a:
                break
            self.slug_list.append(a)