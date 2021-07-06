import json

def addUsernames(x):
    r = json.loads(x.to_json())
    r['_id'] = str(x.id)
    r['by'] = x.by.username
    r['created_on'] = x.id.generation_time
    return r

