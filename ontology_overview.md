

# Онтология за Формула1

## Автор: Любослав Карев, ИИОЗ, ф.н.6MI3400005

## Проект тип: А

## Име на проект: Онтология за Формула 1

## Кратко описание:

​	Онтологията ще има за цел да опише максимално света на Формула 1 - моторен спорт с богата и дълбока история. Ще бъдат представени всички основни лица и събития - пилоти, отбори, писти, състезания и шампионати (Пълен списък с класове и свойства може да видите по-долу). Целта на проекта е да се създаде база от знания, чрез която много лесно да могат да се правят заявки тип "За кои отбори е карал даден пилот ?" или "Кой е пилотът с най-много победи ?" (типични въпроси, задавани на викторини свързани с Формула 1). 

## Използвани технологии:

​	За създаването на проекта ще бъде използвана библиотеката owlready2 и езика Python3

## Класове:

### Атомарни класове:

- Personnel
- Country
- Company
- Constructor
- Session
- Engine Supplier
- Tyre manufacturer
- Circuit
- Season

### Съставни класове:
- Driver
- Rookie Driver
- Reserve Driver
- Pay Driver
- Team Principal
- Qualifying
- Race
- WorldDriversChampion
- MultipleWorldDriversChampion

## Свойства:

| Domain         | Property           | Range          | Characteristics                 |
| -------------- | ------------------ | -------------- | ------------------------------- |
| Constructor    | is_wcc             | Season         |                                 |
| Constructor    | is_supplied_by     | EngineSupplier | Inverse of supplies, Functional |
| Driver         | competes_in_season | Season         | Functional                      |
| Driver         | drived_for         | Constructor    |                                 |
| Driver         | drives_for         | Constructor    | Functional                      |
| Driver         | got_podium         | Race           |                                 |
| Driver         | got_pole           | Qualifying     |                                 |
| Driver         | is_wdc             | Season         |                                 |
| Driver         | raced_at           | Race           |                                 |
| Driver         | won_race           | Race           |                                 |
| EngineSupplier | supplies           | Constructor    | Inverse of isSuppliedBy         |
| Pay Driver     | sponsored_by       | Company        |                                 |
| Person         | works_for          | Constructor    | Functional                      |
| Qualifying     | qualy_at           | Circuit        | Functional                      |
| Qualifying     | qualy_for          | Race           | Functional                      |
| Race           | race_at            | Circuit        | Functional                      |
| Race           | part_of            | Season         | Functional                      |
| Reserve Driver | reserve_driver_for | Constructor    |                                 |

 

# Sources:
https://www.wikiwand.com/en/2022_Formula_One_World_Championship
https://www.wikiwand.com/en/2021_Formula_One_World_Championship
https://www.fpal.org/motorsport/f1/the-test-and-reserve-drivers-for-the-2022-formula-1-season/
https://www.racing-statistics.com/en