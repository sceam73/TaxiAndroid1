from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from plyer import vibrator
import logging

import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials






global fs
global x
x=35


adresF = 1

CREDENTALS_FILE = "./creds.json"

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

global spreadsheet_id
spreadsheet_id='1l1ykdDkwBDPAx8fH4RTNJK5UKD2K08jTnq2OapjljA0'

CarNo=1
DriverName=1
Bort=1
Bolt=1
BoltCash=1
OnTaxi=1
Taxi3000=1
Uklon=1
Taxi3040=1
Taxi838=1
Taxi838Rent=1
Lubimoe=1
Gas=1
Fuel=1
Distance=1
Tea=1

to_base = {"DriverName": "",
           "CarNo": "",
           "Bort": "",
            "Bolt": "",
            "BoltCash": "",
            "OnTaxi": "",
            "Taxi3000": "",
            "Uklon": "",
            "Taxi3040": "",
            "Taxi838": "",
            "Taxi838Rent": "",
            "Lubimoe": "",
            "Gas": "",
            "Fuel": "",
            "Distance": "",
            "Tea": "" }





class MyApp(App):
    def __init__(self):
        super().__init__()
        global steep
        global fs
        steep = 0
        window_sizes = Window.size
        self.size_x, self.size_y = window_sizes
        print(self.size_x, self.size_y)






        fs=self.size_y/x

        self.Blabel0 = Label(text='', font_size=fs)
        self.Blabel1 = Label(text='Приветствую на пересменке', font_size=fs)
        self.Blabel2 = Label(text='для проверки соединения', font_size=fs)
        self.Blabel3 = Label(text='нажми кнопку', font_size=fs)
        self.Blabel4 = Label(text='', font_size=fs)
        self.Blabel5 = Label(text='', font_size=fs)


        self.label0 = Label(text='', font_size=fs)
        self.label1 = Label(text='', font_size=fs)
        self.label2 = Label(text='',font_size =fs)
        self.label3 = Label(text='', font_size=fs)
        self.label4 = Label(text='', font_size=fs)
        self.label5 = Label(text='', font_size=fs)
        self.label6 = Label(text='', font_size=fs)
        self.label7 = Label(text='', font_size=fs)
        self.label8 = Label(text='', font_size=fs)
        self.label9 = Label(text='', font_size=fs)
        self.label10 = Label(text='', font_size=fs)
        self.label11 = Label(text='', font_size=fs)
        self.label12 = Label(text='', font_size=fs)
        self.label13 = Label(text='', font_size=fs)
        self.label14 = Label(text='', font_size=fs)
        self.label15 = Label(text='', font_size=fs)
        self.label16 = Label(text='', font_size=fs)


        self.input_data = TextInput(hint_text="", multiline=False,font_size=fs,background_color=[0,0,0,1])
        self.button1 = Button(text="Проверить",on_press=self.btn_pressed,font_size=fs)
        self.button2 = Button(text='сброс', on_press=self.btn_reset, font_size=fs)

    def vibrate(self,instance):
        try:
            vibrator.vibrate(0.1)
        except:
            pass

    def btn_reset(self,*args):
        global x
        self.vibrate
        window_sizes = Window.size
        self.size_x, self.size_y = window_sizes
        print(self.size_x, self.size_y)
        global fs
        fs = self.size_y / x

        global steep
        steep=0
        self.Blabel0.text = ""
        self.Blabel1.text = 'Приветствую на пересменке'
        self.Blabel2.text = 'для проверки соединения'
        self.Blabel3.text = 'нажми кнопку'
        self.Blabel4.text = ""
        self.Blabel5.text = ''

        self.label0.text = ""
        self.label1.text= ''
        self.label2.text= ''
        self.label3.text = ''
        self.label4.text = ""
        self.label5.text = ''
        self.label6.text = ''
        self.label7.text = ''
        self.label8.text = ''
        self.label9.text = ''
        self.label10.text = ''
        self.label11.text = ''
        self.label12.text = ''
        self.label13.text = ''
        self.label14.text = ''
        self.label15.text = ''
        self.input_data.hint_text=''
        self.input_data.text=""
        self.button1.text = "Проверить"

        self.label0.font_size = fs
        self.label1.font_size = fs
        self.label2.font_size = fs
        self.label3.font_size = fs
        self.label4.font_size = fs
        self.label5.font_size = fs
        self.label6.font_size = fs
        self.label7.font_size = fs
        self.label8.font_size = fs
        self.label9.font_size = fs
        self.label10.font_size = fs
        self.label11.font_size = fs
        self.label12.font_size = fs
        self.label13.font_size = fs
        self.label14.font_size = fs
        self.label15.font_size = fs
        self.button1.font_size = fs
        self.button2.font_size = fs

        self.input_data.background_color = [0, 0, 0, 1]


    def btn_pressed(self,*args):
        self.vibrate



        global CarNo
        global DriverName
        global Bort
        global Bolt
        global BoltCash
        global OnTaxi
        global Taxi3000
        global Uklon
        global Taxi3040
        global Taxi838
        global Taxi838Rent
        global Lubimoe
        global Gas
        global Fuel
        global Distance
        global Tea
        global steep
        global fs
        global spreadsheet_id
        print(str(steep))
        try:
           vibrator.vibrate(0.1)
        except:
            pass
        if steep==0:
           try:


               values = service.spreadsheets().values().get(
                   spreadsheetId=spreadsheet_id,

                   range="A1:B2",
                   majorDimension="ROWS"
               ).execute()

               spisok = values["values"]
               buffer = spisok[0]
               linenumber = buffer[0]
               if int(linenumber)>0:
                  self.Blabel0.text = ""
                  self.Blabel1.text = "Связть установлена"
                  self.Blabel2.text = ""
                  self.button1.font_size = fs/1.5
                  self.button1.text= "Начать пересменку"
                  self.input_data.text = ""
                  steep=1




               else:
                  self.Blabel0.text = ""
                  self.Blabel1.text = "Связть отсутствует"
                  self.Blabel2.text = ""
           except Exception as e:
               logging.error("fatal",exc_info=True)
               self.Blabel0.text = ""
               self.Blabel1.text = "Связть отсутствует"
               self.Blabel2.text = ""
        if steep==1:
            self.input_data.background_color= [0,0,0,1]
            self.Blabel0.text = ""
            self.Blabel1.text = "Связть установлена"
            self.Blabel2.text = ""
            self.button1.font_size = fs / 1.5
            self.button1.text = "Начать пересменку"
            steep = 2
            self.input_data.text = ""
            return
        if steep==2:
            self.input_data.background_color= [1,1,1,1]
            self.Blabel0.text = ""
            self.Blabel1.text = "Введи номер машины"
            self.Blabel3.text = "Без букв и символов"
            self.input_data.hint_text='1212'
            self.button1.font_size = fs
            self.button1.text = "Продолжить"

            steep = steep + 1
            self.input_data.text = ""
        if steep==3:
           CarNo=self.input_data.text
           try:
             int(CarNo)

             ## суда добавляем машины, по образу и подобию предыдущих
             if CarNo == 1715:
                 spreadsheet_id = '1ys9YJtc4Lbuszo6npcmKAIULxza5L9O_esmpuorlj4s'
             if CarNo == 4218:
                 spreadsheet_id = '1Du-Ne1-EWyYbddEqLfC0dxiAN-mzKAoaHd2zQiOgZdw'
             if CarNo == 5598:
                 spreadsheet_id = '1V4Xv0MbdUbizKZ9pao7V9Gf6eNNLTicWnAeIzk-kMrE'
             if CarNo == 3381:
                 spreadsheet_id = '1ttnXa9VrmHK2XcqDf3T8TmWHRLvyUJ2tDPvAznoNJw8'
             if CarNo == 1713:
                 spreadsheet_id = '1NcnLv12mAiSoXgXxJyrcIZErE7uo1A5yQTDbQOxEIDk'
             if CarNo == 8364:
                 spreadsheet_id = '1n3v468YjMuXRpHLcZn4iJMtCaYFwm2uSB-TqOrYJWQw'
             if CarNo == 8990:
                 spreadsheet_id = '1JtKsfNO7PVIvlYoqOiLvwyw3I2J5H8vrjBqaLaBuIdI'
             if CarNo == 8527:
                 spreadsheet_id = '1nfzX7KYlqhO7rW7HONKNJ9-2YyRKqnBguLZM3my-Qqo'
             if CarNo == 3957:
                 spreadsheet_id = '1l7lYdRKcANT3JHoik3Iq8EpCeclnXMjUzTfhFoEclnE'
             if CarNo == 9972:
                 spreadsheet_id = '1lGQ-j35ntMuA7ruMyW8-QuGMVHVNEfzjeMJ1rJ-iC1g'
             if CarNo == 2705:
                 spreadsheet_id = '1lurfzjxa_HIu8RwXPnOzRTVmuzpSjpCHtaIqZd8lENc'
             if CarNo == 4264:
                 spreadsheet_id = '176oW5jpGPI_s_wXMjC_c1pHAIEI1AmlixytmNsvzw2I'
             if CarNo == 9278:
                 spreadsheet_id = '1NAnpIYh16ZakXeeQH9p4UbDwJYxrw1zFHgTThX8xRlQ'
             if CarNo == 7080:
                 spreadsheet_id = '1v_DX9S8J4dGvvmeleAhfJW5wZgxk8YQG9XrOXQBQDQA'
             if CarNo == 2760:
                 spreadsheet_id = '1EEeWeRTSUYDJJbwBfR6vAuHVDhgELylVH77PvaHg_jI'
             if CarNo == str('0543'):
                 spreadsheet_id = '1eCxOeHxKS1Oomj9N1yXbnQL97h4Yi7lJiFOTD8HJFOQ'
             if CarNo == 9052:
                 spreadsheet_id = '1g70ipf-oEJ_UV0eLDfcDaQC5P6BxVeb2LgpHvOruegY'
             if CarNo == 8987:
                 spreadsheet_id = '1R8LM93hqoiHdlztsi25gXnxmDrivmJ-Y3vbGXpH3hAk'
             if CarNo == 5810:
                 spreadsheet_id = '1gbU5YkZKi9HtWc9nFlTUtTRZjF1i8vRGuu8ErAPVbYQ'
             if CarNo == 3519:
                 spreadsheet_id = '1QtPLnXNrSLoWHtmwbxe7Mwi-0x7GJMmA58YpujbGFEE'
             if CarNo == 8049:
                 spreadsheet_id = '1Rt1sWm-eo-Asa1puCYAlgZEL5f-dq3XWfO7U42gIFlE'
             if CarNo == 9588:
                 spreadsheet_id = '1llHmvpXWjhrstci-xTiLb0lmq0IYGwWVAVMaZqp9op4'
             if CarNo == 9892:
                 spreadsheet_id = '1nq6-H9PrDw1bJG2cVPQpofhEJcUzJQQSqHMxYG-FBs8'
             if CarNo == 3101:
                 spreadsheet_id = '1t1a2q93fxP1s0UfCAf7CitSESKGwDkjlU7i8c1SJ0NI'

             steep=steep+1
             self.Blabel1.text="Введи сегодняшнее число"

             self.input_data.hint_text = "11"
             self.input_data.text=""
           except:
             self.input_data.text=""
        if steep==4:
            DriverName = self.input_data.text

            try:

                int(DriverName)


                steep = steep + 1
                self.Blabel1.text = "Введи сегодняшние борты"

                self.input_data.hint_text = "111"
                self.input_data.text = ""
            except:
                self.input_data.text = ""
        if steep==5:
            Bort = self.input_data.text
            try:
                int(Bort)


                steep = steep + 1
                self.Blabel1.text = "Введи Общую кассу болт"

                self.input_data.hint_text = "1121"
                self.input_data.text = ""
            except:
                self.input_data.text = ""
        if steep == 6:
            Bolt = self.input_data.text
            try:
                int(Bolt)

                steep = steep + 1
                self.Blabel1.text = "Введи наличку болт"

                self.input_data.hint_text = "1121"
                self.input_data.text = ""
            except:
                self.input_data.text = ""
        if steep == 7:
            BoltCash = self.input_data.text
            try:
                int(BoltCash)

                steep = steep + 1
                self.Blabel1.text = "Введи общую кассу OnTaxi"

                self.input_data.hint_text = "1121"
                self.input_data.text = ""
            except:
                self.input_data.text = ""
        if steep == 8:
            OnTaxi = self.input_data.text
            try:
                int(OnTaxi)

                steep = steep + 1
                self.Blabel1.text = "Введи общую кассу Taxi3000"

                self.input_data.hint_text = "1121"
                self.input_data.text = ""
            except:
                self.input_data.text = ""
        if steep == 9:
            Taxi3000 = self.input_data.text
            try:
                int(Taxi3000)

                steep = steep + 1
                self.Blabel1.text = "Введи общую кассу Uklon"

                self.input_data.hint_text = "1121"
                self.input_data.text = ""
            except:
                self.input_data.text = ""
        if steep == 10:
            Uklon = self.input_data.text
            try:
                int(Uklon)

                steep = steep + 1
                self.Blabel1.text = "Введи общую кассу 3040"

                self.input_data.hint_text = "1121"
                self.input_data.text = ""
            except:
                self.input_data.text = ""
        if steep == 11:
            Taxi3040 = self.input_data.text
            try:
                int(Taxi3040)

                steep = steep + 1
                self.Blabel1.text = "Введи общую кассу 838"

                self.input_data.hint_text = "1121"
                self.input_data.text = ""
            except:
                self.input_data.text = ""
        if steep == 12:
            Taxi838 = self.input_data.text
            try:
                int(Taxi838)

                steep = steep + 1
                self.Blabel1.text = "Введи комиссию 838"

                self.input_data.hint_text = "1121"
                self.input_data.text = ""
            except:
                self.input_data.text = ""
        if steep == 13:
            Taxi838Rent = self.input_data.text
            try:
                int(Taxi838Rent)

                steep = steep + 1
                self.Blabel1.text = "Введи общую кассу Любимое"

                self.input_data.hint_text = "1121"
                self.input_data.text = ""
            except:
                self.input_data.text = ""
        if steep == 14:
            Lubimoe = self.input_data.text
            try:
                int(Lubimoe)

                steep = steep + 1
                self.Blabel1.text = "Введи суточную заправку газа"

                self.input_data.hint_text = "1121"
                self.input_data.text = ""
            except:
                self.input_data.text = ""
        if steep == 15:
            Gas = self.input_data.text
            try:
                int(Gas)

                steep = steep + 1
                self.Blabel1.text = "Введи суточную заправку бензина"

                self.input_data.hint_text = "1121"
                self.input_data.text = ""
            except:
                self.input_data.text = ""
        if steep == 16:
            Fuel = self.input_data.text
            try:
                int(Fuel)

                steep = steep + 1
                self.Blabel1.text = "Введи суточный пробег"

                self.input_data.hint_text = "1121"
                self.input_data.text = ""
            except:
                self.input_data.text = ""
        if steep == 17:
            Distance = self.input_data.text
            try:
                int(Distance)

                steep = steep + 1
                self.Blabel1.text = "Введи чаевые Bolt (безнал)"

                self.input_data.hint_text = "1121"
                self.input_data.text = ""
            except:
                self.input_data.text = ""
        if steep == 18:
            Tea = self.input_data.text
            try:
                int(Tea)
                self.Blabel0.text = ''
                self.Blabel1.text = ''
                self.Blabel2.text = ''
                self.Blabel3.text = ""
                self.Blabel4.text = ""
                self.Blabel5.text = ''

                self.label0.text = ''
                self.label1.text = ''
                self.label2.text = ''
                self.label3.text = ''
                self.label4.text = ''
                self.label5.text = ''
                self.label6.text = ''
                self.label7.text = ''
                self.label8.text = ''
                self.label9.text = ''
                self.label10.text = ''
                self.label11.text = ''
                self.label12.text = ''
                self.label13.text = ''
                self.label14.text = ''
                self.label15.text = ''
                self.input_data.background_color = [0, 0, 0, 1]



                steep = steep + 1
                self.label0.text = "номерa:" + str(CarNo)
                self.label1.text = "дата:"+str(DriverName)
                self.label2.text = "борт:"+str(Bort)
                self.label3.text = "Bolt:"+str(Bolt)
                self.label4.text = "Bolt нал:"+str(BoltCash)
                self.label5.text = "Bolt чай:"+str(Tea)
                self.label6.text = 'OnTaxi:'+str(OnTaxi)
                self.label7.text = 'Taxi3000:'+str(Taxi3000)
                self.label8.text = 'Uklon:'+str(Uklon)
                self.label9.text = 'Taxi3040:'+str(Taxi3040)
                self.label10.text = 'Taxi838:'+str(Taxi838)
                self.label11.text = 'комиссия 838:'+str(Taxi838Rent)
                self.label12.text = 'любимое:'+str(Lubimoe)
                self.label13.text = 'газ:'+str(Gas)
                self.label14.text = 'бензин:'+str(Fuel)
                self.label15.text = 'пробег'+str(Distance)
                self.button1.font_size = fs / 1.5
                self.button1.text = "Жми если все правильно"
                self.input_data.hint_text = ""
                self.input_data.text = ""
                return
            except:

                self.input_data.text = ""
        if steep == 19:
            self.label0.text = ""
            self.label1.text = ""
            self.label2.text = ""
            self.label3.text = ""
            self.label4.text = ""
            self.label5.text = ""
            self.label6.text = ''
            self.label7.text = ''
            self.label8.text = ''
            self.label9.text = ''
            self.label10.text = ''
            self.label11.text = ''
            self.label12.text = ''
            self.label13.text = ''
            self.label14.text = ''
            self.label15.text = ''

            try:
                ChangeString = [DriverName, CarNo, Bort, Bolt, BoltCash, OnTaxi, Taxi3000, Uklon, Taxi3040, Taxi838,
                                Taxi838Rent, Lubimoe, Gas, Fuel, Distance, Tea]

                values = service.spreadsheets().values().get(
                    spreadsheetId=spreadsheet_id,

                    range="A1:B2",
                    majorDimension="ROWS"
                ).execute()

                spisok = values["values"]
                buffer = spisok[0]
                linenumber = buffer[0]  ###вытаскиваем значение из словаря для определения заполнености таблицы

                adresF = int(linenumber) + 2
                adresFstr = "C" + str(adresF)

                adresL = adresF + 1
                adresLstr = "R" + str(adresL)
                myrange = adresFstr + ":" + adresLstr  # делаем значение типа str для myrange

                values = service.spreadsheets().values().batchUpdate(
                    spreadsheetId=spreadsheet_id,
                    body={
                        "valueInputOption": "USER_ENTERED",
                        "data": [
                            {"range": myrange,
                             "majorDimension": "ROWS",
                             "values": [
                                 ChangeString,
                                 ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
                             ]
                             # заполняем 2 строки таблицы, первую значениями, вторую пробелами, заполнение одной строки неработает хз почему
                             }

                        ]
                    }

                ).execute()
                acc=(int(Bort)+int(Bolt)+int(OnTaxi)+int(Taxi3000)+int(Taxi838)+int(Lubimoe))/int(Distance)
                self.Blabel1.text = "Данные отправлены"
                if acc>10:
                    self.Blabel2.text = "Твоя эфективность "+ str(acc)+' Отлично!'
                if acc<=10:
                    self.Blabel2.text = "Твоя эфективность "+ str(acc)+' Хорошо!'
                if acc <= 9.5:
                    self.Blabel2.text = "Твоя эфективность " + str(acc) + ' Средняя!'
                if acc <= 9:
                    self.Blabel2.text = "Твоя эфективность " + str(acc) + ' Плохо!'
                if acc <= 8.5:
                    self.Blabel2.text = "Твоя эфективность " + str(acc) + ' Отлично!'
                if acc <= 8:
                    self.Blabel2.text = "Твоя эфективность " + str(acc) + ' Ужас!'

                self.Blabel3.text = "Для завершения работы"
                self.Blabel4.text = "Нажимай кнопку ВЫХОД"
                self.button1.font_size = fs
                self.button1.text = "ВЫХОД"
                steep=steep+1
                return
            except:
                self.input_data.text = ""
                self.Blabel1.text = "Данные не отправлены"
                self.Blabel2.text = "Проверь подключение к интернету"
                self.Blabel3.text = "И повтори отправку"
                self.button1.text = "Повторная отправка"
        if steep == 20:
            sys.exit()


    def build(self):

        if steep>-5:
            al = AnchorLayout(anchor_y='top')
            gl = GridLayout(cols=2, size_hint=[1, .5], spacing=3)
            bl = BoxLayout(orientation="vertical", size_hint=[1, .5], spacing=3)
            bl.add_widget(self.Blabel0)
            bl.add_widget(self.Blabel1)
            bl.add_widget(self.Blabel2)
            bl.add_widget(self.Blabel3)
            bl.add_widget(self.Blabel4)
            bl.add_widget(self.Blabel5)

            gl.add_widget(self.button2)
            gl.add_widget(self.label0)
            gl.add_widget(self.label1)
            gl.add_widget(self.label2)
            gl.add_widget(self.label3)
            gl.add_widget(self.label4)
            gl.add_widget(self.label5)
            gl.add_widget(self.label6)
            gl.add_widget(self.label7)
            gl.add_widget(self.label8)
            gl.add_widget(self.label9)
            gl.add_widget(self.label10)
            gl.add_widget(self.label11)
            gl.add_widget(self.label12)
            gl.add_widget(self.label13)
            gl.add_widget(self.label14)
            gl.add_widget(self.label15)
            gl.add_widget(self.label16)
            gl.add_widget(self.input_data)
            gl.add_widget(self.button1)
            al.add_widget(bl)
            al.add_widget(gl)

            return al








if __name__== "__main__":
    MyApp().run()
