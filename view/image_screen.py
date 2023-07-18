from kivy.uix.screenmanager import Screen
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager
import utility.screen_names as screen_names


class ImageScreen(Screen):
    _file_names = [
        'https://pyxis.nymag.com/v1/imgs/d6a/dc7/4a5001b7beea096457f480c8808572428b-09-roll-safe.2x.h473.w710.jpg',
        'https://e3.365dm.com/19/09/1600x900/skynews-drew-scanlon-blinking-white-guy_4786055.jpg?20190925134801',
        'https://www.dictionary.com/e/wp-content/uploads/2021/02/20210202_atw_stonks_800x800.png',
        'https://images.thewest.com.au/publication/C-9992102/bb298a7944c55200b3e1f9213186f4cc3b401ee7.jpg?imwidth=810&impolicy=wan_v3',
        'https://cdn.britannica.com/19/213119-050-C81C786D/Grumpy-Cat-2015-memes.jpg',
        'https://www.frontiersin.org/files/MyHome%20Article%20Library/547065/547065_Thumb_400.jpg',
        'https://www.viasport.ca/sites/default/files/Cover%20photo%20-%20cat.jpg',
        'https://assets-prd.ignimgs.com/2022/07/07/minecraft-memes-1657229425733.jpg?width=1280',
        'https://img.freepik.com/free-vector/funny-serious-cat-animal-meme_23-2148974916.jpg?w=2000',
        'https://napoleoncat.com/wp-content/uploads/2022/05/social-media-memes-emotional-damage-meme.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTB77abPQd9Wsl36LrqDVZklhrBWxo1JxlSLQ&usqp=CAU',
        'https://www.cnet.com/a/img/resize/35164dc21fa690bb0c22cfc2e2137563604de434/hub/2019/05/22/1b710a6b-5f4d-4987-a046-c23674b221a3/picard-meme-facepalm.jpg?auto=webp&fit=crop&height=1200&width=1200',
        'https://cloudfront-eu-central-1.images.arcpublishing.com/thenational/C4CGQVQGKRSRKHSOSX7HYVXON4.jpg',
        'https://teamhood.com/wp-content/uploads/2022/09/welcome-to-the-team-meme.png',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/WikiMeme_Dank.jpg/640px-WikiMeme_Dank.jpg',
        'https://static.displate.com/857x1200/displate/2022-07-07/fb201c5aef2a8558a1eec3a095be6d49_1c1023275f02c2ee7bc146309a812775.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmzg5X2nUc4XR8sqGsKSuQeL9VUvWgkEDtzw&usqp=CAU',
        'https://thechive.com/wp-content/uploads/2023/06/ThumbnailTemplateNEW-27.jpg?attachment_cache_bust=4417772&quality=85&strip=info&w=480&h=250&crop=1',
        'https://xwatch.vn/upload_images/images/2023/05/22/anh-meme-la-gi.jpg',
    ]

    def __init__(self, sm: ScreenManager, **kw):
        self.name = screen_names.image_screen_name
        self.sm = sm
        super().__init__(**kw)
        self._file_num = -1
        main_layout = BoxLayout(
            padding=[20, 20, 20, 20],
            spacing=40,
            orientation='vertical',
        )
        self.img = AsyncImage(
            source='fish_icon.png'
        )
        main_layout.add_widget(self.img)
        change_img_button = Button(
            text='change image',
            size_hint=(.5, .2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self._change_image
        )
        main_layout.add_widget(change_img_button)
        next_screen_button = Button(
            text='next screen',
            size_hint=(.5, .2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self._on_next_screen_button,
        )
        main_layout.add_widget(next_screen_button)
        self.add_widget(main_layout)

    def _change_image(self, instance):
        self._file_num = (self._file_num + 1) % len(self._file_names)
        try:
            self.img.source = self._file_names[self._file_num]
            self.img.reload()
        except Exception as e: # too laizy to search for kivy-image-exception
            print(e)
        pass

    def _on_next_screen_button(self, instance):
        self.sm.current = screen_names.initial_screen_name
