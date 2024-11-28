import requests

def get_aggregated_score():
    url = f"http://localhost:9200/threat_scores/_search"
    query = {
        "size": 0,
        "aggs": {
            "department_avg": {
                "terms": {"field": "Department"},
                "aggs": {"avg_score": {"avg": {"field": "Threat_Score"}}}
            }
        }
    }
    response = requests.post(url, json=query)
    data = response.json()
    aggs = data['aggregations']['department_avg']['buckets']
    scores = {bucket['key']: bucket['avg_score']['value'] for bucket in aggs}
    print(f"Aggregated Threat Scores: {scores}")
    return scores



