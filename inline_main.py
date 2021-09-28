import telebot
import json
from datetime import datetime
from inline_button_maker import make_button
from admin_panel import admin_button, button_photo
from translate_function import translate
token="1782655438:AAF6Wztcp5pegHYQlIp5ai6hjRhT9qcjEtg"
bot=telebot.TeleBot(token,parse_mode="MARKDOWN")
admin="904185120"
#start_command
@bot.message_handler(commands=['start'])
def start(message):
    global main_button
    main_button=make_button("main_button")
    hozir=datetime.now().strftime('%Y-%m-%d %H:%M')
    user=message.from_user
    bot.send_message(message.chat.id,f"*🇺🇿Assalomu alaykum {format(user.first_name)}.\nTarjima uchun matn yuboring va kerakli tilni tanlang.Siz yuborgan matn shu tilga tarjima qilinadi▼\nBot buyruqlari👉/commands*",reply_markup=main_button)
    bot.send_message(admin,f"*/start bosildi.\n👤Foydalanuvchi:{format(user.first_name)}\n👤 Useri:\n@{format(user.username)}\n🆔 Foydalanuvchi id raqami:\n{message.chat.id}*")
#commands_command
@bot.message_handler(commands=['commands'])
def commands(message):
    bot.send_message(message.chat.id,"*/start - botni qayta ishga tushurish.\n/info - botdan foydalanish bo'yicha yo'riqnoma.\n/stat - bot statistikasi.*")   
#info_command
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id,"*Bu bot 9 ta til yo'nalishida matnlarni tarjima qila oladi.Buning uchun siz matn yuborishingiz va kerakli tilni tanlashingiz kerak,siz yuborgan matn o'sha tanlangan tilga tarjima qilinib, yuboriladi.Tarjima matnini unga bitta bosish orqali nusxalab olishingiz mumkin.*")
#stat_command
@bot.message_handler(commands=['stat'])
def stat(message):
                                                     hozir=datetime.now().strftime('%Y-%m-%d %H:%M')
                                                     with open("database/database.txt","r") as db:
                                                         r=db.readlines()
                                                         users=[d.rstrip() for d in r]
                                                     with open("database/count.txt","r") as count:
                                                         read=count.readlines()
                                                     bot.send_message(message.chat.id,f"*👥Bot foydalanuvchilari➙{len(users)} ta\n🕰️Hozirgi vaqt➙{hozir}\n✅Shu vaqtgacha qilingan tarjimalar soni➙{max(read)} ta*")
@bot.message_handler(commands=['status'])
def status(message):
        button=make_button("main_button")
        try:
            with open(f"user_info/{message.chat.id}.txt","r") as file:
                read=file.read()
                if read=="Uz":
                    response="Status - 🇺🇿Uz\n\nYuborilgan matn o'zbekchaga tarjima qilinadi.\n\nTanlang👇"
                elif read=="Eng":
                    response="Status - 🇬🇧Eng\n\nYuborilgan matn inglizchaga tarjima qilinadi.\n\nTanlang👇"
                elif read=="Ru":
                    response="Status - 🇷🇺Ru\n\nYuborilgan matn ruschaga tarjima qilinadi.\n\nTanlang👇"
                elif read=="Tj":
                    response="Status - 🇹🇯Tj\n\nYuborilgan matn tojikchaga tarjima qilinadi.\n\nTanlang👇"
                elif read=="Kyrgyz":
                    response="Status - 🇰🇬Kyrgyz\n\nYuborilgan matn qirg'iz tiliga tarjima qilinadi.\n\nTanlang👇"
                elif read=="Kz":
                    response="Status - 🇰🇿Kz\n\nYuborilgan matn qozoqchaga tarjima qilinadi.\n\nTanlang👇"
                elif read=="Turk":
                    response="Status - 🇹🇷Turk\n\nYuborilgan matn turkchaga tarjima qilinadi.\n\nTanlang👇"
                elif read=="Arabic":
                    response="Status - 🇸🇦Arabic\n\nYuborilgan matn arabchaga tarjima qilinadi.\n\nTanlang👇"
                elif read=="German":
                    response="Status - 🇩🇪German\n\nYuborilgan matn nemischaga tarjima qilinadi.\n\nTanlang👇"
                bot.send_message(message.chat.id,f"*{response}*",reply_markup=button)
        except:
            bot.send_message(message.chat.id,"Xatolik yuz berdi.")
