FROM squidfunk/mkdocs-material

RUN pip install mkdocs-mermaid2-plugin

RUN mkdir -p /docs/

WORKDIR /docs/

COPY mkdocs /docs/

RUN mkdocs build

