import re

from marshmallow.schema import SchemaMeta
from marshmallow_jsonapi import Schema, fields
from marshmallow_jsonapi.fields import Relationship

from django_forest.utils.get_model import get_model

TYPE_CHOICES = {
    'String': fields.Str,
    'Number': fields.Number,
    'Boolean': fields.Boolean,
    'DateOnly': fields.Date,
    'Date': fields.DateTime,
    'Time': fields.Time,
    'Json': fields.Dict,  # maybe a fields.Mapping or fields.Raw,
}


class JsonApiSchema(type):
    _registry = {}

    def __new__(mcs, model_name, bases, attrs):
        klass = super(JsonApiSchema, mcs).__new__(mcs, model_name, bases, attrs)
        mcs._registry[model_name] = klass
        return klass


# Notice: handle metaclass conflict
class MarshmallowType(JsonApiSchema, SchemaMeta):
    pass


def getTypeName(name):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", name)


def create_json_api_schema(collection, ForestSchema):  # noqa: C901
    attrs = {}
    collection_name = collection['name']

    for field in collection['fields']:
        if field['reference'] is not None:
            related_name = field['reference'].split('.')[0]
            field_name = field['field']
            attrs[field_name] = Relationship(
                type_=getTypeName(related_name).lower(),
                many=field['relationship'] == 'HasMany',
                schema=f'{related_name}Schema',
                related_url=f'/forest/{collection_name}/{{{collection_name.lower()}_id}}/relationships/{related_name}',
                related_url_kwargs={f'{collection_name.lower()}_id': '<id>'},
            )
        else:
            attrs[field['field']] = TYPE_CHOICES.get(field['type'], fields.Str)()

    # Add id field if does not exist, taking pk (do not work for smart collection which need an id)
    if 'id' not in attrs:
        Model = get_model(collection_name)
        if Model:
            attrs['id'] = TYPE_CHOICES.get(ForestSchema.get_type(Model._meta.pk.get_internal_type()), fields.Str)()

    class MarshmallowSchema(Schema):

        # TODO, if we want modify how is returned the data, we need to override format_json_api_response
        # https://marshmallow-jsonapi.readthedocs.io/en/latest/api_reference.html#marshmallow_jsonapi.Schema.format_json_api_response
        # format_items and format_item will need to be updated

        # We add the id in the attributes
        def format_item(self, item):
            ret = super().format_item(item)
            if 'attributes' in ret:
                attributes = {
                    (self.fields[field].data_key or field): field for field in self.fields
                }
                for field_name, value in item.items():
                    attribute = attributes[field_name]
                    if attribute == 'id':
                        ret['attributes']['id'] = value

                if 'id' not in ret['attributes']:
                    Model = get_model(self.Meta.type_)
                    if Model:
                        ret['attributes']['id'] = ret['attributes'][Model._meta.pk.name]
                        ret['id'] = ret['attributes'][Model._meta.pk.name]

            return ret

        def get_attribute(self, obj, attr, default):
            value = super().get_attribute(obj, attr, default)
            if value.__class__.__name__ == 'ManyRelatedManager':
                value = value.all()
            return value

        class Meta:
            type_ = getTypeName(collection_name).lower()
            strict = True

    return MarshmallowType(f'{collection_name}Schema', (MarshmallowSchema,), attrs)