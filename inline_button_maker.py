from telebot import types
def make_button(button):
        if button=="main_button":
            button=types.InlineKeyboardMarkup(row_width=3)
            button1=types.InlineKeyboardButton(text="🇺🇿Uz",callback_data="uz")
            button2=types.InlineKeyboardButton(text="🇬🇧Eng",callback_data="en")
            button3=types.InlineKeyboardButton(text="🇷🇺Ru",callback_data="ru")
            button4=types.InlineKeyboardButton(text="🇹🇯Tj",callback_data="tj")
            button5=types.InlineKeyboardButton(text="🇰🇬Kyrgyz",callback_data="ky")
            button6=types.InlineKeyboardButton(text="🇰🇿Kz",callback_data="kz")
            button7=types.InlineKeyboardButton(text="🇹🇷Turk",callback_data="turk")
            button8=types.InlineKeyboardButton(text="🇸🇦Arabic",callback_data="ar")
            button9=types.InlineKeyboardButton(text="🇩🇪German",callback_data="de")
            button10=types.InlineKeyboardButton(text="❌",callback_data="delete")
            button.add(button1, button2,button3,button4,button5,button6,button7,button8,button9,button10)
        elif button=="enter":
            button=types.InlineKeyboardMarkup(row_width=1)
            button1=types.InlineKeyboardButton(text="⬅️",callback_data="back")
            button.add(button1)
        elif button=="del":
            button=types.InlineKeyboardMarkup(row_width=2)
            button1=types.InlineKeyboardButton(text="❌",callback_data="delete")
            button2=types.InlineKeyboardButton(text="⬅️",callback_data="back")
            button.add(button1, button2)
            
   
        return button