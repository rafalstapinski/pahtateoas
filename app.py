from pathatoes.dom import *

html()(
    head()(),
    body()(
        div(classs="container bg-white")(
            h1()("Hello, World!"), p()("This is a paragraph."), a(href="/")("home")
        ),
    ),
)


html()[
    head(),
    body()[
        div(classes="container bg-white")[
            h1()["Hello, World!"],
            p()["This is a paragraph."],
            a(href="/")["home"],
        ]
    ],
]


html(
    children=[
        head(),
        body(
            children=[
                div(
                    classes="container bg-white",
                    children=[
                        h1("Hello, World!"),
                        p("This is a paragraph."),
                        a(href="/")("home"),
                    ],
                ),
            ],
        ),
    ]
)