@bot.message_handler(commands=["send"])
def send(message):
        global main_button
        main_button=admin_button("main_button")
        msg=message.text
        mid=message.chat.id
        if f"{mid}"==admin:
            request=bot.send_message(admin,"*Userlarga yuboriladigan kontentni tanlang👇*",reply_markup=main_button)
            bot.register_next_step_handler(request,admins)
def admins(message):
        blocked=[]
        with open("admin.txt","r") as file:
            read=file.read()
            if read=="oddiyxabar":
                with open("database/database.txt","r+") as data:
                            r=data.readlines()
                            users=[d.rstrip() for d in r]
                            for user in users:
                                    try:
                                        bot.send_message(user,f"*{message.text}*")
                                    except:
                                        blocked.append(user)
                                        continue
            elif read=="forward":
                 with open("database/database.txt","r+") as data:
                            r=data.readlines()
                            users=[d.rstrip() for d in r]
                            for user in users:
                                    try:
                                        bot.forward_message(user,admin,message.id)
                                
                                    except:
                                        blocked.append(user)
                                        continue
            elif read=="rassilka":
                match=""
                msg=message.text
                for i in msg:
                    if i!="+":
                        match+=i
                    else:
                        match+=i.replace(i," ")
                
                b=match.split()
                if len(b)==4:
                    photo=b[0]
                    caption=b[1]
                    button=button_photo(b[2],b[3])
                    with open("database/database.txt","r+") as data:
                                r=data.readlines()
                                users=[d.rstrip() for d in r]
                                for user in users:
                                        try:
                                            bot.send_photo(user,photo,f"*{caption}*",reply_markup=button)
                                        except:
                                            blocked.append(user)
                                            continue
                else:
                      bot.send_message(admin,f"*Ma'lumotlarda xatolik bor.*")
        if blocked:
             bot.send_message(admin,f"*{len(blocked)} ta userga yuborilmadi.*")
        else:
             bot.send_message(admin,f"*Barcha userlarga xabar yuborildi✅*")
                        
                        
@bot.message_handler(content_types=["text"])
def text(message):
    button=make_button("del")
    msg=message.text
    user=message.from_user
    mid=message.chat.id
    main_button=make_button("main_button")
    ##sending_action👇##
    bot.send_chat_action(mid,"typing")
    if len(msg)<400:
        try:
            with open(f"user_info/{mid}.txt","r") as file:
                read=file.read()
                if read=="Uz":
                    response=translate("Uz",msg)
                elif read=="Eng":
                    response=translate("Eng",msg)
                elif read=="Ru":
                    response=translate("Ru",msg)
                elif read=="Tj":
                    response=translate("Tj",msg)
                elif read=="Kyrgyz":
                    response=translate("Kyrgyz",msg)
                elif read=="Kz":
                    response=translate("Kz",msg)
                elif read=="Turk":
                    response=translate("Turk",msg)
                elif read=="Arabic":
                    response=translate("Arabic",msg)
                elif read=="German":
                    response=translate("German",msg)             
                bot.send_message(mid,f"`{response}`",reply_markup=button)
                with open("database/count.txt","r") as count:
                                r=count.readlines()
                                son=int(r[0])
                                a=son+1
                                a=str(a)
                                with open("database/count.txt","w") as count:
                                    count.write(a)
        except:
            bot.send_message(mid,"*Tilni tanlang👇*",reply_markup=main_button)
    else:
        bot.send_message(mid,"*Matn 400 belgidan oshmasligi kerak.❗*")
        
        
