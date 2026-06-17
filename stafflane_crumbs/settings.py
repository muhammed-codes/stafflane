from stafflane.settings import TEMPLATES

TEMPLATES[0]["OPTIONS"]["context_processors"].append(
    "stafflane_crumbs.context_processors.breadcrumbs",
)
