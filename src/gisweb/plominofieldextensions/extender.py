from Products.Archetypes.public import StringField, TextField
from Products.Archetypes.public import StringWidget, TextAreaWidget
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
        _ExtensionTextField(
            name='fieldDescription',
            widget=TextAreaWidget(
                label=u"Field description",
                description=u"Detailed field description",
                rows=5,
            ),
        ),
        _ExtensionTextField(
            name='customAttributes',
            widget=TextAreaWidget(
                label=u"Custom attributes",
                description=u"Custom html5 attributes, example: data-brand=\"toyota\" data-model=\"prius\"",
                rows=5,
            ),
        ),
    ]
    def __init__(self, context):
        self.context = context
    def getFields(self):
        return self.fields
