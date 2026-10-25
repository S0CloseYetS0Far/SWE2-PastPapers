"""Question-bank helpers. Each data_*.py file calls these to register questions."""
Q = []          # all questions, in registration order
BY_ID = {}

CHAPTERS = {
    1: {"title": "Introduction", "deck": "introduction.pptx", "slides": 16},
    2: {"title": "Project Management", "deck": "project management.pptx", "slides": 33},
    3: {"title": "Quality Management", "deck": "quality mangment.pptx", "slides": 32},
    4: {"title": "Source Code Quality", "deck": "Source code Quality.pptx", "slides": 36},
    5: {"title": "Object-Oriented Analysis & Design", "deck": "object-Oriented sowfware analysis and design.pptx", "slides": 27},
    6: {"title": "Security Engineering", "deck": "security engineering.pptx", "slides": 44},
    7: {"title": "Dependability & Reliability", "deck": "Dependability and reliability.pptx", "slides": 33},
    8: {"title": "Software Testing", "deck": None},
    9: {"title": "Software Evolution & Configuration Management", "deck": None},
    10: {"title": "Other Topics (Formal Verification, TDD, Patterns)", "deck": None},
}

SOURCES = {}


def src(id, label, file):
    SOURCES[id] = {"id": id, "label": label, "file": file}


def _add(d):
    assert d["id"] not in BY_ID, "duplicate id " + d["id"]
    assert d["ch"] in CHAPTERS, d
    Q.append(d)
    BY_ID[d["id"]] = d
    return d


def _from(s, qn, pg):
    assert s in SOURCES, s
    return [{"s": s, "qn": qn, "pg": pg}]


def mcq(id, ch, sl, tp, q, o, a, e, s, qn, pg=None, **kw):
    """a = index of the correct option (0-based) or letter."""
    if isinstance(a, str):
        a = "abcdefgh".index(a.lower())
    assert 0 <= a < len(o), id
    return _add(dict(id=id, ch=ch, sl=str(sl), tp=tp, t="mcq", q=q, o=o, a=a, e=e, **{"from": _from(s, qn, pg)}, **kw))


def tf(id, ch, sl, tp, q, a, e, s, qn, pg=None, **kw):
    """a = True/False."""
    return _add(dict(id=id, ch=ch, sl=str(sl), tp=tp, t="tf", q=q, a=0 if a else 1, e=e, **{"from": _from(s, qn, pg)}, **kw))


def short(id, ch, sl, tp, q, a, e, s, qn, pg=None, **kw):
    return _add(dict(id=id, ch=ch, sl=str(sl), tp=tp, t="short", q=q, a=a, e=e, **{"from": _from(s, qn, pg)}, **kw))


PENDING = []


def also(id, s, qn, pg=None):
    """The same question appeared again in another exam (resolved after all files load)."""
    assert s in SOURCES, s
    PENDING.append((id, {"s": s, "qn": qn, "pg": pg}))


def table(head, rows):
    h = '<table class="mini"><tr>' + "".join("<th>%s</th>" % c for c in head) + "</tr>"
    for r in rows:
        h += "<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>"
    return h + "</table>"


def ol(items):
    return "<ol>" + "".join("<li>%s</li>" % i for i in items) + "</ol>"


def ul(items):
    return "<ul>" + "".join("<li>%s</li>" % i for i in items) + "</ul>"
