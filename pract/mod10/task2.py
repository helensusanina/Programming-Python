import re
import doctest

def is_valid_date(date_string):
    """
    Проверка корректности даты по различным критериям

    >>> is_valid_date('20 января 1806')
    True
    >>> is_valid_date('1924, July 25')
    True
    >>> is_valid_date('26/09/1635')
    True
    >>> is_valid_date('3.1.1506')
    True
    >>> is_valid_date('25.08-1002')
    False
    >>> is_valid_date('декабря 19, 1838')
    False
    >>> is_valid_date('8.20.1973')
    False
    >>> is_valid_date('Jun 7, -1563')
    False
    >>> is_valid_date('31 февраля 2023')
    False
    >>> is_valid_date('31 июня 2015')
    False

    """
    pattern = (
        r"^(?:(?:(?:(?:0[1-9]|[12][0-9]|3[01])[./-](?:0[1-9]|1[0-2])[./-]\d{4})|"
        r"(?:\d{4}[./-](?:0[1-9]|1[0-2])[./-](?:0[1-9]|[12][0-9]|3[01]))|"
        r"(?:\d{1,2} (?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|"
        r"октября|ноября|декабря) \d{4}))|"
        r"(?:(?:\d{4}, (?:January|February|March|April|May|June|July|August|September|"
        r"October|November|December) \d{1,2})|"
        r"(?:\d{4}, (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2})|"
        r"(?:\d{1,2} (?:January|February|March|April|May|June|July|August|September|"
        r"October|November|December), \d{4})|"
        r"(?:\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec), \d{4})))$"
    )

    non_negative_check = r"(?=.*\d)(?!0\d)"
    full_regex = non_negative_check + pattern

    match = re.match(full_regex, date_string)

    return bool(match)


doctest.testmod()
