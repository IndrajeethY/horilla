from kite.settings import TEMPLATES

TEMPLATES[0]["OPTIONS"]["context_processors"].append(
    "kite_crumbs.context_processors.breadcrumbs",
)
