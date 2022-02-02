from owlready2 import *
from ontology import *

s2022 = Season("2022")
s2021 = Season("2021")
s2020 = Season("2020")
s2019 = Season("2019")
s2018 = Season("2018")
s2017 = Season("2017")
s2016 = Season("2016")
s2015 = Season("2015")
s2014 = Season("2014")
s2013 = Season("2013")
s2012 = Season("2012")
s2011 = Season("2011")
s2010 = Season("2010")
s2008 = Season("2008")
s2007 = Season("2007")
s2006 = Season("2006")
s2005 = Season("2005")
s2004 = Season("2004")
s2003 = Season("2003")
s2002 = Season("2002")
s2001 = Season("2001")
s2000 = Season("2000")
s1999 = Season("1999")
s1998 = Season("1998")
s1997 = Season("1997")
s1996 = Season("1996")
s1994 = Season("1994")
s1993 = Season("1993")
s1992 = Season("1992")
s1991 = Season("1991")
s1988 = Season("1988")
s1987 = Season("1987")
s1986 = Season("1986")
s1985 = Season("1985")
s1984 = Season("1984")
s1983 = Season("1983")
s1982 = Season("1982")
s1981 = Season("1981")
s1980 = Season("1980")
s1979 = Season("1979")
s1977 = Season("1977")
s1976 = Season("1976")
s1975 = Season("1975")
s1974 = Season("1974")
s1965 = Season("1965")
s1964 = Season("1964")
s1961 = Season("1961")

# Circuit
bahrain = Circuit("Bahrain International Circuit")
imola = Circuit("Autodromo Enzo e Dino Ferrari")
algarve = Circuit("Autodromo Internacional do Algarve")
barcelona = Circuit("Circuit de Barcelona-Catalunya")
monaco = Circuit("Circuit de Monaco")
baku = Circuit("Baku City Circuit")
paul_ricard = Circuit("Circuit Paul Ricard")
red_bull_ring = Circuit("Red Bull Ring")
silverstone = Circuit("Silverstone Circuit")
hungaroring = Circuit("Hungaroring")
spa = Circuit("Circuit de Spa-Francochamps")
zandvoort = Circuit("Circuit Park Zandvoort")
monza = Circuit("Autodromo Nazionale di Monza")
sochi = Circuit("Sochi Autodrom")
istanbul = Circuit("Istanbul Park")
cota = Circuit("Circuit of the Americas")
mexico = Circuit("Autodromo Hermanos Rodriguez")
sao_paulo = Circuit("Autodromo Jose Carlos Pace")
qatar = Circuit("Losail International Circuit")
jeddah = Circuit("Jeddah Street Circuit")
abu_dhabi = Circuit("Yas Marina Circuit")

# Races
# Only adding races from 2021

bahrain_2021 = Race("Bahrain Grand Prix", race_at=bahrain, part_of=s2021)
imola_2021 = Race("Emilia Romagna Grand Prix", race_at=imola, part_of=s2021)
portugal_2021 = Race("Portuguese Grand Prix", race_at=algarve, part_of=s2021)
spain_2021 = Race("Spanish Grand Prix", race_at=barcelona, part_of=s2021)
monaco_2021 = Race("Monaco Grand Prix", race_at=monaco, part_of=s2021)
baku_2021 = Race("Azerbaijan Grand Prix", race_at=baku, part_of=s2021)
france_2021 = Race("French Grand Prix", race_at=paul_ricard, part_of=s2021)
styria_2021 = Race("Styrian Grand Prix", race_at=red_bull_ring, part_of=s2021)
austria_2021 = Race("Austrian Grand Prix", race_at=red_bull_ring, part_of=s2021)
british_2021 = Race("British Grand Prix", race_at=silverstone, part_of=s2021)
hungarian_2021 = Race("Hungarian Grand Prix", race_at=hungaroring, part_of=s2021)
belgium_2021 = Race("Belgium Grand Prix", race_at=spa, part_of=s2021)
netherlands_2021 = Race("Dutch Grand Prix", race_at=spa, part_of=s2021)
italy_2021 = Race("Italian Grand Prix", race_at=monza, part_of=s2021)
russia_2021 = Race("Russian Grand Prix", race_at=sochi, part_of=s2021)
turkey_2021 = Race("Turkish Grand Prix", race_at=istanbul, part_of=s2021)
us_2021 = Race("United States Grand Prix", race_at=cota, part_of=s2021)
mexico_2021 = Race("Mexico City Grand Prix", race_at=mexico, part_of=s2021)
brazil_2021 = Race("São Paulo Grand Prix", race_at=sao_paulo, part_of=s2021)
qatar_2021 = Race("Qatar Grand Prix", race_at=qatar, part_of=s2021)
saudi_2021 = Race("Saudi Arabian Grand Prix", race_at=jeddah, part_of=s2021)
abu_dhabi_2021 = Race("Abu Dhabi Grand Prix", race_at=abu_dhabi, part_of=s2021)

