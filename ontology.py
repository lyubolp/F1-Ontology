from owlready2 import *

onto = get_ontology("file://f1_onto.owl")

with onto:
    class Personnel(Thing): pass


    class Country (Thing): pass


    class Company(Thing): pass


    class Constructor(Thing): pass


    class Session(Thing): pass


    class EngineSupplier(Thing): pass


    class TyreManufacturer(Thing): pass


    class Circuit(Thing): pass


    class Season(Thing): pass


    class Driver(Thing): pass


    class RookieDriver(Driver): pass


    class ReserveDriver(Driver): pass


    class PayDriver(Driver): pass


    class TeamPrincipal(Personnel): pass


    class Qualifying(Session): pass


    class Race(Session): pass


    class is_wcc(Constructor >> Season): pass


    class drives_for(FunctionalProperty, Driver >> Constructor): pass


    class reserve_driver_for(ReserveDriver >> Constructor): pass


    class sponsored_by(Driver >> Company): pass


    class drived_for(Driver >> Constructor): pass


    class works_for(FunctionalProperty, Personnel >> Constructor): pass


    class competes_in_season(FunctionalProperty, Driver >> Season): pass


    class got_pole(Driver >> Qualifying): pass


    class raced_at(Driver >> Race): pass


    class won_race(Driver >> Race): pass


    class got_podium(Driver >> Race): pass


    class is_wdc(Driver >> Season): pass


    class supplies(EngineSupplier >> Constructor): pass


    class born_in(Driver >> Country, FunctionalProperty): pass

    class based_in(Constructor >> Country, FunctionalProperty): pass


    class is_supplied_by(FunctionalProperty, Constructor >> EngineSupplier):
        inverse_property = supplies


    class race_at(FunctionalProperty, Race >> Circuit): pass


    class qualy_at(FunctionalProperty, Qualifying >> Circuit): pass


    class qualy_for(FunctionalProperty, Qualifying >> Race): pass


    class part_of(FunctionalProperty, Race >> Season): pass


    class supplies_tyres(TyreManufacturer >> Constructor): pass

    class teammate(Driver >> Driver, SymmetricProperty, FunctionalProperty): pass

    class ahead_in_championship(Driver >> Driver, TransitiveProperty): pass


    class Driver(Thing):
        equivalent_to = [drives_for.some(Constructor)]


    class ReserveDriver(Thing):
        equivalent_to = [reserve_driver_for.some(Constructor)]


    class TeamPrincipal(Personnel):
        equivalent_to = [Personnel & works_for.some(Constructor)]


    class Qualifying(Thing):
        equivalent_to = [Session & qualy_at.some(Circuit) & qualy_for.some(Race)]


    current_season = Season("2021")


    class Race(Thing):
        equivalent_to = [Session & race_at.some(Circuit) & part_of.value(current_season)]


    class WorldDriversChampion(Driver):
        equivalent_to = [Driver & is_wdc.min(1, Season)]


    class MultipleWorldDriversChampion(Driver):
        equivalent_to = [Driver & is_wdc.min(2, Season)]


    class PayDriver(Driver):
        equivalent_to = [Driver & sponsored_by.min(1, Company)]

