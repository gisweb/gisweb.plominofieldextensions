from Products.Archetypes.public import StringField, StringWidget
from Products.Archetypes.public import TextField, TextAreaWidget
from archetypes.schemaextender.field import ExtensionField
from Products.CMFPlomino.interfaces import IPlominoField
from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender

from .interfaces import IPlominoFieldExtension


class _ExtensionStringField(ExtensionField, StringField): pass

class _ExtensionTextField(ExtensionField, TextField): pass

class PlominoExtender(object):
    adapts(IPlominoField)
    implements(ISchemaExtender, IBrowserLayerAwareExtender)

    layer = IPlominoFieldExtension

    fields = [
	_ExtensionStringField(
            "cell_class",
            widget = StringWidget(
                label=u"Class name",
                description=u"BootStrap class name for this field",
            ),
        ),
        _ExtensionStringField(
            "tooltip_title",
            widget = StringWidget(
                label=u"Tooltip Title",
                description=u"Title of tooltip for this field",
            ),
        ),
        _ExtensionTextField(
            name='tooltip_description',
            widget=TextAreaWidget(
                label=u"Tooltip description",
                description=u"Will be displayed in the tooltip",
                rows=10,
            ),
        ),

    ]
    def __init__(self, context):
        self.context = context
    def getFields(self):
        return self.fields
