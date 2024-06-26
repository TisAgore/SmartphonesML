class MachineLearningFilter:
    import pandas as pd

    __data = pd.read_csv('Final dataset.csv', index_col='Unnamed: 0')
    __data = __data.reset_index(drop=True)
    __data.columns = ['rating', 'Price', 'Memory', 'Battery', 'Camera', 'smartphone']

    @staticmethod
    def find_smartphone(features):
        import statistics
        from sklearn.cluster import KMeans

        keys = []
        mask = []

        for key in features.keys():
            if features[key]:
                mask.append(features[key])
                keys.append(key)

        tmp_data = MachineLearningFilter.__data.copy()
        tmp_data = tmp_data[keys]
        ml = KMeans(n_clusters=40).fit(tmp_data.to_numpy())
        tmp_data['ml'] = ml.predict(tmp_data.to_numpy())
        s = []
        for i in keys:
            s.append(statistics.mean(features[i]))

        to_return = ml.predict([s])
        tmp_data = tmp_data[tmp_data['ml'] == to_return.tolist()[0]]

        data = MachineLearningFilter.__data
        data = data.iloc[tmp_data.index]

        return data['smartphone'].tolist()
