from __future__ import annotations

from typing import Any, Self


class EventTarget:
    ...


class Node(EventTarget):
    def to_html(self) -> str:
        raise NotImplementedError()


class Document(Node):
    ...


class Attr(Node):
    ...


class TextNode(Node):
    _text: str

    def __init__(self, text: str):
        self._text = text

    def to_html(self) -> str:
        return self._text


class Element(Node):
    _tag: str
    _attributes: dict[str, Any]
    _children: tuple[Element | TextNode, ...]

    def __init__(
        self,
        /,
        **kwargs,
    ):
        self._attributes = kwargs

    def __getitem__(self, children: tuple[str | Element, ...] | str | Element) -> Self:
        match children:
            case str():
                self._children = (TextNode(children),)
            case Element():
                self._children = (children,)
            case tuple():
                self._children = tuple([TextNode(c) if isinstance(c, str) else c for c in children])
            case _:
                raise Exception("invalid children", children)

        return self

    def to_html(self) -> str:
        res = [f"<{self._tag}>"]

        for child in self._children:
            res.append(child.to_html())

        res.append(f"</{self._tag}>")
        return "".join(res)


class html(Element):
    _tag = "html"


class head(Element):
    _tag = "head"


class body(Element):
    _tag = "body"


class div(Element):
    _tag = "div"


class p(Element):
    _tag = "p"


class a(Element):
    _tag = "a"


class img(Element):
    _tag = "img"


class span(Element):
    _tag = "span"