bahrain_2021_q = Qualifying("Bahrain Grand Prix Qualy", qualy_at=bahrain, qualy_for=bahrain_2021)
imola_2021_q = Qualifying("Emilia Romagna Grand Prix Qualy", qualy_at=imola, qualy_for=imola_2021)
portugal_2021_q = Qualifying("Portuguese Grand Prix Qualy", qualy_at=algarve, qualy_for=portugal_2021)
spain_2021_q = Qualifying("Spanish Grand Prix Qualy", qualy_at=barcelona, qualy_for=spain_2021)
monaco_2021_q = Qualifying("Monaco Grand Prix Qualy", qualy_at=monaco, qualy_for=monaco_2021)
baku_2021_q = Qualifying("Azerbaijan Grand Prix Qualy", qualy_at=baku, qualy_for=baku_2021)
france_2021_q = Qualifying("French Grand Prix Qualy", qualy_at=paul_ricard, qualy_for=france_2021)
styria_2021_q = Qualifying("Styrian Grand Prix Qualy", qualy_at=red_bull_ring, qualy_for=styria_2021)
austria_2021_q = Qualifying("Austrian Grand Prix Qualy", qualy_at=red_bull_ring, qualy_for=austria_2021)
british_2021_q = Qualifying("British Grand Prix Qualy", qualy_at=silverstone, qualy_for=british_2021)
hungarian_2021_q = Qualifying("Hungarian Grand Prix Qualy", qualy_at=hungaroring, qualy_for=hungarian_2021)
belgium_2021_q = Qualifying("Belgium Grand Prix Qualy", qualy_at=spa, qualy_for=belgium_2021)
netherlands_2021_q = Qualifying("Dutch Grand Prix Qualy", qualy_at=spa, qualy_for=netherlands_2021)
italy_2021_q = Qualifying("Italian Grand Prix Qualy", qualy_at=monza, qualy_for=italy_2021)
russia_2021_q = Qualifying("Russian Grand Prix Qualy", qualy_at=sochi, qualy_for=russia_2021)
turkey_2021_q = Qualifying("Turkish Grand Prix Qualy", qualy_at=istanbul, qualy_for=turkey_2021)
us_2021_q = Qualifying("United States Grand Prix Qualy", qualy_at=cota, qualy_for=us_2021)
mexico_2021_q = Qualifying("Mexico City Grand Prix Qualy", qualy_at=mexico, qualy_for=mexico_2021)
brazil_2021_q = Qualifying("São Paulo Grand Prix Qualy", qualy_at=sao_paulo, qualy_for=brazil_2021)
qatar_2021_q = Qualifying("Qatar Grand Prix Qualy", qualy_at=qatar, qualy_for=qatar_2021)
saudi_2021_q = Qualifying("Saudi Arabian Grand Prix Qualy", qualy_at=jeddah, qualy_for=saudi_2021)
abu_dhabi_2021_q = Qualifying("Abu Dhabi Grand Prix Qualy", qualy_at=abu_dhabi, qualy_for=abu_dhabi_2021)



# Engine supplier
ferrari_engine = EngineSupplier("Ferrari")
mercedes_engine = EngineSupplier("Mercedes")
red_bull_engine = EngineSupplier("Red Bull")
renault_engine = EngineSupplier("Renault")

