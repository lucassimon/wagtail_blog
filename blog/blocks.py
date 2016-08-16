# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# Stdlib imports

# Core Django imports

# Third-party app imports
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
# Stream field dependencies
# Imports from your apps


class ImageCarouselBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.TextBlock(required=False)
    video = EmbedBlock(required=False)

    class Meta:
        icon = 'image'


class GoogleMapBlock(blocks.StructBlock):
    map_long = blocks.CharBlock(
        required=True,
        max_length=255
    )

    map_lat = blocks.CharBlock(
        required=True,
        max_length=255
    )

    map_zoom_level = blocks.CharBlock(
        default=14,
        required=True,
        max_length=3
    )

    class Meta:
        template = 'core/blocks/google_map.html'
        icon = 'cogs'
        label = 'Google Map'
