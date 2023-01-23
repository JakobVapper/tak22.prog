sales = {
    "Johnver": {
        "revenue": {
            "tea": 190,
            "coffee": 325,
            "water": 682,
            "milk": 829,
        },
        "expenses": {
            "tea": 120,
            "coffee": 300,
            "water": 50,
            "milk": 67,
        }
    },
    "Vanston": {
        "revenue": {
            "tea": 140,
            "coffee": 19,
            "water": 14,
            "milk": 140,
        },
        "expenses": {
            "tea": 65,
            "coffee": 10,
            "water": 299,
            "milk": 254,
        }
    },
    "Danbree": {
        "revenue": {
            "tea": 1926,
            "coffee": 293,
            "water": 852,
            "milk": 609,
        },
        "expenses": {
            "tea": 890,
            "coffee": 23,
            "water": 1290,
            "milk": 87,
        }
    },
    "Vansey": {
        "revenue": {
            "tea": 14,
            "coffee": 1491,
            "water": 56,
            "milk": 120,
        },
        "expenses": {
            "tea": 54,
            "coffee": 802,
            "water": 12,
            "milk": 129,
        }
    },
    "Mundyke": {
        "revenue": {
            "tea": 143,
            "coffee": 162,
            "water": 659,
            "milk": 87,
        },
        "expenses": {
            "tea": 430,
            "coffee": 235,
            "water": 145,
            "milk": 76,
        }
    }
}

for employee_name, employee_sales in sales.items():
    print(employee_name)
    comission = 0

    for product, revenue in employee_sales["revenue"].items():
        profit = revenue - employee_sales["expenses"][product]

        if profit > 0:
            profit_calc = profit * 0.062
            comission += profit * 0.062
    print(int(comission))