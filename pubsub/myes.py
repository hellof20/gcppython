from elasticsearch import Elasticsearch

es = Elasticsearch("https://instance6.joey618.top:9200", basic_auth=('xxxxx','xxxxx'), verify_certs=False)

def insert(doc):
    result = es.index(index="glo-log-index", document=doc) 
    return result