# Constructors
alfa_romeo = Constructor("Alfa Romeo", is_supplied_by=ferrari_engine)
alpha_tauri = Constructor("Alpha Tauri", is_supplied_by=red_bull_engine)
alpine = Constructor("Alpine", is_supplied_by=renault_engine, is_wcc=[s2006, s2005])
aston_martin = Constructor("Aston Martin", is_supplied_by=mercedes_engine)
ferrari = Constructor("Ferrari", is_supplied_by=ferrari_engine,
                      is_wcc=[s2008, s2007, s2004, s2003, s2002, s2001, s2000, s1999, s1983, s1982,
                              s1979, s1977, s1976, s1975, s1965, s1964, s1961])
haas = Constructor("Haas", is_supplied_by=ferrari_engine)
mclaren = Constructor("McLaren", is_supplied_by=mercedes_engine,
                      is_wcc=[s1998, s1991, s1988, s1986, s1985, s1984, s1974])
mercedes = Constructor("Mercedes", is_supplied_by=mercedes_engine,
                       is_wcc=[s2021, s2020, s2019, s2018, s2017, s2016, s2015, s2014])
red_bull = Constructor("Red Bull", is_supplied_by=red_bull_engine,
                       is_wcc=[s2013, s2012, s2011, s2010])
williams = Constructor("Williams", is_supplied_by=mercedes_engine,
                       is_wcc=[s1997, s1996, s1994, s1993, s1992, s1987, s1986, s1981, s1980])



# Tyre supplier
pirelli = TyreManufacturer("Pirelli", supplies_tyres=[alfa_romeo, alpha_tauri, alpine,
                                                      aston_martin, ferrari, haas, mclaren,
                                                      mercedes, red_bull, williams])

# Sponsors
uralkali = Company("Uralkali")
lavazza = Company("Lavazza")

# Drivers
guanyu_zhou = Driver("Guanyu Zhou", competes_in_season=s2022, drives_for=alfa_romeo)

valtteri_bottas = Driver("Valtteri Bottas", competes_in_season=s2022, drives_for=alfa_romeo,
                         drived_for=[williams, mercedes],
                         got_podium=[bahrain_2021, portugal_2021, spain_2021, styria_2021],
                         got_pole=[portugal_2021_q, turkey_2021_q, mexico_2021_q, brazil_2021_q],
                         raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021, monaco_2021,
                                  baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                                  hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                                  russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                                  qatar_2021, saudi_2021, abu_dhabi_2021],
                         won_race=[turkey_2021])

pierre_gasly = Driver("Pierre Gasly", competes_in_season=s2022, drives_for=alpha_tauri,
                      drived_for=[red_bull],
                      got_podium=[baku_2021],
                      raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021, monaco_2021,
                               baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                               hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                               russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                               qatar_2021, saudi_2021, abu_dhabi_2021]
                      )
yuki_tsunoda = Driver("Yuki Tsonoda", competes_in_season=s2022, drives_for=alpha_tauri,
                      raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021, monaco_2021,
                               baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                               hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                               russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                               qatar_2021, saudi_2021, abu_dhabi_2021]
                      )

fernando_alonso = Driver("Fernando Alonso", competes_in_season=s2022, drives_for=alpine,
                         drived_for=[mclaren, ferrari],
                         got_podium=[qatar_2021],
                         is_wdc=[s2005, s2006],
                         raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021, monaco_2021,
                                  baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                                  hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                                  russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                                  qatar_2021, saudi_2021, abu_dhabi_2021]
                         )
esteban_ocon = Driver("Esteban Ocon", competes_in_season=s2022, drives_for=alpine,
                      drived_for=[aston_martin],
                      raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021, monaco_2021,
                               baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                               hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                               russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                               qatar_2021, saudi_2021, abu_dhabi_2021],
                      won_race=[hungarian_2021]
                      )

