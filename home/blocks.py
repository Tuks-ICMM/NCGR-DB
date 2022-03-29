from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

# class TitleandTextBlock(blocks.StructBlock):
#     title = blocks.CharBlock(required=False)
#     text = blocks.TextBlock(required=False)

#     class Meta:
#         template = "home/streamfields.html"
#         icon = "edit"
#         label = "Title and text"


class CardBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=False)

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=False)),
                ("title", blocks.CharBlock(required=False)),
                ("text", blocks.TextBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False)),
            ]
        )
    )

    class Meta:
        template = "home/team_cards.html"
        icon = "edit"
        label = "Team Cards"


class AffiliationBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=False)

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=False)),
                ("title", blocks.CharBlock(required=False)),
                ("text", blocks.TextBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False)),
            ]
        )
    )

    class Meta:
        template = "home/affiliation_cards.html"
        icon = "edit"
        label = "Affiliation Cards"
