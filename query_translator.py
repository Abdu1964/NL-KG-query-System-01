# query_translator.py

class QueryTranslator:
    def __init__(self, neo4j_helper):
        self.neo4j_helper = neo4j_helper

    def translate(self, parsed_query):
        return f"MATCH (n:{parsed_query}) RETURN n"
