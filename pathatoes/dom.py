from __future__ import annotations

from typing import Any, NoReturn, Self, TypedDict, Unpack, reveal_type


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
        classes: list[str] | None = None,
        **kwargs,
    ):
        self._attributes = {}
        self._children = ()

        if classes:
            self._attributes["class"] = " ".join(classes)

        for key in kwargs:
            self._attributes[key.replace("_", "-")] = kwargs[key]

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
        attrs = " ".join([f'{key}="{value}"' for key, value in self._attributes.items()])

        res = [f"<{self._tag} {attrs}>"]

        for child in self._children:
            res.append(child.to_html())

        res.append(f"</{self._tag}>")
        return "".join(res)


class VoidElement(Element):
    def __getitem__(self) -> NoReturn:
        raise Exception(f"{self._tag} cannot have children")

    def to_html(self) -> str:
        attrs = " ".join([f'{key}="{value}"' for key, value in self._attributes.items()])
        return f"<{self._tag} {attrs} />"


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


class span(Element):
    _tag = "span"


class title(Element):
    _tag = "title"


class img(VoidElement):
    _tag = "img"


class br(VoidElement):
    _tag = "br"


class hr(VoidElement):
    _tag = "hr"


class input(VoidElement):
    _tag = "input"


class button(Element):
    _tag = "button"


class form(Element):
    _tag = "form"


class label(Element):
    _tag = "label"


class select(Element):
    _tag = "select"


class option(Element):
    _tag = "option"


class textarea(Element):
    _tag = "textarea"


class table(Element):
    _tag = "table"


class tr(Element):
    _tag = "tr"


class th(Element):
    _tag = "th"


class td(Element):
    _tag = "td"


class ul(Element):
    _tag = "ul"


class ol(Element):
    _tag = "ol"


class li(Element):
    _tag = "li"


class h1(Element):
    _tag = "h1"


class h2(Element):
    _tag = "h2"


class h3(Element):
    _tag = "h3"


class h4(Element):
    _tag = "h4"


class h5(Element):
    _tag = "h5"


class h6(Element):
    _tag = "h6"


class meta(VoidElement):
    _tag = "meta"


class link(VoidElement):
    _tag = "link"


class style(Element):
    _tag = "style"


class script(Element):
    _tag = "script"


class noscript(Element):
    _tag = "noscript"


class iframe(Element):
    _tag = "iframe"
