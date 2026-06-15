from typing import TYPE_CHECKING
from .items import get_progression_medal
from .locations import get_series_name
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from . import TrackmaniaWorld

def set_rules(world: "TrackmaniaWorld"):
    medal_total: int = world.series_data[0]["MedalTotal"]
    # Setting the rules for each serie
    for i in range(1,world.options.series_number):
        set_series_rules(world, i, medal_total)
        medal_total += world.series_data[i]["MedalTotal"]

    # Setting the rule for the victory region
    final_medal_requirement: int = medal_total
    progression_system = world.options.progression_system.value

    if progression_system == 0 :
        set_rule(world.multiworld.get_entrance("Victory!", world.player),
                 lambda state: state.has(get_progression_medal(world), world.player, final_medal_requirement))

    if progression_system == 1 : 
        progression_medal = get_progression_medal(world)
        if progression_medal == "Author Medal":
            set_rule(world.get_entrance("Victory!", world.player),
                 lambda state: (state.count("Author Medal", world.player) +
                        state.count("Gold Medal", world.player) +
                        state.count("Silver Medal", world.player) +
                        state.count("Bronze Medal", world.player)) >= final_medal_requirement * 4)
        if progression_medal == "Gold Medal":
            set_rule(world.get_entrance("Victory!", world.player),
                 lambda state: (state.count("Gold Medal", world.player) +
                        state.count("Silver Medal", world.player) +
                        state.count("Bronze Medal", world.player)) >= final_medal_requirement * 3)
        if progression_medal == "Silver Medal":
            set_rule(world.get_entrance("Victory!", world.player),
                 lambda state: (state.count("Silver Medal", world.player) +
                        state.count("Bronze Medal", world.player)) >= final_medal_requirement * 2)
        if progression_medal == "Bronze Medal":
            set_rule(world.get_entrance("Victory!", world.player),
                 lambda state: (state.count("Bronze Medal", world.player)) >= final_medal_requirement)
            
    if progression_system == 2 :
        progression_medal = get_progression_medal(world)
        if progression_medal == "Author Medal":
            set_rule(world.get_entrance("Victory!", world.player),
                 lambda state: (state.count("Author Medal", world.player) * 5 +
                     state.count("Gold Medal", world.player) * 3 +
                     state.count("Silver Medal", world.player) * 1 +
                     state.count("Bronze Medal", world.player) * 1
                 ) >= final_medal_requirement * 10)
        if progression_medal == "Gold Medal":
            set_rule(world.get_entrance("Victory!", world.player),
                 lambda state: (state.count("Gold Medal", world.player) * 5 +
                        state.count("Silver Medal", world.player) * 3 +
                        state.count("Bronze Medal", world.player) * 2) >= final_medal_requirement * 10)
        if progression_medal == "Silver Medal":
            set_rule(world.get_entrance("Victory!", world.player),
                 lambda state: (state.count("Silver Medal", world.player) * 7 +
                        state.count("Bronze Medal", world.player) * 3) >= final_medal_requirement * 10)
        if progression_medal == "Bronze Medal":
            set_rule(world.get_entrance("Victory!", world.player),
                 lambda state: (state.count("Bronze Medal", world.player) * 10) >= final_medal_requirement * 10)

    # default just in case
    else :
         set_rule(world.get_entrance(entrance_name),
                 lambda state: state.has(get_progression_medal(world), world.player, final_medal_requirement))

    
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory!", world.player)

def set_series_rules(world: "TrackmaniaWorld", series_index : int, medal_total: int):
    entrance_name: str = f"{get_series_name(series_index - 1)} -> {get_series_name(series_index)}"
    progression_system = world.options.progression_system.value
    
    if progression_system == 0 :
        set_rule(world.get_entrance(entrance_name),
                 lambda state: state.has(get_progression_medal(world), world.player, medal_total))
        
    if progression_system == 1 : 
        progression_medal = get_progression_medal(world)
        if progression_medal == "Author Medal":
            set_rule(world.get_entrance(entrance_name),
                 lambda state: (state.count("Author Medal", world.player) +
                        state.count("Gold Medal", world.player) +
                        state.count("Silver Medal", world.player) +
                        state.count("Bronze Medal", world.player)) >= medal_total * 4)
        if progression_medal == "Gold Medal":
            set_rule(world.get_entrance(entrance_name),
                 lambda state: (state.count("Gold Medal", world.player) +
                        state.count("Silver Medal", world.player) +
                        state.count("Bronze Medal", world.player)) >= medal_total * 3)
        if progression_medal == "Silver Medal":
            set_rule(world.get_entrance(entrance_name),
                 lambda state: (state.count("Silver Medal", world.player) +
                        state.count("Bronze Medal", world.player)) >= medal_total * 2)
        if progression_medal == "Bronze Medal":
            set_rule(world.get_entrance(entrance_name),
                 lambda state: (state.count("Bronze Medal", world.player)) >= medal_total)
            
    if progression_system == 2 :
        progression_medal = get_progression_medal(world)
        if progression_medal == "Author Medal":
            set_rule(world.get_entrance(entrance_name),
                 lambda state: (state.count("Author Medal", world.player) * 5 +
                     state.count("Gold Medal", world.player) * 3 +
                     state.count("Silver Medal", world.player) * 1 +
                     state.count("Bronze Medal", world.player) * 1
                 ) >= medal_total * 10)
        if progression_medal == "Gold Medal":
            set_rule(world.get_entrance(entrance_name),
                 lambda state: (state.count("Gold Medal", world.player) * 5 +
                        state.count("Silver Medal", world.player) * 3 +
                        state.count("Bronze Medal", world.player) * 2) >= medal_total * 10)
        if progression_medal == "Silver Medal":
            set_rule(world.get_entrance(entrance_name),
                 lambda state: (state.count("Silver Medal", world.player) * 7 +
                        state.count("Bronze Medal", world.player) * 3) >= medal_total * 10)
        if progression_medal == "Bronze Medal":
            set_rule(world.get_entrance(entrance_name),
                 lambda state: (state.count("Bronze Medal", world.player) * 10) >= medal_total * 10)

    # default just in case
    else :
         set_rule(world.get_entrance(entrance_name),
                 lambda state: state.has(get_progression_medal(world), world.player, medal_total))
    

            
        
