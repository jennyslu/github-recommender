import csv
import json
import numpy as np
from sklearn.cluster import KMeans

if __name__ == '__main__':
    with open('mappings/project_map.json') as f:
        project_map = json.load(f)

    # pandas fails read CSV normally instead
    with open('languages/languages.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        all_languages = reader.fieldnames
        project_ids = []
        data = np.zeros((len(project_map), len(all_languages)-1))
        i = 0
        for row in reader:
            project_name = row.pop('repo_name')
            project_id = project_map[project_name]
            project_ids.append(project_id)
            print('{} with id:{}'.format(project_name, project_id))
            data[i] = row.values()
            i += 1

    sums = data.sum(axis=1)[:,np.newaxis]
    sums[(sums < 1)] = 1
    props = data/sums