@bot.callback_query_handler(func=lambda call:True)
def answer(call):
        button1=make_button("enter")
        button_cancel=admin_button("cancel")
        try:
            if call.data=="uz":
                with open(f"user_info/{call.message.chat.id}.txt","w") as file:
                    file.write("Uz")
                bot.edit_message_text(f"*🇺🇿Uz\nMatn kiriting:*",call.message.chat.id,call.message.id,reply_markup=button1)
            elif call.data=="en":
                with open(f"user_info/{call.message.chat.id}.txt","w") as file:
                    file.write("Eng")
                bot.edit_message_text(f"*🇬🇧Eng\nMatn kiriting:*",call.message.chat.id,call.message.id,reply_markup=button1)
            elif call.data=="ru":
                with open(f"user_info/{call.message.chat.id}.txt","w") as file:
                    file.write("Ru")
                bot.edit_message_text(f"*🇷🇺Ru\nMatn kiriting:*",call.message.chat.id,call.message.id,reply_markup=button1)
            elif call.data=="tj":
                with open(f"user_info/{call.message.chat.id}.txt","w") as file:
                    file.write("Tj")
                bot.edit_message_text(f"*🇹🇯Tj\nMatn kiriting:*",call.message.chat.id,call.message.id,reply_markup=button1)
            elif call.data=="ky":
                with open(f"user_info/{call.message.chat.id}.txt","w") as file:
                    file.write("Kyrgyz")
                bot.edit_message_text(f"*🇰🇬Kyrgyz\nMatn kiriting:*",call.message.chat.id,call.message.id,reply_markup=button1)
            elif call.data=="kz":
                with open(f"user_info/{call.message.chat.id}.txt","w") as file:
                    file.write("Kz")
                bot.edit_message_text(f"*🇰🇿Kz\nMatn kiriting:*",call.message.chat.id,call.message.id,reply_markup=button1)
            elif call.data=="turk":
                with open(f"user_info/{call.message.chat.id}.txt","w") as file:
                    file.write("Turk")
                bot.edit_message_text(f"*🇹🇷Turk\nMatn kiriting:*",call.message.chat.id,call.message.id,reply_markup=button1)
            elif call.data=="ar":
                with open(f"user_info/{call.message.chat.id}.txt","w") as file:
                    file.write("Arabic")
                bot.edit_message_text(f"*🇸🇦Arabic\nMatn kiriting:*",call.message.chat.id,call.message.id,reply_markup=button1)
            elif call.data=="de":
                with open(f"user_info/{call.message.chat.id}.txt","w") as file:
                    file.write("German")
                bot.edit_message_text(f"*🇩🇪German\nMatn kiriting:*",call.message.chat.id,call.message.id,reply_markup=button1)   
            elif call.data=="back":
                try:
                    bot.edit_message_text("🏠*Asosiy menyu*",call.message.chat.id,call.message.id,reply_markup=main_button)
                except:
                    bot.send_message(call.message.chat.id,"🏠*Asosiy menyu*")
            elif call.data=="delete":
                bot.delete_message(call.message.chat.id,call.message.id)
                bot.delete_message(call.message.chat.id,call.message.id-1)
            
            elif call.data=="oddiyxabar":
                with open ("admin.txt","w") as file:
                    file.write("oddiyxabar")
                bot.edit_message_text(f"*Xabar yuboring:*",call.message.chat.id,call.message.id,reply_markup=button_cancel)
            elif call.data=="forwardxabar":
                with open ("admin.txt","w") as file:
                    file.write("forward")
                bot.edit_message_text(f"*Forward xabar yuboring:*",call.message.chat.id,call.message.id,reply_markup=button_cancel)
            elif call.data=="rassilka":
                with open ("admin.txt","w") as file:
                    file.write("rassilka")
                bot.edit_message_text(f"*Quyidagi formatda rassilka yuboring:\nrasm linki+rasm sarlavhasi+tugma nomi+tugma manzili*",call.message.chat.id,call.message.id,reply_markup=button_cancel)    
            elif call.data=="cancel":
                with open ("admin.txt","w") as file:
                    file.write("")
                bot.delete_message(call.message.chat.id,call.message.id)
                bot.send_message(call.message.chat.id,"*Bekor qilindi*")
            elif call.data=="back_admin":
                bot.edit_message_text("*Asosiy menyu*",call.message.chat.id,call.message.id, reply_markup=main_button)            
        except Exception as x:
             bot.send_message(call.message.chat.id,x)
        with open("database/database.txt","r+") as db:
                 mid=call.message.chat.id
                 r=db.readlines()
                 read=[d.rstrip() for d in r]
                 if f"{mid}" not in read:
                     db.write(f"{mid}\n")
             

        


bot.polling(none_stop=True)
    