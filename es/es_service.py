from es.es_config import EsConfig


class EsService(EsConfig):
    def search(self, searchable_text: str) -> object:
        params = {
            "query_string": {
                "query": searchable_text
            }
        }
        self.data['query']['bool']['must'].append(params)

        return self
