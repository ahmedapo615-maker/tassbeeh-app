import webbrowser
import arabic_reshaper
from bidi.algorithm import get_display

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

# ضبط لون خلفية التطبيق (داكن وأنيق)
Window.clearcolor = (0.12, 0.12, 0.18, 1)


def ar(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)


class TasbeehApp(App):

    def build(self):
        self.title = "تطبيق التسبيح والذكر"
        self.counter = 0

        # قائمة الأذكار
        self.azkar_raw = [
            "سُبْحَانَ اللَّهِ",
            "الْحَمْدُ لِلَّهِ",
            "لا إِلَهَ إِلا اللَّهُ",
            "اللَّهُ أَكْبَرُ",
            "لا حَوْلَ وَلا قُوَّةَ إِلا بِاللَّهِ",
            "أَسْتَغْفِرُ اللَّهَ وَأَتُوبُ إِلَيْهِ",
            "اللَّهُمَّ صَلِّ وَسَلِّمْ عَلَى نَبِيِّنَا مُحَمَّدٍ",
        ]

        # إعادة تشكيل الأذكار للغة العربية
        self.azkar_arabic = [ar(item) for item in self.azkar_raw]

        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=12)

        # 1. العنوان الرئيسي
        title_label = Label(
            text=ar("📿 الـسُّبْحَةُ الإِلِكْتُرُونِيَّةُ"),
            font_size="22sp",
            color=(0.97, 0.88, 0.68, 1),
            size_hint=(1, 0.12),
        )

        # 2. اختيار الذكر
        self.spinner = Spinner(
            text=self.azkar_arabic[0],
            values=self.azkar_arabic,
            font_size="18sp",
            size_hint=(1, 0.10),
        )

        # 3. شاشة العداد
        self.count_label = Label(
            text=str(self.counter),
            font_size="55sp",
            color=(0.65, 0.89, 0.63, 1),
            size_hint=(1, 0.30),
        )

        # 4. زر التسبيح
        btn_count = Button(
            text=ar("سَبِّحْ"),
            font_size="24sp",
            background_color=(0.53, 0.70, 0.98, 1),
            size_hint=(1, 0.16),
        )
        btn_count.bind(on_press=self.increment)

        # 5. زر إعادة الضبط
        btn_reset = Button(
            text=ar("إعادة ضبط"),
            font_size="16sp",
            background_color=(0.95, 0.54, 0.65, 1),
            size_hint=(1, 0.08),
        )
        btn_reset.bind(on_press=self.reset)

        # 6. عبارة نسألكم الدعاء
        dua_label = Label(
            text=ar("🤲 نسألكم الدعاء"),
            font_size="16sp",
            color=(0.95, 0.8, 0.5, 1),
            size_hint=(1, 0.08),
        )

        # 7. زر صفحة الفيسبوك
        btn_facebook = Button(
            text=ar("📘 صفحة المطور على فيسبوك"),
            font_size="14sp",
            background_color=(0.26, 0.40, 0.70, 1),
            size_hint=(1, 0.08),
        )
        btn_facebook.bind(on_press=self.open_facebook)

        # 8. اسم المطور
        dev_label = Label(
            text="Developed by: DR/Mohamed Elgamil",
            font_size="13sp",
            color=(0.8, 0.84, 0.95, 1),
            size_hint=(1, 0.08),
        )

        # إضافة العناصر بالترتيب
        main_layout.add_widget(title_label)
        main_layout.add_widget(self.spinner)
        main_layout.add_widget(self.count_label)
        main_layout.add_widget(btn_count)
        main_layout.add_widget(btn_reset)
        main_layout.add_widget(dua_label)
        main_layout.add_widget(btn_facebook)
        main_layout.add_widget(dev_label)

        return main_layout

    def increment(self, instance):
        self.counter += 1
        self.count_label.text = str(self.counter)

    def reset(self, instance):
        self.counter = 0
        self.count_label.text = str(self.counter)

    def open_facebook(self, instance):
        fb_url = "https://www.facebook.com/share/1DnLDLJH1Z/"
        webbrowser.open(fb_url)


if __name__ == "__main__":
    TasbeehApp().run()