sebastian_vettel = Driver("Sebastian Vettel", competes_in_season=s2022, drives_for=aston_martin,
                          drived_for=[alpha_tauri, red_bull, ferrari],
                          got_podium=[baku_2021],
                          is_wdc=[s2010, s2011, s2012, s2013],
                          raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021, monaco_2021,
                                   baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                                   hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                                   russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                                   qatar_2021, saudi_2021, abu_dhabi_2021]
                          )
lance_stroll = Driver("Lance Stroll", competes_in_season=s2022, drives_for=aston_martin,
                      raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021, monaco_2021,
                               baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                               hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                               russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                               qatar_2021, saudi_2021, abu_dhabi_2021]
                      )

charles_leclerc = Driver("Charles Leclerc", competes_in_season=s2022, drives_for=ferrari,
                         drived_for=[alfa_romeo], got_podium=[british_2021],
                         got_pole=[monaco_2021_q, baku_2021_q],
                         raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021, monaco_2021,
                                  baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                                  hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                                  russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                                  qatar_2021, saudi_2021, abu_dhabi_2021]
                         )
carlos_sainz = Driver("Carlos Sainz", competes_in_season=s2022, drives_for=ferrari,
                      drived_for=[alpha_tauri, alpine, mclaren],
                      got_podium=[monaco_2021, hungarian_2021, russia_2021, abu_dhabi_2021],
                      raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021, monaco_2021,
                               baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                               hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                               russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                               qatar_2021, saudi_2021, abu_dhabi_2021]
                      )

nikita_mazepin = Driver("Nikita Mazepin", competes_in_season=s2022, drives_for=haas,
                           raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021,
                                    monaco_2021,
                                    baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                                    hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                                    russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                                    qatar_2021, saudi_2021, abu_dhabi_2021],
                           sponsored_by=[uralkali]
                           )
mick_schumacher = Driver("Mick Schumacher", competes_in_season=s2022, drives_for=haas,
                         raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021,
                                  monaco_2021,
                                  baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                                  hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                                  russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                                  qatar_2021, saudi_2021, abu_dhabi_2021])

daniel_ricciardo = Driver("Daniel Ricciardo", competes_in_season=s2022, drives_for=mclaren,
                          drived_for=[alpha_tauri, red_bull],
                          raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021,
                                   monaco_2021,
                                   baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                                   hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                                   russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                                   qatar_2021, saudi_2021, abu_dhabi_2021],
                          won_race=[italy_2021]
                          )
lando_norris = Driver("Lando Norris", competes_in_season=s2022, drives_for=mclaren,
                      got_podium=[imola_2021, monaco_2021, austria_2021, italy_2021],
                      got_pole=[russia_2021_q],
                      raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021,
                               monaco_2021,
                               baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                               hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                               russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                               qatar_2021, saudi_2021, abu_dhabi_2021]
                      )

lewis_hamilton = Driver("Lewis Hamilton", competes_in_season=s2022, drives_for=mercedes,
                        drived_for=[mclaren],
                        got_podium=[imola_2021,
                                    france_2021, styria_2021,
                                    hungarian_2021, belgium_2021, netherlands_2021,
                                    us_2021, mexico_2021, abu_dhabi_2021],
                        got_pole=[imola_2021_q, spain_2021_q, hungarian_2021_q, qatar_2021_q,
                                  saudi_2021_q],
                        is_wdc=[s2008, s2014, s2015, s2017, s2018, s2019, s2020],
                        raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021,
                                 monaco_2021,
                                 baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                                 hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                                 russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                                 qatar_2021, saudi_2021, abu_dhabi_2021],
                        won_race=[bahrain_2021, portugal_2021, spain_2021, british_2021,
                                  russia_2021, brazil_2021,
                                  qatar_2021, saudi_2021]
                        )
george_russell = Driver("George Russell", competes_in_season=s2022, drives_for=mercedes,
                        drived_for=[williams],
                        raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021,
                                 monaco_2021,
                                 baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                                 hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                                 russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                                 qatar_2021, saudi_2021, abu_dhabi_2021])

