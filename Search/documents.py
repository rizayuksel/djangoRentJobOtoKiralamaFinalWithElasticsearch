from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from Autos.models import Autos

@registry.register_document
class AutosDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'autos'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Autos # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'id',
            'title',
            'trademark',
            'model',
            'year',
            'gear',
            'fuel',
            'carClass',
            'horsePower',
            'baggageVolume',
        ]