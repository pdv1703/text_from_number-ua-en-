import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QTextEdit, QPushButton,
                             QLabel, QGridLayout, QComboBox, QDoubleSpinBox)

import decimal
import locale


class Example(QWidget):
    def __init__(self):
        super().__init__()

        # start button
        self.go_button = QPushButton('&Start converting')

        # line for inserting
        self.insert_number_line = QDoubleSpinBox()
        print(QDoubleSpinBox().locale())

        self.insert_number_line.setRange(0, 2147483647)
        #print(self.insert_number_line.locale())
        self.insert_number_line.editingFinished.connect(self.convert)

        # language list
        self.language_title = QLabel('Language:')
        self.language = QComboBox()
        self.language.setFixedWidth(50)
        self.language.addItem('En')
        self.language.addItem('Ua')


        self.exit_text = QTextEdit()
        # self.exit_text.setEnabled(0)

        self.initui()

    def initui(self):

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.go_button, 2, 0)
        grid.addWidget(self.insert_number_line, 2, 1)
        grid.addWidget(self.language_title, 1, 0)
        grid.addWidget(self.language, 1, 1)
        grid.addWidget(self.exit_text, 3, 0, 3, 2)
        self.setLayout(grid)

        self.setGeometry(70, 70, 500, 300)
        self.setWindowTitle('Convert number to text')
        self.show()

        self.go_button.clicked.connect(self.convert)

    def convert(self):
        self.exit_text.setText("")

        self.insert_number = self.insert_number_line.text()

        self.number = []

        if self.insert_number_line.locale().decimalPoint() == ".":
            for arg in self.insert_number.split("."):
                self.number.append(arg)

        if self.insert_number_line.locale().decimalPoint() == ",":
            for arg in self.insert_number.split(","):
                self.number.append(arg)

        if self.language.currentText() == "Ua":
            self.convert_ua(self.number)

        if self.language.currentText() == "En":
            self.convert_en(self.number)

    def convert_ua(self, number):
        """General Ua func"""

        if int(number[0]) == 0 and int(number[1]) == 0:
            self.exit_text.setText("нуль гривень")
        else:
            if int(number[0]) == 1:
                self.exit_text.setText("одна гривня")
            elif int(number[0]) == 2 or int(number[0]) == 3 or int(
                    number[0]) == 4:
                self.exit_text.setText(
                    self.int_to_ua(int(number[0])) + " гривні")
            else:
                self.exit_text.setText(
                    self.int_to_ua(int(number[0])) + " гривень")

            if int(number[0]) == 0 and int(number[1]) != 0:
                if int(number[1]) == 1:
                    self.exit_text.setText("одна копійка")
                else:
                    self.uah = self.exit_text.toPlainText()
                    self.exit_text.setText(
                        self.int_to_ua(int(number[1])) + " копійки")

            else:
                if int(number[1]) == 1:
                    self.uah = self.exit_text.toPlainText()
                    self.exit_text.setText(self.dollars + " та одна копійка")
                else:
                    if int(number[1]) != 0:
                        self.uah = self.exit_text.toPlainText()
                        self.exit_text.setText(
                            self.uah + " та " +
                            self.int_to_ua(int(number[1])) + " копійок")

    def convert_en(self, number):
        """General En func"""

        if int(number[0]) == 0 and int(number[1]) == 0:
            self.exit_text.setText("zero dollar")
        else:
            if int(number[0]) == 1:
                self.exit_text.setText("one dollar")
            else:
                self.exit_text.setText(
                    self.int_to_en(int(number[0])) + " dollars")

            if int(number[0]) == 0 and int(number[1]) != 0:
                if int(number[1]) == 1:
                    self.exit_text.setText("one cent")
                else:
                    self.dollars = self.exit_text.toPlainText()
                    self.exit_text.setText(
                        self.int_to_en(int(number[1])) + " cents")

            else:
                if int(number[1]) == 1:
                    self.dollars = self.exit_text.toPlainText()
                    self.exit_text.setText(self.dollars + " and one cent")
                else:
                    if int(number[1]) != 0:
                        self.dollars = self.exit_text.toPlainText()
                        self.exit_text.setText(
                            self.dollars + " and " +
                            self.int_to_en(int(number[1])) + " cents")

    def int_to_en(self, num):
        """convert int value to en text"""

        d = {
            0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety'
        }
        k = 1000
        m = k * 1000
        b = m * 1000
        t = b * 1000

        assert (0 <= num)

        if num < 20:
            return d[num]

        if num < 100:
            if num % 10 == 0:
                return d[num]
            else:
                return d[num // 10 * 10] + '-' + d[num % 10]

        if num < k:
            if num % 100 == 0:
                return d[num // 100] + ' hundred'
            else:
                return d[num // 100] + ' hundred and ' + self.int_to_en(
                    num % 100)

        if num < m:
            if num % k == 0:
                return self.int_to_en(num // k) + ' thousand'
            else:
                return self.int_to_en(
                    num // k) + ' thousand, ' + self.int_to_en(num % k)

        if num < b:
            if (num % m) == 0:
                return self.int_to_en(num // m) + ' million'
            else:
                return self.int_to_en(
                    num // m) + ' million, ' + self.int_to_en(num % m)

        if num < t:
            if (num % b) == 0:
                return self.int_to_en(num // b) + ' billion'
            else:
                return self.int_to_en(
                    num // b) + ' billion, ' + self.int_to_en(num % b)

        if num % t == 0:
            return self.int_to_en(num // t) + ' trillion'
        else:
            return self.int_to_en(num // t) + ' trillion, ' + self.int_to_en(
                num % t)

        # ======================= Ua section ===============

    units = (u'нуль', (u'один', u'одна'), (u'два', u'дві'), u'три', u'чотири',
             u"п'ять", u'шість', u'сім', u'вісім', u"дев'ять")

    teens = (u'десять', u'одинадцять', u'дванадцять', u'тринадцять',
             u'чотирнадцять', u"п'ятнадцять", u'шістнадцять', u'сімнадцять',
             u'вісімнадцять', u"дев'ятнадцять")

    tens = (teens, u'двадцять', u'тридцять', u'сорок', u'пятдесят',
            u'шістдесят', u'сімдесят', u'вісімдесят', u"дев'яносто")

    hundreds = (u'сто', u'двісті', u'триста', u'чотириста', u"п'ятсот",
                u'шістсот', u'сімсот', u'вісімсот', u"дев'ятсот")

    orders = (
        ((u'тисяча', u'тисячі', u'тисяч'), 'f'),
        ((u'мільйон', u'мільйона', u'мільйонів'), 'm'),
        ((u'мільярд', u'мільярда', u'мільярдів'), 'm'),
    )

    def thousand(self, rest, sex):
        """Converts numbers from 19 to 999"""
        prev = 0
        plural = 2
        name = []
        use_teens = rest % 100 >= 10 and rest % 100 <= 19
        if not use_teens:
            data = ((self.units, 10), (self.tens, 100), (self.hundreds, 1000))
        else:
            data = ((self.tens, 10), (self.hundreds, 1000))
        for names, x in data:
            cur = int(((rest - prev) % x) * 10 / x)
            prev = rest % x
            if x == 10 and use_teens:
                plural = 2
                name.append(self.teens[cur])
            elif cur == 0:
                continue
            elif x == 10:
                name_ = names[cur]
                if isinstance(name_, tuple):
                    name_ = name_[0 if sex == 'm' else 1]
                name.append(name_)
                if cur >= 2 and cur <= 4:
                    plural = 1
                elif cur == 1:
                    plural = 0
                else:
                    plural = 2
            else:
                name.append(names[cur - 1])
        return plural, name

    def int_to_ua(self, num, main_units=((u'', u'', u''), 'm')):
        _orders = (main_units, ) + self.orders
        if num == 0:
            return ' '.join((self.units[0], _orders[0][0][2])).strip()  # ноль

        rest = abs(num)
        ord = 0
        name = []
        while rest > 0:
            plural, nme = self.thousand(rest % 1000, _orders[ord][1])
            if nme or ord == 0:
                name.append(_orders[ord][0][plural])
            name += nme
            rest = int(rest / 1000)
            ord += 1

        name.reverse()
        return ' '.join(name).strip()

    def decimal2text(self,
                     value,
                     places=2,
                     int_units=(('', '', ''), 'm'),
                     exp_units=(('', '', ''), 'm')):
        value = decimal.Decimal(value)
        q = decimal.Decimal(10)**-places

        integral, exp = str(value.quantize(q)).split('.')
        return u'{} {}'.format(
            self.int_to_ua(int(integral), int_units),
            self.int_to_ua(int(exp), exp_units))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
