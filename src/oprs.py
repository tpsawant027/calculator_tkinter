from math import pi, e


class Operator:
    operator_list = [
        [
            "\N{SQUARE ROOT}",
            "\N{GREEK SMALL LETTER PI}",
            "e",
            " \N{Circumflex Accent} ",
        ],
        ["AC", "\N{Left Parenthesis}", "\N{Right Parenthesis}", " \N{Division Sign} "],
        ["7", "8", "9", " \N{Multiplication Sign} "],
        ["6", "5", "4", " \N{Plus Sign} "],
        ["3", "2", "1", " \N{Minus Sign} "],
        ["0", "\N{Full Stop}", "\N{Erase To the Left}", "\N{Equals Sign} "],
    ]

    operator_dict = {
        operator_list[2][3]: " * ",
        operator_list[0][3]: " ** ",
        operator_list[1][3]: " / ",
        operator_list[4][3]: " - ",
        operator_list[0][1]: str(pi),
        operator_list[0][2]: str(e),
    }