max_verstappen = Driver("Max Verstappen", competes_in_season=s2022, drives_for=red_bull,
                        drived_for=[alpha_tauri],
                        got_podium=[bahrain_2021, portugal_2021, spain_2021,
                                 russia_2021, turkey_2021, brazil_2021,
                                 qatar_2021, saudi_2021],
                        got_pole=[bahrain_2021_q, imola_2021_q, portugal_2021_q, spain_2021_q,
                                 monaco_2021_q, baku_2021_q, france_2021_q, styria_2021_q,
                                  austria_2021_q, british_2021_q,
                                 hungarian_2021_q, belgium_2021_q, netherlands_2021_q, italy_2021_q,
                                 russia_2021_q, turkey_2021_q, us_2021_q, mexico_2021_q, brazil_2021_q,
                                 qatar_2021_q, saudi_2021_q, abu_dhabi_2021_q],
                        raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021,
                                 monaco_2021,
                                 baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                                 hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                                 russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                                 qatar_2021, saudi_2021, abu_dhabi_2021],
                        is_wdc=[s2021],
                        won_race=[imola_2021, monaco_2021, france_2021, styria_2021, austria_2021,
                                 belgium_2021, netherlands_2021, us_2021, mexico_2021, abu_dhabi_2021],
                        )
sergio_perez = Driver("Sergio Perez", competes_in_season=s2022, drives_for=red_bull,
                      drived_for=[alfa_romeo, mclaren, aston_martin],
                      got_podium=[france_2021, turkey_2021, us_2021, mexico_2021],
                      raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021,
                               monaco_2021,
                               baku_2021, france_2021, styria_2021, austria_2021, british_2021,
                               hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                               russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                               qatar_2021, saudi_2021, abu_dhabi_2021],
                      won_race=[baku_2021]
                      )

nicholas_latifi = Driver("Nicholas Latifi", competes_in_season=s2022, drives_for=williams,
                            raced_at=[bahrain_2021, imola_2021, portugal_2021, spain_2021,
                                     monaco_2021,
                                     baku_2021, france_2021, styria_2021, austria_2021,
                                     british_2021,
                                     hungarian_2021, belgium_2021, netherlands_2021, italy_2021,
                                     russia_2021, turkey_2021, us_2021, mexico_2021, brazil_2021,
                                     qatar_2021, saudi_2021, abu_dhabi_2021],
                            sponsored_by=[lavazza]
                            )
alexander_albon = Driver("Alexander Albon", competes_in_season=s2022, drives_for=williams,
                         drived_for=[alpha_tauri, red_bull])

# Reserve Drivers
sebastien_buemi = ReserveDriver("Sebastien Buemi", reserve_driver_for=[red_bull])
antonio_giovinazzi = ReserveDriver("Antonio Giovinazzi", reserve_driver_for=[ferrari])
oscar_piastri = ReserveDriver("Oscar Piastri", reserve_driver_for=[alpine])

# Team Principals
frederic_vasseur = TeamPrincipal("Frederic Vasseur", works_for=alfa_romeo)
franz_tost = TeamPrincipal("Franz Tost", works_for=alpha_tauri)
davide_brivio = TeamPrincipal("Davide Brivio", works_for=alpine)
mike_krack = TeamPrincipal("Mike Krack", works_for=aston_martin)
mattia_sbinotto = TeamPrincipal("Matia Binotto", works_for=ferrari)
guenther_steiner = TeamPrincipal("Guenther Steiner", works_for=haas)
anreas_seidl = TeamPrincipal("Andreas Seidl", works_for=mclaren)
toto_wolf = TeamPrincipal("Toto Wolf", works_for=mercedes)
christian_horner = TeamPrincipal("Christian Horner", works_for=red_bull)
jost_capito = TeamPrincipal("Jost Capito", works_for=williams)

onto.save()


print(f"Lewis Hamilton is {lewis_hamilton.is_a[0]}")
print(f"Nikita Mazepin is {nikita_mazepin.is_a[0]}")

inferences = get_ontology("http://test.org/onto_inferences.owl")
with inferences:
     sync_reasoner_pellet()

print(f"Lewis Hamilton is {lewis_hamilton.is_a[0]}")
print(f"Nikita Mazepin is {nikita_mazepin.is_a[0]}")

