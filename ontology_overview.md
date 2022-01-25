

# Онтология за Формула1

## Автор: Любослав Карев, ИИОЗ, ф.н.6MI3400005

## Проект тип: А

## Име на проект: Онтология за Формула 1

## Кратко описание:

​	Онтологията ще има за цел да опише максимално света на Формула 1 - моторен спорт с богата и дълбока история. Ще бъдат представени всички основни лица и събития - пилоти, отбори, писти, състезания и шампионати (Пълен списък с класове и свойства може да видите по-долу). Целта на проекта е да се създаде база от знания, чрез която много лесно да могат да се правят заявки тип "За кои отбори е карал даден пилот ?" или "Кой е пилотът с най-много победи ?" (типични въпроси, задавани на викторини свързани с Формула 1). 

## Използвани технологии:

​	За създаването на проекта ще бъде използвана библиотеката owlready2 и езика Python3

## Класове:

- Person
- Company
- Driver
- Reserve Driver 
- Pay Driver 
- Team Principal
- Constructor
- Season
- Qualifiying
- Race
- Circuit
- Championship
- World Drivers Champion
- World Constructors Champion
- Engine Suplier
- Works Team

## Свойства:



| Domain         | Property         | Range       | Characteristics |
| -------------- | ---------------- | ----------- | --------------- |
| Driver         | drivesFor        | Constructor |                 |
| Reserve Driver | reserveDriverFor | Construcotr |                 |
| Pay Driver     | sponsoredBy      | Company     |                 |
| Driver         | drivedFor        | Constructor |                 |
| Person         | workedFor        | Constructor |                 |
| Person         | worksFor         | Constructor |                 |
|                | competesInSeason |             |                 |
|                | gotPole          |             |                 |
|                | racedAt          |             |                 |
|                | wonRace          |             |                 |
|                | gotPodium        |             |                 |
|                | isWDC            |             |                 |
|                | isWCC            |             |                 |
|                | supplies         |             |                 |
|                | isSuppliedBy     |             |                 |

 

