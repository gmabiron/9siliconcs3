birth_year = int(input("Enter your year of birth: "))

if birth_year < 1900:
    print("Invalid input! Birth year must not be earlier than 1900.")
else:
    remainder = birth_year % 12

    if remainder == 4:
        zodiac = "Rat (鼠 / Shǔ)"
    elif remainder == 5:
        zodiac = "Ox (牛 / Niú)"
    elif remainder == 6:
        zodiac = "Tiger (虎 / Hǔ)"
    elif remainder == 7:
        zodiac = "Rabbit (兔 / Tù)"
    elif remainder == 8:
        zodiac = "Dragon (龙 / Lóng)"
    elif remainder == 9:
        zodiac = "Snake (蛇 / Shé)"
    elif remainder == 10:
        zodiac = "Horse (马 / Mǎ)"
    elif remainder == 11:
        zodiac = "Goat (羊 / Yáng)"
    elif remainder == 0:
        zodiac = "Monkey (猴 / Hóu)"
    elif remainder == 1:
        zodiac = "Rooster (鸡 / Jī)"
    elif remainder == 2:
        zodiac = "Dog (狗 / Gǒu)"
    else:
        zodiac = "Pig (猪 / Zhū)"
    print(f"Your Chinese Zodiac sign is: {zodiac}")