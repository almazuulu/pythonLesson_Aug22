#Task 2
"""
(Стоимость доставки) Транспортная компания использует
следующий тариф для расчета стоимости (в долларах) доставки на
основе веса посылки (в килограммах).
• Если вес находится в промежутке между
0 и 2 кг - то расчет за кг идет по тарифу 3.5$ за кг.
• Если вес находится в промежутке между
3 и 5 кг - то расчет за кг идет по тарифу 5.5$ за кг.
• Если вес находится в промежутке между
6 и 10 кг - то расчет за кг идет по тарифу 7$ за кг.
• Если вес до 50кг расчет за кг идет по тарифу 10$ за кг.
Напишите программу, предлагающую пользователю ввести вес
посылки и отобразить стоимость доставки. Если вес больше 50 кг,
отобразить сообщение «посылка не может быть отправлена»
"""

weight = int(input('Enter kg: '))
if weight > 0 and weight<= 2.9:
    result = weight * 3.5
elif weight >= 3 and weight <= 5.9:
    result = weight * 5.5
elif weight >= 6 and weight <= 10:
    result = weight * 7
elif weight > 10 and weight <50 :
    result = weight * 10
else:
    result =  weight * 15

print(f'Final Price after calculation: {result}$')
