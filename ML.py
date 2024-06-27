class MachineLearningFilter:
    import pandas as pd

    __data = pd.read_csv('Final dataset.csv', index_col='Unnamed: 0')
    __data = __data.reset_index(drop=True)
    __data.columns = ['rating', 'Price', 'Memory', 'Battery', 'Camera', 'smartphone']

    @staticmethod
    def find_smartphone(features):
        import pandas as pd
        import statistics
        from sklearn.cluster import KMeans

        tmp_data = MachineLearningFilter.__data.copy()
        keys = []
        mask = []

        for key in features.keys():
            if features[key]:
                if key != 'Brand':
                    mask.append(features[key])
                    keys.append(key)
                else:
                    brands = features['Brand']
                    brands = tuple(map(str.lower, brands))
                    tmp_data = tmp_data[tmp_data.smartphone.str.startswith(brands)]
                    tmp_data = tmp_data[tmp_data['smartphone'].str.startswith(brands)]

        tmp_data = tmp_data[keys]

        if len(tmp_data) < 5:
            return MachineLearningFilter.__data['smartphone'].tolist()
        elif len(tmp_data) < 50:
            n_cluster = 5
        elif len(tmp_data) < 100:
            n_cluster = 10
        else:
            n_cluster = len(tmp_data) // 20

        ml = KMeans(n_clusters=n_cluster).fit(tmp_data.to_numpy())
        tmp_data['ml'] = ml.predict(tmp_data.to_numpy())

        predict_data = []
        for i in keys:
            predict_data.append(statistics.mean(features[i]))

        to_return = ml.predict([predict_data])
        tmp_data = tmp_data[tmp_data['ml'] == to_return.tolist()[0]]

        data: pd.DataFrame = MachineLearningFilter.__data
        data = data.iloc[tmp_data.index]

        data = data.sort_values(by=['Camera', 'Memory', 'rating'], ascending=False).sort_values(by='Price')
        data = data[['Price', 'smartphone']].head(3)

        return data.to_numpy().tolist()
