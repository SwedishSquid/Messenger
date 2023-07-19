from model.data import singletons


def on_next_screen_button_action():
    singletons.get_screen_changer().goto_initial_screen()
    pass


def get_next_image():
    # self._file_num = (self._file_num + 1) % len(self._file_names)
    # try:
    #     self.img.source = self._file_names[self._file_num]
    #     self.img.reload()
    # except Exception as e:  # too laizy to search for kivy-image-exception
    #     print(e)
    print('make method get_next_image')
    pass
