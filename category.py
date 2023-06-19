import telebot
from telebot import TeleBot, types



# main category
maincategory = types.InlineKeyboardMarkup(row_width=4)
saving = types.InlineKeyboardButton('저축', callback_data='saving')
income = types.InlineKeyboardButton("수입", callback_data='income')
fixed_expenditure = types.InlineKeyboardButton("고정지출", callback_data='fixed_expenditure')
food_expenses = types.InlineKeyboardButton('식비', callback_data='food_expenses')
pocket_money = types.InlineKeyboardButton("용돈", callback_data='pocket_money')
clothing = types.InlineKeyboardButton('의복/미용', callback_data='clothing')
animals = types.InlineKeyboardButton("동물", callback_data='animals')
health = types.InlineKeyboardButton('건강', callback_data='health')
self_improv  = types.InlineKeyboardButton('자기계발', callback_data='self_emprov')
family_celebration = types.InlineKeyboardButton("경조사", callback_data='family_celebration')
travelling = types.InlineKeyboardButton('여행', callback_data='traveling')
daily_supply = types.InlineKeyboardButton('생활용품', callback_data = 'daily_supply')
maincategory.add(income, saving, fixed_expenditure,food_expenses, pocket_money, clothing, animals, health, self_improv, family_celebration, travelling, daily_supply)

# saving
savingcategory = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
mainsalary = types.KeyboardButton('월급')
bonus =types.KeyboardButton('상여금')
parttime = types.KeyboardButton('부수입')
savingcategory.add(mainsalary, bonus, parttime)

# income
incomecategory = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
trading =  types.KeyboardButton('외환트레이딩')
toss= types.KeyboardButton('모임통장(토스)')
incomecategory.add(trading, toss)



# fixed_expenditure
fixedcategory = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
house =  types.KeyboardButton('주거비')
car=  types.KeyboardButton('차')
phone = types.KeyboardButton('통신비')
bus= types.KeyboardButton('교통비')
fixedcategory.add(house, car, phone, bus)


# food_expenses
foodcategory = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
market = types.KeyboardButton('마트')
gs = types.KeyboardButton('편의점')
eatout = types.KeyboardButton('외식')
delivery = types.KeyboardButton('배달음식')
foodcategory.add(market, gs, eatout, delivery)


# pocket_money
pocketcategory = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
ugene = types.KeyboardButton('유진_용돈')
katarina= types.KeyboardButton('리나_용돈')
pocketcategory.add(ugene, katarina)



# clothing
clothingcategory = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
clothes = types.KeyboardButton('의류')
beauty = types.KeyboardButton('뷰티')
hair = types.KeyboardButton('헤어')
clothingcategory.add(clothes, beauty, hair)



# daily_supply
dailysupplycategory = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
dailynessessity = types.KeyboardButton('생필품/소모품')
repair = types.KeyboardButton('수리비')
kitchen = types.KeyboardButton('주방/욕실')
dailysupplycategory.add(dailynessessity, repair, kitchen)


# animals
animalscategory =  types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
gil = types.KeyboardButton('생질_산책')
dogfood = types.KeyboardButton('사료')
animalhospital = types.KeyboardButton('병원비')
dogcare = types.KeyboardButton('미용')
dogvitamin = types.KeyboardButton('비타민')
animalscategory.add(gil, dogfood, animalhospital, dogcare, dogvitamin)


# health
healthcategory = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
hospital = types.KeyboardButton('병원/약국')
nutrition = types.KeyboardButton('영양제')
exercise = types.KeyboardButton('운동비')
healthcategory.add(hospital, nutrition, exercise)



# self_improv
selfcategory =  types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
lecture = types.KeyboardButton('강의')
book = types.KeyboardButton('책')
exemination = types.KeyboardButton('응시료')
selfcategory.add(lecture, book, exemination)


# family_celebration
familycategory = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
family = types.KeyboardButton('가족')
acquaintance = types.KeyboardButton('지인')
familycategory.add(family, acquaintance)


# travelling
travellingcategory = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
airticket = types.KeyboardButton('비행기표')
hotel = types.KeyboardButton('호텔')
travel = types.KeyboardButton('여행비')
travelgift = types.KeyboardButton('여행선물')
visa = types.KeyboardButton('비자')
travellingcategory.add(airticket, hotel, travel, travelgift, visa)

