import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# -------------------------------------------------

# Функция "Рекомендация космоса"

# -------------------------------------------------

class SpaceApp(App):

def recommendation(self, instance):

    secret = random.randint(1, 10)

    if secret == 1:
        f = 'Пора в отпуск, дорогуша!'
    elif secret == 2:
        f = 'Упасть, отжаться 10 раз!'
    elif secret == 3:
        f = 'Будь осторожен в общении с коллегами: один из них "подложит свинью"!'
    elif secret == 4:
        f = 'Позвони родственникам, они нуждаются в этом!'
    elif secret == 5:
        f = 'Наташа, займись делом, вымой полы!'
    elif secret == 6:
        f = 'В вашей профессиональной деятельности появится важный помощник!'
    elif secret == 7:
        f = 'Вам пора взглянуть по-новому на свое отношение к работе!'
    elif secret == 8:
        f = 'Подумай о драконах и единорогах (или, опять же, делом займись)'
    elif secret == 9:
        f = 'Неожиданное хобби поглотит вас в ближайшее время!'
    else:
        f = 'В ближайшее время стоит поклеить новые обои в детской'

    # Результат
    self.result.text = f

    # 2 и 5 — красным, остальные — тёмно-синим
    if secret == 2 or secret == 5:
        self.result.color = (1, 0, 0, 1)
    else:
        self.result.color = (0, 0, 0.5, 1)

# -------------------------------------------------
# Выход
# -------------------------------------------------

def exit_app(self, instance):
    self.stop()

# -------------------------------------------------
# Главное окно
# -------------------------------------------------

def build(self):

    layout = BoxLayout(
        orientation='vertical',
        padding=30,
        spacing=20
    )

    # Заголовок
    title = Label(
        text='Космос знает ответ...',
        font_size='24sp',
        color=(0, 0, 1, 1),
        size_hint=(1, 0.2)
    )

    layout.add_widget(title)

    # Результат
    self.result = Label(
        text='Жми, смелее...',
        font_size='20sp',
        color=(0, 0, 0.5, 1),
        halign='center',
        valign='middle',
        text_size=(0, None),
        size_hint=(1, 0.3)
    )

    layout.add_widget(self.result)

    # Кнопка рекомендации
    button_recommendation = Button(
        text='Рекомендация космоса',
        font_size='20sp',
        size_hint=(1, 0.2)
    )

    button_recommendation.bind(
        on_press=self.recommendation
    )

    layout.add_widget(button_recommendation)

    # Кнопка выхода
    button_exit = Button(
        text='Выход',
        font_size='20sp',
        size_hint=(1, 0.2)
    )

    button_exit.bind(
        on_press=self.exit_app
    )

    layout.add_widget(button_exit)

    return layout

# -------------------------------------------------

# Запуск программы

# -------------------------------------------------

if **name** == '**main**':
SpaceApp().run()
