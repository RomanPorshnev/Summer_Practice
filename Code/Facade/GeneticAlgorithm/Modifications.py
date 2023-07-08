import enum


class Modifications(enum.Enum):
    # варианты выбор родителей
    tournament_selection = 0
    roulette_selection = 1
    # варианты составления пар
    panmixia = 2
    in_and_outbreeding = 3
    # варианты кроссоверов
    homogeneous_recombination = 4
    single_point_recombination = 5
    # варианты мутаторов
    binary_mutator = 6
    adaptive_mutator = 7
    # варианты селекторов популяции
    elite_selection = 8
    selection_by_displacement = 9
